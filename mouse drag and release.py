elif e.type == p.MOUSEBUTTONDOWN:
    location = p.mouse.get_pos() #(x, y)
    column = location[0]//SQUARE_SIZE
    row = location[1]//SQUARE_SIZE
                
if squareSelected == (row, column):
                        squareSelected = () # deselect
                        playerClicks = [] # clears the player clicks
                    else:
                        squareSelected = (row, column)
                        playerClicks.append(squareSelected)
                if e.type == p.MOUSEBUTTONUP: # after second click
                    # first click signfies the piece that'll be moved, the second click is its destination.
                    location = p.mouse.get_pos()
                    column = location [0]//SQUARE_SIZE
                    row = location [1]//SQUARE_SIZE
                    move = ChessEngine.Move(playerClicks[0], , gs.board) 
                    print(move.getChessNotation()) # printsthe moves
                    gs.makeMove(move) # making the move
                    squareSelected = () # resets user clicks
                    playerClicks = []