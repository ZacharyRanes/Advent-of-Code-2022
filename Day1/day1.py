def main():
    input_array = []
    elf_cal_count = []

    with open('input.txt', 'r', encoding="UTF-8") as file_name:
        input_array = file_name.readlines()

    # build an array of arrays each sub array is an elf
    elf_cal_count.append([])
    elf_index = 0
    for n in input_array:
        if n == '\n':
            elf_index += 1
            elf_cal_count.append([])
        else:
            elf_cal_count[elf_index].append(int(n.strip()))

    max_cal1 = 0
    max_cal2 = 0
    max_cal3 = 0

    for n in elf_cal_count:
        s = sum(n)
        if s > max_cal1:
            max_cal3, max_cal2 = max_cal2, max_cal1
            max_cal1 = s
        elif s > max_cal2:
            max_cal3 = max_cal2
            max_cal2 = s
        elif s > max_cal3:
            max_cal3 = s

    print("1st {}".format(max_cal1))
    print("2st {}".format(max_cal2))
    print("3st {}".format(max_cal3))

    print("sum {}".format((max_cal3 + max_cal1 + max_cal2)))


if __name__ == "__main__":
    main()
