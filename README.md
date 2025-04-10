# K-means Clustering Assignment

This repository includes two implementations of the K-means clustering algorithm: one in C and one in Python. Both programs take a set of data points as input and cluster them into K groups based on the standard K-means algorithm. The final output is the list of centroids after convergence or after a fixed number of iterations.

The assignment was submitted for the Software Project course at Tel Aviv University.

## What’s Included

- kmeans.c – C implementation of the algorithm
- kmeans.py – Python implementation of the algorithm

## How It Works

The program expects:
- A number of clusters K (where 1 < K < N)
- A maximum number of iterations (optional in Python, default is 200)
- A dataset of data points

It uses the Euclidean distance to assign each point to the nearest cluster and recomputes the centroids until the centroids stop moving significantly (less than 0.001) or the iteration limit is reached.

All centroids are printed to standard output, formatted to exactly 4 decimal places.

## Running the Programs

### C Version

To compile the C code:

gcc -ansi -Wall -Wextra -Werror -pedantic-errors kmeans.c -o kmeans

To run it:
./kmeans K iter < input_data.txt
Replace `K` with the number of clusters and `iter` with the maximum number of iterations. Input is read from `stdin`.

### Python Version

To run the Python code:
python3 kmeans.py K iter input_data.txt

If `iter` is not provided, it defaults to 200. The input file must contain one data point per line, with comma-separated float values. The last line should be empty (as expected by the assignment).

Each line is a centroid. All numbers are printed with exactly 4 digits after the decimal point.

## Input Format

- The dataset must be a text file.
- Each line represents a point with comma-separated float values.
- All points must have the same dimension.
- The last line in the file is empty (required by the assignment specification).

## Constraints and Notes

- Valid K: must be greater than 1 and less than the number of data points.
- Valid iter: must be between 1 and 999.
- Use of any external Python libraries or C includes (beyond stdio.h, stdlib.h, math.h) is not allowed.
- In case of invalid input, the program prints a specific error message and exits.
- Memory must be properly freed in the C implementation.
- Floating-point values must be treated as `double` in C and `float` in Python.

## Summary

This assignment demonstrates how to implement K-means clustering from scratch in two languages, handle input and output cleanly, and manage convergence logic with precision.



