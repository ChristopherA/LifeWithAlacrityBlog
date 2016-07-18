#!/usr/bin/python2.4
# -*- coding: utf-8 -*-

# Copyright 2008 Google Inc., 2016 Kevin Marks
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0.txt
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import codecs
import os.path
import logging
import re
import sys
import time
import urlparse
from xml.sax.saxutils import escape


__author__ = 'Kevin Marks via JJ Lueck (jlueck@gmail.com)'

########################
# Constants
########################


###########################
# Translation class
###########################

def appenditem(entry,name,value):
    l = entry.get(name,[])
    l.append(value)
    entry[name] = l

class MovableType2Hugo(object):
  """Performs the translation of MovableType text export to Blogger
     export format.
  """

  def __init__(self):
    self.next_id = 1
  
  def Translate(self, infile, outPath='post'):
    """Performs the actual translation to a Blogger export format.

    Args:
      infile: The input MovableType export file
      outfile: The output directory that the posts will be written to
    """
    # Calculate the last updated time by inspecting all of the posts
    last_updated = 0

    # These three variables keep the state as we parse the file
    feed=[]
    post_entry = {}                   # The current post entry
    comment_entry = None              # The current comment entry
    last_entry = None                 # The previous post entry if exists
    tag_name = None                   # The current name of multi-line values
    tag_contents = ''                 # The contents of multi-line values

    # Loop through the text lines looking for key/value pairs
    for line in infile:

      # Remove whitespace
      line = line.strip().lstrip(codecs.BOM_UTF8)

      # Check for the post ending token
      if line == '-' * 8:
        # If the body tag is still being read, add what has been read.
        if tag_name == 'BODY':
          post_entry['content'] = self._TranslateContents(tag_contents)

        # Add the post to our feed
        feed.append(post_entry)
        last_entry = post_entry

        # Reset the state variables
        post_entry = {}
        comment_entry = None
        tag_name = None
        tag_contents = ''
        continue

      # Check for the tag ending separator
      elif line == '-' * 5:
        # Get the contents of the body and set the entry contents
        if tag_name == 'BODY':
          post_entry['content'] = self._TranslateContents(tag_contents)

        # This is the start of the COMMENT section.  Create a new entry for
        # the comment and add a link to the original post.
        elif tag_name == 'COMMENT':
          comment_entry['content'] =self._TranslateContents(tag_contents)
          comment_entry['name'] = self._Encode(self._CreateSnippet(tag_contents))
          appenditem(post_entry,'comments',comment_entry)
          #in-reply to ?
          comment_entry = None

        # Get the contents of the extended body and append it to the
        # entry contents
        elif tag_name == 'EXTENDED BODY':
          newcontent= self._TranslateContents(tag_contents).strip()
          if post_entry and newcontent:
            post_entry['content'] += '<!--more-->' + self._TranslateContents(tag_contents)
          elif last_entry and last_entry['content'] and newcontent:
            last_entry['content'] += '<!--more-->' + self._TranslateContents(tag_contents)

        # Convert any keywords (comma separated values) into Blogger labels
        elif tag_name == 'KEYWORDS':
          for keyword in tag_contents.split(','):
            keyword = keyword.strip()
            if keyword != '':
              appenditem(post_entry,'category',keyword)

        # Reset the current tag and its contents
        tag_name = None
        tag_contents = ''
        continue

      # Split the line into key/value pairs
      elems = line.split(':')
      key = elems[0]
      value = ''
      if len(elems) > 1:
        value = ':'.join(elems[1:]).strip()

      # The author key indicates the start of a post as well as the author of
      # the post entry or comment
      if key == 'AUTHOR':
        # Add the author's name
        author_name = self._Encode(value)
        if not author_name:
          author_name = 'Anonymous'
        if tag_name == 'COMMENT':
          appenditem(comment_entry,'author',{'name':author_name})
        else:
          appenditem(post_entry,'author',{'name':author_name})

      # The title only applies to new posts
      elif key == 'TITLE' and tag_name != 'PING':
        post_entry['title'] = self._Encode(value)

      # If the status is a draft, mark it as so in the entry.  If the status
      # is 'Published' there's nothing to do here
      elif key == 'STATUS':
        if value == 'Draft':
          post_entry['draft'] = 'true'

      # Turn categories into labels
      elif key == 'CATEGORY':
        if value != '':
          appenditem(post_entry,'category',value)

      # Convert the date and specify it as the published/updated time
      elif key == 'DATE' and tag_name != 'PING':
        time_val = self._FromMtTime(value)
        entry = post_entry
        if tag_name == 'COMMENT':
          entry = comment_entry
        entry['published'] = time_val
        entry['updated'] = time_val

        # Check to see if this was the last post published (so far)
        seconds = time.mktime(time_val)
        last_updated = max(seconds, last_updated)

      # Convert all tags into Blogger labels
      elif key == 'TAGS':
        for keyword in value.split(','):
          keyword = keyword.strip()
          if keyword != '' :
            appenditem(post_entry,'category',keyword)

      # Update the author's email if it is present and not empty
      elif tag_name == 'COMMENT' and key == 'EMAIL' and len(value) > 0:
        comment_entry['author'][-1]['email'] = value

      # Update the author's URI if it is present and not empty
      elif tag_name == 'COMMENT' and key == 'URL' and len(value) > 0:
        comment_entry['author'][-1]['url'] = value

      # If any of these keys are used, they contain information beyond this key
      # on following lines
      elif key in ('COMMENT', 'BODY', 'EXTENDED BODY', 'EXCERPT', 'KEYWORDS', 'PING'):
        tag_name = key
        if key == 'COMMENT':
          comment_entry = {}
          
      # convert basename to slug
      elif key == 'BASENAME':
        post_entry['slug'] = value.strip()

      # keep orginal post url, but make it site relative
      elif key == 'UNIQUE URL':
        relative_url =  urlparse.urlsplit(value.strip()).path
        if relative_url: 
            post_entry['url'] = relative_url


      # These lines can be safely ignored
      elif key in ( 'ALLOW COMMENTS', 'CONVERT BREAKS',
                   'ALLOW PINGS', 'PRIMARY CATEGORY', 'IP', 'EMAIL'):
        continue

      # If the line is empty and we're processing the body, add a newline
      # break
      elif tag_name == 'BODY' and len(line) == 0:
        tag_contents += ''

      # This would be a line of content beyond a key/value pair
      elif len(key) != 0:
        tag_contents += line + '\n'

    # Serialize the feed object
    #outfile.write(str(feed))
    postcount=1;
    for entry in feed:
        slug = entry.get('slug','post_%s' % postcount)
        postcount = postcount+1
        with open("%s/%s.md" %(outPath,slug), 'w') as outfile:
            outfile.write('---\n') #YAML header
            for key in ('title', 'slug', 'url', 'draft'):
                if entry.get(key):
                    outfile.write('%s: "%s"\n' %(key, entry.get(key))) #simple fields
            if entry.get('category'):
                outfile.write('tags:\n')
                for tag in entry.get('category'):
                    outfile.write('  - "%s"\n' % tag)
            if entry.get('published'):
                outfile.write('date: "%s"\n' % self._ToBlogTime(entry.get('published')))
            outfile.write('---\n') #YAML footer
            outfile.write(entry.get('content'))
            # deal with comments mf2 indie style
            if entry.get("comments"):
                outfile.write('<footer><h3>Comments</h3>\n')
                for comment in entry.get("comments"):
                    outfile.write('<div class="u-comment h-cite">\n')
                    outfile.write('<p class="p-content p-name">%s</p>\n' % comment.get('content',''))
                    if comment.get('author'):
                        for author in comment.get('author'):
                            outfile.write('<a class="u-author h-card" href="%s">%s</a>\n' % (author.get('url','#'),author.get('name','anon')))
                    if comment.get('published'):
                        outfile.write('<time class="dt-published" datetime="%s">%s</time>\n' % (self._ToBlogTime(comment.get('published')), self._ToBlogTime(comment.get('published'))))
                    outfile.write('</div>\n')
                outfile.write('</footer>\n')
            if entry.get('url'):
                outfile.write('<p class="previous"><a href="/previous%s" rel="syndication">orginal layout</a></p>\n' % entry.get('url'))


  def _GetNextId(self):
    """Returns the next entry identifier as a string."""
    ret = self.next_id
    self.next_id += 1
    return str(self.next_id)

  def _CreateSnippet(self, content):
    """Creates a snippet of content.  The maximum size being 53 characters,
    50 characters of data followed by elipses.
    """
    content = re.sub('</?[^>/]+/?>', '', content)
    if len(content) < 50:
      return content
    return content[0:49] + '...'

  def _TranslateContents(self, content):
    #content = content.replace('\n', '<br/>')
    return self._Encode(content,False)

  def _Encode(self, content, stripQuotes=True):
    unicontent= content.decode('utf-8', 'replace')
    if stripQuotes:
        unicontent= unicontent.replace(u' "',u' “')
        unicontent= unicontent.replace(u'"',u'”')
    return unicontent.encode('utf-8')

  def _FromMtTime(self, mt_time):
    try:
      return time.strptime(mt_time, "%m/%d/%Y %I:%M:%S %p")
    except ValueError:
      return time.gmtime()
  # forcing pacific time here as mt has no TZ
  def _ToBlogTime(self, time_tuple):
    """Converts a time struct to a Blogger time/date string."""
    if time_tuple.tm_isdst:
        return time.strftime('%Y-%m-%dT%H:%M:%S-07:00', time_tuple)
    else:
        return time.strftime('%Y-%m-%dT%H:%M:%S-08:00', time_tuple) #

if __name__ == '__main__':
  if len(sys.argv) <= 1:
    print 'Usage: %s <movabletype_export_file>' % os.path.basename(sys.argv[0])
    print
    print ' Outputs the converted Hugo export file to standard out.'
    sys.exit(-1)
  path='post'
  if len(sys.argv) >= 2:
    path  = sys.argv[2]
  mt_file = open(sys.argv[1])
  translator = MovableType2Hugo()
  translator.Translate(mt_file,path)
  mt_file.close()
