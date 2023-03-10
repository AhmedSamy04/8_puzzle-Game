
def function1(puzzle):                    # returns the possible actions in the current state of the puzzle
    actions = []
    empty_index = puzzle.index(0)         # to find the index of the empty tile (represented by the number 0)
    if (empty_index // 3) > 0:            # check if the index > 2 then up move is available
        actions.append('^')
    if (empty_index // 3) < 2:            # check if the index < 6 then down move is available
        actions.append('v')
    if (empty_index % 3) > 0:             # check if the index not equal (0,3,6) then left move is available
        actions.append('<')
    if (empty_index % 3) < 2:             # check if the index not equal (2,5,8) then right move is available
        actions.append('>')
    return actions



def function2(puzzle, selected_move):    # apply the action to the current state and returns the new state of the puzzle
    new_puzzle = puzzle[:]
    empty_index = new_puzzle.index(0)    # to find the index of the empty tile (represented by the number 0)
    if selected_move == '^':             # Swap
        new_puzzle[empty_index], new_puzzle[empty_index - 3] = new_puzzle[empty_index - 3], new_puzzle[empty_index]
    if selected_move == 'v':
        new_puzzle[empty_index], new_puzzle[empty_index + 3] = new_puzzle[empty_index + 3], new_puzzle[empty_index]
    if selected_move == '<':
        new_puzzle[empty_index], new_puzzle[empty_index - 1] = new_puzzle[empty_index - 1], new_puzzle[empty_index]
    if selected_move == '>':
        new_puzzle[empty_index], new_puzzle[empty_index + 1] = new_puzzle[empty_index + 1], new_puzzle[empty_index]
    return new_puzzle



def function3(puzzle):              # returns True only if the state of the puzzle satisfy the goal condition
    for i in range(len(puzzle)):
        if i != puzzle[i]:
            return False
        return True
    pass
