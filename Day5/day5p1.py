def main():
    input_array = []

    with open('input.txt', 'r', encoding="UTF-8") as file_name:
        input_array = file_name.readlines()

    move_index = 0
    boxes = []

    for i in range(len(input_array)):
        if input_array[i][1] == "1":
            move_index = i + 2
            break
        row = input_array[i].replace("    ", " [0]").split()
    #     print(row)
    # print(move_index)


if __name__ == "__main__":
    main()
