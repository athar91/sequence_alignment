from __future__ import print_function
import numpy as np

def sequence_alignment(reference, biocharm, match_score=1, mismatch_score=-1, gap_score=-2):
    # Create a matrix to store alignment scores
    matrix = np.zeros((len(reference) + 1, len(biocharm) + 1))
    arrows = [[" " for _ in range(len(biocharm) + 1)] for _ in range(len(reference) + 1)]

    # Initialize the first row and column with gap penalties
    for i in range(len(reference) + 1):
        matrix[i][0] = i * gap_score
    for j in range(len(biocharm) + 1):
        matrix[0][j] = j * gap_score

    # Fill the matrix using dynamic programming
    for i in range(1, len(reference) + 1):
        for j in range(1, len(biocharm) + 1):
            match = matrix[i-1][j-1] + (match_score if reference[i-1] == biocharm[j-1] else mismatch_score)
            delete = matrix[i-1][j] + gap_score
            insert = matrix[i][j-1] + gap_score
            matrix[i][j] = max(match, delete, insert)
            if matrix[i][j] == match:
                arrows[i][j] = "\\"
            elif matrix[i][j] == delete:
                arrows[i][j] = "^"
            else:
                arrows[i][j] = "<"

    # Determine the width for each cell in the matrix
    max_score_width = max(len(str(int(np.max(matrix)))), len("Score"))
    cell_width = max(max_score_width, 3)  # At least 3 for arrows

    # Print the alignment matrix with sequences and arrows
    print("Alignment Matrix:")
    print(" " * (cell_width + 1), end="")
    print("  ".join(biocharm))

    for i in range(len(reference) + 1):
        if i > 0:
            print(reference[i-1].rjust(cell_width), end=" ")
        else:
            print(" " * cell_width, end=" ")

        for j in range(len(biocharm) + 1):
            cell_content = str(int(matrix[i][j])).rjust(cell_width) + arrows[i][j]
            print(cell_content, end="  ")
        print()

    # Backtrack to find the alignment
    alignment_reference = ''
    alignment_biocharm = ''
    i, j = len(reference), len(biocharm)
    while i > 0 and j > 0:
        if arrows[i][j] == "\\":
            alignment_reference = reference[i-1] + alignment_reference
            alignment_biocharm = biocharm[j-1] + alignment_biocharm
            i -= 1
            j -= 1
        elif arrows[i][j] == "^":
            alignment_reference = reference[i-1] + alignment_reference
            alignment_biocharm = '-' + alignment_biocharm
            i -= 1
        else:
            alignment_reference = '-' + alignment_reference
            alignment_biocharm = biocharm[j-1] + alignment_biocharm
            j -= 1

    while i > 0:
        alignment_reference = reference[i-1] + alignment_reference
        alignment_biocharm = '-' + alignment_biocharm
        i -= 1
    while j > 0:
        alignment_reference = '-' + alignment_reference
        alignment_biocharm = biocharm[j-1] + alignment_biocharm
        j -= 1

    return alignment_reference, alignment_biocharm

# Example usage
reference = "ATCTGAT"
biocharm = "TGCATA"
alignment_reference, alignment_biocharm = sequence_alignment(reference, biocharm)

print("\nReference alignment:", alignment_reference)
print("BioCharm alignment:", alignment_biocharm)
