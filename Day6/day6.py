def main():
    input_array = []

    with open('input.txt', 'r', encoding="UTF-8") as file_name:
        input_array = file_name.readlines()

    data_stream = input_array[0]
    # data_slice_size = 4  # Part1
    data_slice_size = 14

    for i in range(data_slice_size, len(data_stream)):
        data_slice = data_stream[i-data_slice_size:i]
        if len(set([*data_slice])) == data_slice_size:
            print(data_slice)
            return i


if __name__ == "__main__":
    print(main())
