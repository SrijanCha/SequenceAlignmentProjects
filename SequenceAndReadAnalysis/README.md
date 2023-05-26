# README

### Purpose: the programs in this project allow the user to take any FASTA formatted sequences and perform a local alignment on them. In addition, several other programs exist to perform further analysis and experimentation.





### Required Packages
###### numpy
install using 'pip3 install numpy' if using python3

###### argparse
install using 'pip3 install argparse' if using python3



### locAL.py
###### Purpose:
Takes a file with pairs of strings delineated by newlines, and 3 numeral parameters to determine the best local alignment of the two sequences. Outputs the highest score and the length of the longest alignment. Optionally outputs the actual sequence in BLAST format.

###### Usage:
locAL.py <seq_filename> -m M -s S -d D [-a]

- <seq_filename> the name or path of the file
- m the score awarded if characters match
- s the score taken if characters don't match
- d the score taken if insertion or deletion is found.
- a (optional) include if alignment sequences need to be output.

###### Output:
Prints to console a 2 line message with the highest score of the alignment, followed by the length of the alignment. If '-a' flag is added, will print 3 additional lines, the two sequences and the alignment in the middle, in BLAST format.

###### IMPORTANT NOTES REGARDING OUTPUT
It is highly recommended to redirect outputs to a file using the following syntax:

locAL.py <seq_filename> -m M -s S -d D [-a] > <outfile_name>

The output may be lengthy, and will produce a lot of text. 





### randomDNA.py
###### Purpose:
Takes two numerical parameters, length and count, and produces a file 'sequences.dat' that contains 'count' number of sequences, each 'length' characters long. The sequences are DNA only. In addition, it outputs to the console a small summary with information regarding the frequency of each character in the sequences produced.

###### Usage
randomDNA.py \<count> \<length>

- \<count> the number of sequences needed to be produced
- \<length> the length of each sequence in characters

###### Output:
Writes to a file 'sequences.dat' the list of all sequences separated by a newline. Then, prints to console a summary.


###### IMPORTANT NOTES REGARDING OUTPUT
It is highly recommended to redirect console output to a file using the following syntax:

randomDNA.py \<count> \<length> > sequences.sum




