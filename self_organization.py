# -*- coding: utf-8 -*-
# Learning involves selection of postsynaptic unit with greater activity (“Hard winner-take-all”) 
# followed by Hebbian learning followed by normalization (multiply by oldsumW/newsumW)

import numpy as np

def self_organize(connectivity_matrix, pattern):
    # Convert the matrix and patterns to numpy arrays
    connectivity_matrix = np.array(connectivity_matrix, dtype=float)
    pattern = np.array(pattern, dtype=float)

    # Figure out which postsynaptic unit will win
    activity = np.dot(connectivity_matrix, pattern)
    winner = np.argmax(activity)

    # Determine activity depending on winner
    if winner == 0:
        activity = np.array([[1],[0]])
    elif winner == 1:
        activity = np.array([[0],[1]])
    else:
        activity = np.array([[0],[0]])

    # Apply Hebbian learning
    W = np.dot(activity, pattern.transpose())

    # Add the new weights to the old weights
    new_connectivity_matrix = connectivity_matrix + W

    # Normalize the new weights
    oldsumW = np.sum(connectivity_matrix, axis=1)[winner]
    newsumW = np.sum(new_connectivity_matrix, axis=1)[winner]
    new_connectivity_matrix[winner] *= oldsumW/newsumW

    return new_connectivity_matrix
   

# problem information
matrix = [[2, 1, 1], [1, 2, 1]]
pattern1 = [[1],[0],[1]]
pattern2 = [[0],[1],[0]]

# find the steady state
newIteration = matrix
for i in range(100):
    if i%2 == 0:
        newIteration = self_organize(newIteration, pattern1)
    else:
        newIteration = self_organize(newIteration, pattern2)
    if i < 4:
        print(i)
        print(newIteration)
        print(" ")

print("steady state")
print(newIteration)