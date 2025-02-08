tic_tac_toe = [
     #0    #1    #2
    [None, None, None], #0
    [None, None, None], #1
    [None, None, None]  #2
]
# X X O
# O X O
# 0 X X

tic_tac_toe[0][0] = 'X'
tic_tac_toe[0][1] = 'X'
tic_tac_toe[0][2] = '0'

tic_tac_toe[1][0] = 'O'
tic_tac_toe[1][1] = 'X'
tic_tac_toe[1][2] = '0'

tic_tac_toe[2][0] = 'X'
tic_tac_toe[2][1] = 'X'
tic_tac_toe[2][2] = 'X'

for i in range(len(tic_tac_toe)):
    print(tic_tac_toe[i])
