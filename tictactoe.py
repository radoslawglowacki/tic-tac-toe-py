ACTUAL_MARK = "X"
IS_RUNNING = True


def get_user_coordinates():
    while True:
        allowed_letters = "abc"
        allowed_numbers = "123"
        letter_coordinate = ""
        number_coordinate = ""
        result_user_coordinates = []
        user_inputs = [(input("Enter first coordinate: ")).lower(), input("Enter second coordinate: ")]

        for item in user_inputs:
            if item in allowed_letters:
                letter_coordinate = item
            elif item in allowed_numbers:
                number_coordinate = item

        for i in range(len(list(allowed_letters))):
            if list(allowed_letters)[i] == letter_coordinate.lower():
                result_user_coordinates.append(i)
        for i in range(len(list(allowed_numbers))):
            if list(allowed_numbers)[i] == number_coordinate:
                result_user_coordinates.append(i)

        if len(result_user_coordinates) == 2:
            return result_user_coordinates
        else:
            print("\n")
            print("Please enter correct coordinates!")
            print("\n")


def generate_board():
    return [[".", ".", "."], [".", ".", "."], [".", ".", "."]]


def check_if_won(game_table):
    for i in range(0, 3):
        resultX = 0
        resultY = 0
        for j in range(0, 3):
            if game_table[j][i] == "X":
                resultX += 1
            elif game_table[j][i] == "O":
                resultY += 1
        if resultX == 3:
            print("Player X Wins!")
            return False
        elif resultY == 3:
            print("Player Y Wins!")
            return False

    if game_table[0][0] == "X" and game_table[1][1] == "X" and game_table[2][2] == "X":
        print("Player X Wins!")
        return False
    elif game_table[0][0] == "O" and game_table[1][1] == "O" and game_table[2][2] == "O":
        print("Player O Wins!")
        return False
    elif game_table[2][0] == "O" and game_table[1][1] == "O" and game_table[0][2] == "O":
        print("Player O Wins!")
        return False
    elif game_table[2][0] == "X" and game_table[1][1] == "X" and game_table[0][2] == "X":
        print("Player X Wins!")
        return False
    else:
        return True


def write_mark(game_table, actual_player_mark, user_coordinates):
    row = user_coordinates[0]
    col = user_coordinates[1]
    if game_table[row][col] == ".":
        game_table[row][col] = actual_player_mark
        if actual_player_mark == "X":
            actual_player_mark = "O"
        else:
            actual_player_mark = "X"
        return actual_player_mark
    else:
        print("This place is taken, enter your choose again!")
        return actual_player_mark


def main(is_running, actual_player_mark):
    game_table = generate_board()
    while is_running:
        print("  1   2   3")
        print("A " + game_table[0][0] + " | " + game_table[0][1] + " | " + game_table[0][2])
        print("  - - - - -")
        print("B " + game_table[1][0] + " | " + game_table[1][1] + " | " + game_table[1][2])
        print("  - - - - -")
        print("C " + game_table[2][0] + " | " + game_table[2][1] + " | " + game_table[2][2])

        user_coordinates = get_user_coordinates()
        actual_player_mark = write_mark(game_table, actual_player_mark, user_coordinates)
        is_running = check_if_won(game_table)
        if not is_running:
            print("""
            
Thank you for playing this game!

Good bye !""")


main(IS_RUNNING, ACTUAL_MARK)
