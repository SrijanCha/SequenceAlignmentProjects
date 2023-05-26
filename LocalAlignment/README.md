# README

### Purpose: the programs in this project allow the user to take any FASTA formatted sequences and perform a local alignment on them by forming a MWT. In addition, several other programs exist to perform further analysis and experimentation.


### Required Packages
None

### Local Alignment.py

##### Description:

The basic unit of the Multiway Trie is the Node Class, which contains data, whether it is the end of a word, and what other letters are its children.


##### addWord

Takes the root node of the MWT and a string as input, attempts to add the word to the existing multiway trie.



###### main code blocks

The main code blocks require that the query texts be in file 'query.txt' and 'query2.txt'.

At In[9], use the 'start' variable to determine at what position in the database the user wishes to start pattern matching.

The remaining blocks of code exist solely for output.