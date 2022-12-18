def main():
    input_array = []

    with open('input.txt', 'r', encoding="UTF-8") as file_name:
        input_array = file_name.readlines()

    instruction_start_index, box_array = read_in_boxes(input_array)

    for i in range(instruction_start_index, (len(input_array))):
        box_array = follow_instruction(box_array, input_array[i])

    for n in box_array:
        print(n[-1].strip('[').strip(']'), end="")
    print()


def follow_instruction(box_array, instruction):
    instruction_array = instruction.split()

    count = int(instruction_array[1])
    from_index = int(instruction_array[3]) - 1
    to_index = int(instruction_array[5]) - 1

    box_array = move_boxes(box_array, count, from_index, to_index)

    return box_array


def move_boxes(box_array, count, from_index, to_index):
    boxes = []
    for _ in range(count):
        boxes.insert(0, box_array[from_index].pop())
    for n in boxes:
        box_array[to_index].append(n)
    return box_array


def read_in_boxes(input_array):
    move_index = 0
    boxes = []
    box_pile_count = int(len(input_array[0])/4)
    for _ in range(box_pile_count):
        boxes.append([])

    for i in range(len(input_array)):
        if input_array[i][1] == "1":
            move_index = i + 2
            break
        row = input_array[i].replace("    ", " [0]").split()

        for j in range(box_pile_count):
            if row[j] != "[0]":
                (boxes[j]).insert(0, row[j])

    return move_index, boxes


if __name__ == "__main__":
    main()
