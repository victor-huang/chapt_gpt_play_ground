"""
we want to using recursion to print a christmas tree on the screen, here an example output of a tree with 5 level:

    *
   ***
  *****
 *******
*********

Expansion:
once you print the desired three, you can decorate it with the printing of the top of the tree with a Red color star
"""


def printTreeLevel(level, totalLevels):
    # base case / stopping case

    # call itself again to solve for a "simpler" problem 
    printTreeLevel()


totalLevels = 10
printTreeLevel(1, totalLevels)
