# sequence_alignment
Tutorial: Sequence Alignment using Dynamic Programming
Sequence alignment is a fundamental technique used to compare and identify similarities between biological sequences, such as DNA or protein sequences. Dynamic programming is a powerful approach commonly used for sequence alignment. In this tutorial, we will walk you through a Python script that performs sequence alignment using dynamic programming and prints the alignment matrix along with the optimal alignment of the sequences.
Prerequisites
Before getting started, ensure you have the following prerequisites:
1.	Basic understanding of Python programming.
2.	Familiarity with bioinformatics concepts like DNA sequences, sequence alignment, and dynamic programming.
Script Overview
The script provided performs sequence alignment between two input sequences and prints the alignment matrix and the aligned sequences. Here's a brief overview of the script:
1.	Import necessary libraries:
a.	numpy (as np): Used to create and manipulate arrays efficiently.
2.	Define the sequence_alignment function:
a.	This function takes two input sequences (reference and biocharm) and optional scores for matches, mismatches, and gaps.
b.	It initializes an alignment score matrix and an arrow matrix.
c.	The matrix is filled using dynamic programming to calculate the alignment scores.
d.	Arrows are used to indicate the optimal path in the alignment matrix.
3.	Calculate alignment scores:
•	The function calculates alignment scores using dynamic programming.
•	It considers match, mismatch, deletion, and insertion scores to determine the optimal alignment score at each position.
•	Scoring:
•	match_score: Score assigned to matching characters.
•	mismatch_score: Score assigned to mismatched characters.
•	gap_score: Penalty score for introducing a gap (insertion or deletion).
4.	Print the alignment matrix:
•	The alignment matrix is printed to visualize the dynamic programming process.
•	Rows correspond to the reference sequence, and columns correspond to the biocharm sequence.
•	The matrix displays alignment scores along with arrows indicating the optimal path.
5.	Backtrack to find the alignment:
•	Starting from the bottom-right corner of the matrix, the script traces back to find the optimal alignment of sequences.
•	Arrows are used to determine whether to match characters, insert gaps, or delete characters.
Arrows represent:
•	↖ or "/" for diagonal movement (match/mismatch)
•	"↑" for upward movement (deletion)
•	"←" for leftward movement (insertion)
6.	Example usage:
•	Two example sequences, reference and biocharm, are provided.
•	The sequence_alignment function is called to perform sequence alignment.
•	The aligned sequences are printed as output.
How to Use the Script
1.	Make sure you have Python installed on your system.
2.	Copy and paste the provided script into a python mathar@octopus:~/tmp/seq_alignment3/5_align.py. Download it
3.	Modify the reference and biocharm sequences according to your specific use case.
4.	Run the script using the following command: python3 5_align.py 
5.	The script will output the alignment matrix and the aligned sequences for the given input sequences.
