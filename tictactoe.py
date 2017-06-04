board = [[' ' for i in range(3)] for i in range(3)]
# marker = 'X'
player_one = 1
player_one_score = 0
player_two_score = 0

# board[2][0] = marker
# board[1][1] = marker
# board[0][2] = marker

def printBoard():
	global board
	horizontal = "   --- --- --- "
	print("    1   2   3")
	for i, row in enumerate(board):
		print(horizontal)
		row_string = "{} ".format(i + 1)
		for marker in row:
			row_string += "| {} ".format(marker)
		row_string += "|"
		print(row_string)
	print(horizontal)

def clearBoard():
	global board
	for row in range(3):
		for col in range(3):
			board[row][col] = ' '


def togglePlayer():
	global player_one
	player_one = not player_one

def isValidSelection( selection ):
	try:
		selection = int(selection)
		return selection >= 1 and selection <= 3
	except ValueError:
		return False

def isWinningRow( row ):
	global board
	marker = board[row][0]
	if marker != ' ':
		for col in range(3):
			if board[row][col] != marker:
				return False
		else:
			return True
	else:
		return False

def isWinningCol( col ):
	global board
	marker = board[0][col]
	if marker != ' ':
		for row in range(3):
			if board[row][col] != marker:
				return False
		else:
			return True
	else:
		return False

def isWinningTopLeftDiagonal():
	global board
	if board[0][0] == ' ':
		return False
	else:
		return board[0][0] == board[1][1] == board[2][2]

def isWinningBottomLeftDiagonal():
	global board
	if board[2][0] == ' ':
		return False
	else:
		return board[2][0] == board[1][1] == board[0][2]

def checkWinner():
	global board
	winner = {'row':-1, 'col':-1, 'diagonal':-1, 'marker':-1}
	for idx in range(3):
		if isWinningRow( idx ):
			winner['row'] = idx
			winner['marker'] = board[idx][0]
			return winner
		elif isWinningCol( idx ):
			winner['col'] = idx
			winner['marker'] = board[0][idx]
			return winner
	if isWinningTopLeftDiagonal():
		winner['diagonal'] = 'top'
		winner['marker'] = board[0][0]
		return winner
	elif isWinningBottomLeftDiagonal():
		winner['diagonal'] = 'bottom'
		winner['marker'] = board[2][0]
		return winner
	else:
		return winner

def isCatsGame():
	global board
	for row in board:
		for marker in row:
			if marker == ' ':
				return False
	else:
		return True



def isAlreadyTaken( row, col ):
	global board
	return board[row - 1][col - 1] != ' '

def getInput():
	row = raw_input("Please enter a row between 1 and 3, inclusive: ")
	while not isValidSelection(row):
		print("That is not a valid raw_input.")
		row = raw_input("Please enter a row between 1 and 3, inclusive: ")
	row = int(row)
	col = raw_input("Please enter a column between 1 and 3, inclusive: ")
	while not isValidSelection(col):
		print("That is not a valid raw_input.")
		col = raw_input("Please enter a column between 1 and 3, inclusive: ")
	col = int(col)
	if isAlreadyTaken( row, col ):
		print("Row {} column {} is already in use! Pick something different.".format(row,col))
		return getInput()
	else:
		return (row - 1, col - 1)


def placeMarker( row_col_tuple ):
	global board
	row = row_col_tuple[0]
	col = row_col_tuple[1]
	if player_one:
		board[row][col] = 'X'
	else:
		board[row][col] = 'O'

def showWinner( winner ):
	global board, player_one_score, player_two_score
	winningPlayer = 0
	if winner['row'] != -1:
		row = winner['row']
		if board[row][0] == 'X':
			winningPlayer = 1
		for idx in range(3):
			board[row][idx] = '-'
		printBoard()
	elif winner['col'] != -1:
		col = winner['col']
		if board[0][col] == 'X':
			winningPlayer = 1
		for idx in range(3):
			board[idx][col] = '|'
		printBoard()
	elif winner['diagonal'] == 'top':
		if board[0][0] == 'X':
			winningPlayer = 1
		for idx in range(3):
			board[idx][idx] = '\\'
		printBoard()
	else:
		# bottom left diagonal winner
		if board[2][0] == 'X':
			winningPlayer = 1
		board[2][0] = '/'
		board[1][1] = '/'
		board[0][2] = '/'
		printBoard()

	winningString = '\033[91m'
	if winningPlayer:
		player_one_score += 1
		winningString += "Player One wins!"
	else:
		player_two_score += 1
		winningString += "Player Two wins!"
	winningString += '\033[0m'
	print(winningString)

def reset():
	global player_one
	player_one = 1
	clearBoard()

def play():
	winner = checkWinner()
	while winner['marker'] == -1 and not isCatsGame():
		printBoard()
		if player_one:
			print("Player One's Turn!")
			placeMarker( getInput() )
		else:
			print("Player Two's Turn!")
			placeMarker( getInput() )
		winner = checkWinner()
		togglePlayer()
	else:
		if isCatsGame():
			print('\033[91m' + "No moves left . . . Cat's Game!" + '\033[0m')
		else:
			showWinner( winner )
	reset()


def explainGame():
	print("~ Welcome to Tic Tac Toe ~\n")
	print("Player One will use the marker 'X', Player Two will use 'O'\n")
	print("Let's get started!\n")

def endGame():
	global player_one_score, player_two_score
	formatting_begin = '\033[91m'
	formatting_end = '\033[0m'
	print(" ")
	print("{}Player One Score:{} {}".format(formatting_begin, formatting_end, player_one_score))
	print("{}Player Two Score:{} {}".format(formatting_begin, formatting_end, player_two_score))
	print("\nThanks so much for playing! See you next time!")

def main():
	explainGame()
	play()
	response = raw_input("Would you like to play again (y/n)? ")
	while response == 'y':
		play()
		response = raw_input("Would you like to play again (y/n)? ")
	endGame()



if __name__ == '__main__':
	main()




