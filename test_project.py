import numpy as np
import random


def create_board(n: int, m: int):
    board = [["."] * m for ligne in range(n)]
    return board


def print_board(board):
    # calcul longueur ligne (n) et colonne (m)
    colonnes = len(board[0])
    lignes = len(board)

    # première rangée compteur colonne
    space = True
    for colonne in range(colonnes):
        if space:
            print("      ", end="")
        space = False
        if colonne < 10:
            print(" ", end="    ")
        else:
            colonne = str(colonne)
            nbr_1 = colonne[0]
            print(nbr_1, end=" ")
    print("")

    # seconde rangée compteur colonne
    space = True
    for colonne in range(colonnes):
        if space:
            print("      ", end="")
            space = False
        if colonne < 10:
            print(colonne, end="    ")
        else:
            colonne = str(colonne)
            nbr_2 = colonne[1]
            print(nbr_2, end=" ")
    print("")

    # ligne en dessous du compteur de colonne
    space = True
    for colonne in range(colonnes):
        if space:
            print("    ", end="")
            space = False
        print("-----", end="")
    print("")

    # compteur nombre de lignes
    for ligne in range(lignes):
        if ligne < 10:
            print(" ", ligne, "|", end=" ")
            for index in range(len(board[ligne])):
                print(board[ligne][index], end="    ")
            print("|", end="")
            print("")
        else:
            ligne = str(ligne)
            print(ligne[0], ligne[1], "|", end=" ")
            ligne = int(ligne)
            for index in range(len(board[ligne])):
                print(board[ligne][index], end="    ")
            print("|", end="")
            print("")

    space = True
    for colonne in range(colonnes):
        if space:
            print("    ", end="")
            space = False
        print("-----", end="")
    print("")

def get_size(board):
    colonnes = len(board[0])
    lignes = len(board)
    res = (lignes, colonnes)
    return res


def get_neighbors(board, pos_x, pos_y):
    voisin = []
    for x in range(pos_x - 1, pos_x + 2):
        for y in range(pos_y - 1, pos_y + 2):
            if (x, y) == (pos_x, pos_y):
                pass
            elif x == -1 or y == -1:
                pass
            elif x >= get_size(board)[0] or y >= get_size(board)[1]:
                pass
            else:
                voisin.append((x, y))
    return voisin


def place_mines(reference_board, number_of_mines, first_pos_x, first_pos_y):
    voisin_debut = get_neighbors(reference_board, first_pos_x, first_pos_y)
    mines = []
    for nbr in range(number_of_mines):
        mines.append(0)
    x_max, y_max = get_size(reference_board)
    liste = []
    for ligne in range(x_max):
        for colonne in range(y_max):
            duo = (ligne, colonne)
            liste.append(duo)
    for elem in range(len(mines)):
        good = False
        while not good:
            emplacement = random.choice(liste)
            if emplacement not in voisin_debut and emplacement not in mines:
                good = True
                mines[elem] = emplacement

        mine_x = 0    #utiliser random.choice() (contient liste prend elem random) (enlever voisin_debut de la liste mise dans random.choice)
    return mines


def fill_in_board(reference_board):
    #nombre de mines pour test, à changer ensuite (utiliser sys.argv)
    global nbr_mines
    voisin_mines = []
    global mines
        #place_mines(reference_board, nbr_mines, pos_x, pos_y)
    for index in range(nbr_mines):
        mine = mines[index]
        x, y = mine
        reference_board[x][y] = "X"
        voisin_mines.append(get_neighbors(reference_board, x, y))
    for liste_mines in voisin_mines:
        for voisins in liste_mines:
            x, y = voisins
            if reference_board[x][y] == "X":
                pass
            elif reference_board[x][y] == ".":
                reference_board[x][y] = 1
            else:
                reference_board[x][y] += 1
    lignes, colonnes = get_size(reference_board)
    for li in range(lignes):
        for co in range(colonnes):
            if reference_board[li][co] == ".":
                reference_board[li][co] = 0
    #print_board(reference_board)



# def propagate_click(game_board, reference_board, pos_x , pos_y):
    
#     if reference_board[pos_x][pos_y] == 0 :
        
#         # Le problème vient de cet appel                👇     👇
#         # Récursivement il ne kiffe pas (trop d'appel)
#         voisins_click = get_neighbors(reference_board, pos_x, pos_y)
        
#         game_board[pos_x][pos_y] = reference_board[pos_x][pos_y]
        
#         longueur = len(voisins_click)
        
#         for index in range(longueur):
#             x, y = voisins_click[index][0], voisins_click[index][1]
#             while reference_board[x][y] == 0:
#                 propagate_click(game_board, reference_board, x, y)



def propagate_click(game_board, reference_board, pos_x, pos_y):
    # Pour le premier print
    game_board[pos_x][pos_y] = reference_board[pos_x][pos_y]
    
    # Propage le click 
    neighbors = get_neighbors(reference_board, pos_x, pos_y)
    for x, y in neighbors:
        if game_board[x][y] == ".":
            game_board[x][y] = reference_board[x][y]
            if reference_board[x][y] == "0":
                propagate_click(game_board, reference_board, x, y)
            



###################################################
##########     partie test fonctions     ##########
###################################################

##################################
#####   CONSTANTES      ##########
##################################

lignes, colonnes = 12, 11
pos_x, pos_y = 11, 10
first_pos_x, first_pos_y = 8,5
nbr_mines = 10

##################################
##### REFERENCE_BOARD   ##########
##################################

reference_board = create_board(lignes, colonnes)

print("\n")
print("Dimension du reference_board : ", get_size(reference_board), "\n")

mines = place_mines(reference_board, nbr_mines,first_pos_x, first_pos_y)

print(f"Les voisins de ({pos_x},{pos_y}) sont : \n {get_neighbors(reference_board, pos_x, pos_y)} \n ")
print(f"Les mines sont : \n {mines} \n")

fill_in_board(reference_board)

print("<-----------   REFERENCE BOARD    ------------>")
print_board(reference_board)
print("\n \n")

##################################
######  GAME_BOARD        ########
##################################

game_board = create_board(lignes, colonnes)

propagate_click(game_board,reference_board,first_pos_x,first_pos_y)

print("<-----------   GAME BOARD    ------------>")
print_board(game_board)
print("\n \n")





