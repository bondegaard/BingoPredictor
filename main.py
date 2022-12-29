import random


import user_input
from Board import Board


found_index:int = 0

def simulate(board_amount:int):
    global found_index
    # Fill boards
    boards = []
    for i in range(board_amount):
        boards.append(Board(i))

    picked_numbers:list = random.sample(range(1, 100), 99)

    amount_of_numbers:int = 0
    won = False
    while len(picked_numbers) > 0:
        amount_of_numbers+=1

        number:int = picked_numbers[0]
        picked_numbers.pop(0)
        for board in boards:
            while number in board.board: board.board.remove(number)
            if len(board.board) <= 0:
                if not won:
                    won = True
                    found_index+=amount_of_numbers
                boards.remove(board)



def main():
    """Start of program...!"""

    try:
        # Get basic information for the simulation
        i: int = user_input.get_int_positiv("Please enter the amount of trials to run: ")
        boards: int = user_input.get_int_positiv("Please enter the amount of boards in each trial: ")

    except:
        return
    run(i, boards) # Start the simulation

def run(epochs: int, boards:int):
    """Run the simulation a set amount of times"""


    # Run each Simulation
    for i in range(1, epochs+1):
        # % Program Finished
        print(str(i) + " | " + "{:.2f}".format((i/epochs)*100) + "%")
        # Run one simulation (Saves output globally)
        simulate(boards)
    print("{:.2f}".format((found_index/epochs)))

    # Display data for all the simulations
 #   display_DataFrame()


if __name__ == '__main__':
    main()
