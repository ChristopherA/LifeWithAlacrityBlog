import os
import shutil
import sys
import absrel
class Error(Exception):
    """Base class for exceptions in this module."""
    pass

def processfiles(src, dst, base_url):
    names = os.listdir(src)
    try:
        os.makedirs(dst)
    except OSError as err:
        print err.args[0]
        pass
    errors = []
    for name in names:
        if name.startswith('.DS_'): #apparently '.shared' is a typepad path o_O
            print "skipping '%s'" % name
            continue
        srcname = os.path.join(src, name)
        dstname = os.path.join(dst, name)
        print dstname
        try:
            if os.path.isdir(srcname):
                newbase = "%s/%s" % (base_url,name)
                print "recurse with name '%s', srcname '%s', base_url, '%s'" % (name, srcname,  newbase)
                processfiles(srcname, dstname, newbase )
            elif srcname.endswith(".html"):
                with open(srcname, 'r') as f:
                    relhtml = absrel.relativize(f.read(), base_url)
                    with open(dstname, 'w') as fo:
                        fo.write(relhtml.encode('utf-8'))
            else:
                shutil.copy2(srcname, dstname)
        except (IOError, os.error) as why:
            print 
            errors.append((srcname, dstname, str(why)))
        # catch the Error from the recursive processfiles so that we can
        # continue with other files
        except Error as err:
            errors.extend(err.args[0])
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
    try:
        shutil.copystat(src, dst)
    except WindowsError:
        # can't copy file access times on Windows
        pass
    except OSError as why:
        errors.extend((src, dst, str(why)))
    if errors:
        raise Error(errors)


