#!/usr/bin/env python3
import numpy as np

def main():
    # We want to solve the system:
    #   2x + 3y = 5
    #   4x -  y = 11
    #
    # In matrix form, this is:
    #   A * x = b
    #
    # Where A is the coefficient matrix, x is the vector of unknowns,
    # and b is the constants vector.

    # Define the coefficient matrix A and constants vector b
    A = np.array([[2, 3],
                  [4, -1]])
    b = np.array([5, 11])

    print("Coefficient matrix A:")
    print(A)
    print("\nConstants vector b:")
    print(b)

    # Calculate the determinant of A to check if it is invertible.
    det = np.linalg.det(A)
    print("\nDeterminant of A:", det)

    if det != 0:
        # Calculate the inverse of A using numpy
        A_inv = np.linalg.inv(A)
        print("\nInverse of A:")
        print(A_inv)

        # Solve for x (which is the vector [x, y]) by multiplying A_inv with b
        solution = np.dot(A_inv, b)
        print("\nSolution vector [x, y]:")
        print(solution)
    else:
        print("\nThe determinant is zero, so the inverse of A does not exist.")
        print("This means the system may not have a unique solution.")

if __name__ == "__main__":
    main()