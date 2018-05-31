# ControlFlowPathsListingProgram

This program can be used to list all the control flow paths of a java program.
To run this program
1: Run the python file "parse.py"
2: When it asks you to enter some text, enter the path to the java file.

The id of the nodes in the graph is given in their order of level order traversal of the decision tree the program forms.

# How it works

Nested if statements have some sort of recursive definition (since they form a decision TREE). So I used a stack to identify which statements were imbedded which. each block of code is considered as a node object defined in node.py. the position of the opening brace of that block identifies it uniquely. so, I save it in node.start and the start of the block that contains it in node.parent.

Then I filter out the blocks that are if,else if, or else statements and save them to a new array.

Finally, I identify the leaf nodes and create a child-to-parent dictionary to represent the tree.
To print all the paths of the tree, I start at a leaf node traverse towards the root of the tree while appending the id of each node at each step to an array. Then, I reverse the array and print the path in a formatted mannner. 

