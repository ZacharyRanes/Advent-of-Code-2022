def main():
    input_array = []

    with open('input.txt', 'r', encoding="UTF-8") as file_name:
        input_array = file_name.readlines()

    priorities_sum = 0

    for i in range(0, len(input_array), 3):
        like_type = list(set(input_array[i].strip()) & set(
            input_array[i+1].strip()) & set(input_array[i+2].strip()))

        print(like_type[0])
        if (like_type[0].isupper()):
            # print(ord(like_type[0])-38)
            priorities_sum += (ord(like_type[0])-38)
        else:
            # print(ord(like_type[0])-96)
            priorities_sum += (ord(like_type[0])-96)

    print(priorities_sum)


if __name__ == "__main__":
    main()
