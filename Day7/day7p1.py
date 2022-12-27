def main():
    input_array = []

    with open('input.txt', 'r', encoding="UTF-8") as file_name:
        input_array = file_name.readlines()

    file_tree = build_tree(input_array)

    print(file_tree.node_size)


def build_tree(command_array):
    tree = Node("/", "dir", None, 0)

    return tree


class Node:
    node_name = ""
    node_type = ""
    node_data = []
    node_size = 0

    def __init__(self, name, node_type, data, size):
        Node.node_name = name
        Node.node_type = node_type
        Node.node_data = data
        Node.node_size = size


if __name__ == "__main__":
    main()
