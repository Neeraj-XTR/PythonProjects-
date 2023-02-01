listy = []
listz = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
for i in range(1, 10):
    listy.append(i)


def playing_field():
    print(f'{listz[0][0]} | {listz[0][1]} | {listz[0][2]}')
    print("--+---+--")
    print(f'{listz[1][0]} | {listz[1][1]} | {listz[1][2]}')
    print("--+---+--")
    print(f'{listz[2][0]} | {listz[2][1]} | {listz[2][2]}')
    return ""


def player1():
    print("Player 1 turn ")
    print("Enter the row and  column number to give the entry")
    row_entry = int(input())
    col_entry = int(input())
    for i in range(3):
        for j in  range(3):
            if i == row_entry and j == col_entry:
                listz[i][j] = "X"
                return playing_field()


def player2():
    print("Player 2 turn ")
    print("Enter the row and  column number to give the entry")
    row_entry = int(input())
    col_entry = int(input())
    for i in range(3):
        for j in range(3):
            if i == row_entry and j == col_entry:
                listz[i][j] = "O"
                return playing_field()

def win_condition():
    if listz[0][0]==listz[0][1] and listz[0][1]==listz[0][2] and listz[0][0]!=' ':
        if listz[0][0]=="X":
            print("You Win!!")
            return 1

    elif listz[1][0]==listz[1][1] and listz[1][1]==listz[1][2] and listz[1][0]!=' ':
        if listz[1][0]=="X":
            print("You Win!!")
            return 1

    elif listz[2][0]==listz[2][1] and listz[2][1]==listz[2][2] and listz[2][0]!=' ':
        if listz[2][0]=="X":
            print("You Win!!")
            return 1

    elif listz[0][0]==listz[1][0] and listz[1][0]==listz[2][0] and listz[0][0]!=' ':
        if listz[0][0]=="X":
            print("You Win!!")
            return 1

    elif listz[0][1]==listz[1][1] and listz[1][1]==listz[2][1] and listz[0][1]!=' ':
        if listz[0][1]=="X":
            print("You Win!!")
            return 1

    elif listz[0][2]==listz[1][2] and listz[1][2]==listz[2][2] and listz[0][2]!=' ':
        if listz[0][2]=="X":
            print("You Win!!")
            return 1

    elif listz[0][0]==listz[1][1] and listz[1][1]==listz[2][2] and listz[0][0]!=' ':
        if listz[0][0]=="X":
            print("You Win!!")
            return 1

    elif listz[0][2]==listz[1][1] and listz[1][1]==listz[2][0] and listz[0][2]!=' ':
        if listz[0][2]=="X":
            print("You Win!!")
            return 1

    if listz[0][0]==listz[0][1] and listz[0][1]==listz[0][2] and listz[0][0]!=' ':
        if listz[0][0]=="O":
            print("You Win!!")
            return 2

    elif listz[1][0]==listz[1][1] and listz[1][1]==listz[1][2] and listz[1][0]!=' ':
        if listz[1][0]=="O":
            print("You Win!!")
            return 2

    elif listz[2][0]==listz[2][1] and listz[2][1]==listz[2][2] and listz[2][0]!=' ':
        if listz[2][0]=="O":
            print("You Win!!")
            return 2

    elif listz[0][0]==listz[1][0] and listz[1][0]==listz[2][0] and listz[0][0]!=' ':
        if listz[0][0]=="O":
            print("You Win!!")
            return 2

    elif listz[0][1]==listz[1][1] and listz[1][1]==listz[2][1] and listz[0][1]!=' ':
        if listz[0][1]=="O":
            print("You Win!!")
            return 2

    elif listz[0][2]==listz[1][2] and listz[1][2]==listz[2][2] and listz[0][2]!=' ':
        if listz[0][2]=="O":
            print("You Win!!")
            return 2

    elif listz[0][0]==listz[1][1] and listz[1][1]==listz[2][2] and listz[0][0]!=' ':
        if listz[0][0]=="O":
            print("You Wi!!")
            return 2

    elif listz[0][2]==listz[1][1] and listz[1][1]==listz[2][0] and listz[0][2]!=' ':
        if listz[0][2]=="O":
            print("You Win!!")
            return 2

# def win_condition():
#
#     def compare():
#         yield 1
#         yield 2
#         yield 3
#
#     for i in range(len(listz)):
#         for j in range(len(listz)):
#             x = compare()
#             y = compare()
#             q = compare()
#             w = compare()
#             e = compare()
#             r = compare()
#             if (i == 0 and x.__next__() == j) and (i == 0 and x.__next__() == j) and (i == 0 and x.__next__() == j):
#                 print("Player one has won")
#
#             elif (i == 1 and y.__next__() == j) and (i == 0 and y.__next__() == j) and (i == 0 and y.__next__() == j):
#                 print("player one has won")
#             elif (i == 2 and q.__next__() == j) and (i == 0 and q.__next__() == j) and (i == 0 and q.__next__() == j):
#                 print("Player 0 has won")
#             elif (j == 0 and w.__next__() == j) and (j == 0 and w.__next__() == i) and (j == 0 and w.__next__() == i):
#                 print("Player 0 has won")
#             elif (j == 1 and e.__next__() == j) and (j == 0 and e.__next__() == i) and (j == 0 and e.__next__() == i):
#                 print("Player 0 has won")
#             elif (j == 2 and r.__next__() == j) and (j == 0 and r.__next__() == i) and (j == 0 and r.__next__() == i):
#                 print("Player 0 has won")
#             elif (i == 0 and j == 0) and (i == 1 and j == 1) and (i == 2 and j == 2):
#                 print("PLayer 0 has won")
#             elif (i == 2 and j == 0) and (i == 1 and j == 1) and (i == 0 and j == 2):
#                 print("PLayer 0 has won")


def taking_entry():
    choice = int(input("Chose X or O:\nfor X press 1 for O press 2"))
    print(playing_field())
    if choice == 1:
        while choice != 0:
            player1()
            if win_condition() == 1:
                break
            player2()
            if win_condition() == 2:
                break
    else:
        while choice != 0:
            player2()
            if win_condition() == 2:
                break
            player1()
            if win_condition() == 1:
                break

print(taking_entry())

# def compare(n):
#    if n == 1 or n == 2 or n == 3:
#         return True
#     else:
#         return False
#
#
# for iin range(3):
#     for jin range(3):
#        if i == 1 and compare(j) == True:
#             print("Player one has won")
#         elif i ==2 and compare(j) == True:
#             print("player one has won")
#         elif i == 3 and compare(j) == True:
#             print("Player 1 has won")
#         elif j == 1 and compare(i) == True:
#             print("Player 1 has won")
#         elif j == 2 and compare(i) == True:
#             print("Player 1 has won")
#         elif j == 3 and compare(i) == True:
#             print("Player 1 has won")
#         elif (i == 1 and j == 1) and (i == 2 and j == 2) and (i == 3 and j == 3):
#             print("PLayer 1 has won")
#         elif (i == 3 and j == 1) and (i == 2 and j == 2) and (i == 1 and j == 3):
#             print("PLayer 1 has won")