import makerelative

makerelative.processfiles('raw dumps/www.lifewithalacrity.com','../scratchspace','http://www.lifewithalacrity.com')
## then flatten out the legacy domain too
makerelative.processfiles('../scratchspace','../lifewithalacrity.github.io','http://lifewithalacrity.blogs.com')