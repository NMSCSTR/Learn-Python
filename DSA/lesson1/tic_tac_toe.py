tic_tac_toe = [
    #0      #1   #2 - Elements
    [None, None, None], #0 - List or row
    [None, None, None], #1
    [None, None, None]  #2
]

# X X O - first row
# O X O - second row
# 0 X X - third row

tic_tac_toe[0][0] = 'X' # Elements inside in first row
tic_tac_toe[0][1] = 'X' # Elements inside in first row
tic_tac_toe[0][2] = 'O' # Elements inside in first row

tic_tac_toe[1][0] = 'O' # Elements inside in second row
tic_tac_toe[1][1] = 'X' # Elements inside in second row
tic_tac_toe[1][2] = 'O' # Elements inside in second row

tic_tac_toe[2][0] = 'O' # Elements inside in third row
tic_tac_toe[2][1] = 'X' # Elements inside in third row
tic_tac_toe[2][2] = 'X' # Elements inside in third row

for row in tic_tac_toe: # Traversing the row
    for element in row: # Traversing the element inside in row
        print(element)

