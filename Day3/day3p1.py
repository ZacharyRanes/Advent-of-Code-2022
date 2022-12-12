def main():
    input_array = []

    with open('input.txt', 'r', encoding="UTF-8") as file_name:
        input_array = file_name.readlines()

    priorities_sum = 0

    for n in input_array:
        length = len(n.strip())
        s1 = slice(0, length//2)
        s2 = slice(length//2, length)
        compartment1 = n.strip()[s1]
        compartment2 = n.strip()[s2]
        like_type = list(set(compartment1) & set(compartment2))

        # print(like_type[0])
        if (like_type[0].isupper()):
            # print(ord(like_type[0])-38)
            priorities_sum += (ord(like_type[0])-38)
        else:
            # print(ord(like_type[0])-96)
            priorities_sum += (ord(like_type[0])-96)

    print(priorities_sum)


if __name__ == "__main__":
    main()
