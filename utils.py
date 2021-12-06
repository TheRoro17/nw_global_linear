import numpy as np


# Exo 17:

def gen_sigma(match, transition, transversion):
    # gen sigma
    sigma = np.full((4, 4), None)

    for i in range(sigma.shape[1]):
        for j in range(sigma.shape[0]):
            if i == j:
                sigma[i, j] = match
            elif i - 1 == j or i == j - 1:
                sigma[i, j] = transversion
            elif (i == sigma.shape[0] - 1 and j == 0) or (j == sigma.shape[1] - 1 and i == 0):
                sigma[i, j] = transversion
            else:
                sigma[i, j] = transition

    return sigma


# Exo 18:


def print_backtrack(B):
    pos_x = B.shape[0] - 1
    pos_y = B.shape[1] - 1
    while B[pos_x, pos_y] is not None:
        dir_x = B[pos_x, pos_y][0]
        dir_y = B[pos_x, pos_y][1]
        # cas fleche up
        if pos_x - 1 == dir_x and pos_y == dir_y:
            B[pos_x, pos_y] = "U"
            pos_x = dir_x
            pos_y = dir_y
        # cas fleche diag
        elif pos_x - 1 == dir_x and pos_y - 1 == dir_y:
            B[pos_x, pos_y] = "D"
            pos_x = dir_x
            pos_y = dir_y
        # cas fleche left
        elif pos_x == dir_x and pos_y - 1 == dir_y:
            B[pos_x, pos_y] = "L"
            pos_x = dir_x
            pos_y = dir_y
        elif dir_x == 0 and dir_y == 0:
            B[pos_x, pos_y] = "L"
            if pos_x == 0:
                pos_x = pos_x
                pos_y = pos_y - 1
            if pos_y == 0:
                pos_x = pos_x - 1
                pos_y = pos_y
    print(B)
    for i in range(B.shape[0]):
        for j in range(B.shape[1]):
            if j == B.shape[1] - 1:
                if B[i, j] is None:
                    print("0", end="\n")
                elif B[i, j] == "U":
                    print("U", end="\n")
                elif B[i, j] == "L":
                    print("L", end="\n")
                elif B[i, j] == "D":
                    print("D", end="\n")
                elif B[i, j] == (0, 0):
                    print("0", end="\n")
                else:
                    print("0", end="\n")
            else:
                if B[i, j] is None:
                    print("0", end=" ")
                elif B[i, j] == "U":
                    print("U", end=" ")
                elif B[i, j] == "L":
                    print("L", end=" ")
                elif B[i, j] == "D":
                    print("D", end=" ")
                elif B[i, j] == (0, 0):
                    print("0", end=" ")
                else:
                    print("0", end=" ")
