def main():
    input_array = []

    with open('input.txt', 'r', encoding="UTF-8") as file_name:
        input_array = file_name.readlines()

    your_score = 0

    game_scoring = {
        "AX": 3,
        "AY": 6,
        "AZ": 0,
        "BX": 0,
        "BY": 3,
        "BZ": 6,
        "CX": 6,
        "CY": 0,
        "CZ": 3
    }

    for n in input_array:
        opponent_choose = n.strip()[0]
        your_choose = n.strip()[-1]

        if your_choose == "X":
            your_score += 1
        if your_choose == "Y":
            your_score += 2
        if your_choose == "Z":
            your_score += 3

        your_score += game_scoring[opponent_choose+your_choose]

    print(your_score)


if __name__ == "__main__":
    main()
