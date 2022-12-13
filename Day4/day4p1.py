def main():
    input_array = []

    with open('input.txt', 'r', encoding="UTF-8") as file_name:
        input_array = file_name.readlines()

    pair_array = []

    # converted the text lines into array for easier use
    for n in input_array:
        # replace is used so split can break the line into four with one pass
        pair_array.append(n.strip().replace("-", ",").split(','))

    subsets = 0

    # [ 0, 1, 2, 3]
    # [L1,R1,L2,R2]

    for n in pair_array:
        if ((int(n[0]) >= int(n[2])) and (int(n[1]) <= int(n[3]))):
            subsets += 1
        elif ((int(n[2]) >= int(n[0])) and (int(n[3]) <= int(n[1]))):
            subsets += 1

    print(subsets)


if __name__ == "__main__":
    main()
