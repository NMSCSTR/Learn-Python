tic_tac_toe = [
        [None, None, None], 
        [None, None, None],
        [None, None, None] 
    ]
#FIRST ROW WITH INDEX OF 0
tic_tac_toe[0][0] = "X" #0
tic_tac_toe[0][1] = "O" #1
tic_tac_toe[0][2] = "O" #2
#SECOND ROW WITH AN INDEX OF 1
tic_tac_toe[1][0] = "O"
tic_tac_toe[1][1] = "X"
tic_tac_toe[1][2] = "O"
#THIRD ROWS WITH AN INDEX OF 2
tic_tac_toe[2][0] = "X"
tic_tac_toe[2][1] = "X"
tic_tac_toe[2][2] = "X"

for rows in tic_tac_toe:
        print(rows)