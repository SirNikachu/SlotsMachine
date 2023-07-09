import random

MAX_LINES = 3  # Maximum number of lines to bet on
MAX_BET = 100  # Maximum bet amount
MIN_BET = 1  # Minimum bet amount

ROWS = 3  # Number of rows in the slot machine
COLS = 3  # Number of columns in the slot machine

symbol_count = {
    "A": 2,  
    "B": 4,  
    "C": 6,  
    "D": 8   
}

symbol_value = {
    "A": 5, 
    "B": 4,  
    "C": 3,  
    "D": 2   
}

def check_winnings(columns, lines, bet, values):
    """
    Checks the winnings based on the provided columns, lines, bet, and symbol values.

    Arguments:
    - columns: A list of columns in the slot machine.
    - lines: The number of lines to bet on.
    - bet: The bet amount on each line.
    - values: A dictionary containing the values of different symbols.

    Returns:
    - winnings: The total winnings.
    - winning_lines: A list of line numbers on which the player won.
    """
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    """
    Generates a random spin of the slot machine.

    Arguments:
    - rows: The number of rows in the slot machine.
    - cols: The number of columns in the slot machine.
    - symbols: A dictionary containing the count of different symbols.

    Returns:
    - columns: A list of columns in the slot machine spin.
    """
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    """
    Prints the slot machine with the provided columns.

    Arguments:
    - columns: A list of columns in the slot machine.
    """
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


def deposit():
    """
    Asks the user for the deposit amount and returns it.

    Returns:
    - amount: The deposit amount.
    """
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount


def get_number_of_lines():
    """
    Asks the user for the number of lines to bet on and returns it.

    Returns:
    - lines: The number of lines to bet on.
    """
    while True:
        lines = input(
            "Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines


def get_bet():
    """
    Asks the user for the bet amount and returns it.

    Returns:
    - amount: The bet amount.
    """
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount


def spin(balance):
    """
    Performs a spin on the slot machine based on user inputs.

    Arguments:
    - balance: The current balance of the player.

    Returns:
    - balance_change: The change in balance after the spin.
    """
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet


def main():
    """
    Main function to run the slot machine game.
    """
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")


main()
