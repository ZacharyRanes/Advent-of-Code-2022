def main():
    input_array = []

    with open('input.txt', 'r', encoding="UTF-8") as file_name:
        input_array = file_name.readlines()

    your_score = 0

    game_strat = {
        "AX": 3,
        "AY": 1,
        "AZ": 2,
        "BX": 1,
        "BY": 2,
        "BZ": 3,
        "CX": 2,
        "CY": 3,
        "CZ": 1
    }

    for n in input_array:
        opponent_choose = n.strip()[0]
        your_strat = n.strip()[-1]

        if your_strat == "X":  # loose
            your_score += 0
        if your_strat == "Y":  # draw
            your_score += 3
        if your_strat == "Z":  # win
            your_score += 6

        your_score += game_strat[opponent_choose+your_strat]

    print(your_score)


if __name__ == "__main__":
    main()
