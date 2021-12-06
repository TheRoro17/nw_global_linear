import numpy as np
import math


# Exo 1:

def init_S(x, y):
    S = np.full((len(x) + 1, len(y) + 1), -math.inf)
    return S


# Exo 2:

def init_B(x, y):
    B = np.full((len(x) + 1, len(y) + 1), None)
    return B


# Exo 3:

def fill_S_corner(S):
    S[0, 0] = 0
    return S


# Exo 4:

def fill_B_corner(B):
    B[0, 0] = None
    return B


# Exo 5:

def fill_S_border(S, e):
    # la première ligne
    for i in range(1, S.shape[1]):
        S[0, i] = e * i
    # la première colonne
    for j in range(1, S.shape[0]):
        S[j, 0] = e * j
    return S


# Exo 6:

def fill_B_border(B):
    # la première ligne
    for i in range(1, B.shape[1]):
        B[0, i] = (0, 0)
    # la première colonne
    for j in range(1, B.shape[0]):
        B[j, 0] = (0, 0)
    return B


# Exo 7:

def diag_score(S, i, j, x, y, sigma):
    dico = {"A": 0, "T": 1, "G": 2, "C": 3}
    # sigma1 c'est sigma depuis la matrice sigma
    sigma1 = sigma[dico[x[i - 1]], dico[y[j - 1]]]

    # S1 c'est sigma en diag
    S1 = S[i - 1, j - 1]

    return S1 + sigma1


# Exo 8:

def left_score(S, i, j, gamma):
    # S1 c'est sigma à gauche
    S1 = S[i, j - 1]

    return gamma + S1


# Exo 9:

def up_score(S, i, j, gamma):
    # S1 c'est sigma en haut
    S1 = S[i - 1, j]

    return gamma + S1


# Exo 10:

def max_score(S, i, j, x, y, sigma, gamma):
    maxim = np.amax(np.array([diag_score(S, i, j, x, y, sigma), left_score(S, i, j, gamma), up_score(S, i, j, gamma)]))
    # print(np.array([diag_score(S, i, j, x, y, sigma), left_score(S, i, j, gamma), up_score(S, i, j, gamma)]))
    return maxim


# Exo 11:

def max_score_idx(S, i, j, x, y, sigma, gamma):
    maxim = np.argmax([diag_score(S, i, j, x, y, sigma), left_score(S, i, j, gamma), up_score(S, i, j, gamma)])
    if maxim == 0:
        return i - 1, j - 1
    elif maxim == 1:
        return i, j - 1
    else:
        return i - 1, j


# Exo 12:

def nw_global_linear(x, y, sigma, gamma):
    S = fill_S_border(fill_S_corner(init_S(x, y)), gamma)
    B = fill_B_border(fill_B_corner(init_B(x, y)))
    for i in range(1, len(x) + 1):
        for j in range(1, len(y) + 1):
            S[i, j] = max_score(S, i, j, x, y, sigma, gamma)
            B[i, j] = max_score_idx(S, i, j, x, y, sigma, gamma)
    return S, B


# Exo 13:

def score(S):
    return S[S.shape[0] - 1, S.shape[1] - 1]


# Exo 14:

def score_idx(S):
    return S.shape[0] - 1, S.shape[1] - 1


# Exo 15:

def backtrack(x, y, S, B):
    start_pos = score_idx(S)
    pos_x = start_pos[0]
    pos_y = start_pos[1]
    seq_x = ""
    seq_y = ""
    while B[pos_x, pos_y] is not None:
        dir_x = B[pos_x, pos_y][0]
        dir_y = B[pos_x, pos_y][1]
        # cas fleche up
        if pos_x - 1 == dir_x and pos_y == dir_y:
            seq_x = x[pos_x - 1] + seq_x
            seq_y = "-" + seq_y
            pos_x = dir_x
            pos_y = dir_y
        # cas fleche diag
        elif pos_x - 1 == dir_x and pos_y - 1 == dir_y:
            seq_x = x[pos_x - 1] + seq_x
            seq_y = y[pos_y - 1] + seq_y
            pos_x = dir_x
            pos_y = dir_y
        # cas fleche left
        elif pos_x == dir_x and pos_y - 1 == dir_y:
            seq_x = "-" + seq_x
            seq_y = y[pos_y - 1] + seq_y
            pos_x = dir_x
            pos_y = dir_y
        elif dir_x == 0 and dir_y == 0:
            seq_x = "-" + seq_x
            seq_y = y[pos_y - 1] + seq_y
            if pos_x == 0:
                pos_x = pos_x
                pos_y = pos_y - 1
            if pos_y == 0:
                pos_x = pos_x - 1
                pos_y = pos_y
    return seq_x, seq_y


# Exo 16:

def align_nw_global_linear(x, y, sigma, gamma):
    S = nw_global_linear(x, y, sigma, gamma)[0]
    B = nw_global_linear(x, y, sigma, gamma)[1]
    return score(S), backtrack(x, y, S, B)
