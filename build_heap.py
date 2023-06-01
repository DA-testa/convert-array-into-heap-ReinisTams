# python3

def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(n // 2 - 1, -1, -1):
        sift_down(data, i, n, swaps)

    return swaps


def sift_down(data, i, n, swaps):
    index = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and data[left] < data[index]:
        index = left
    if right < n and data[right] < data[index]:
        index = right
    if i != index:
        data[i], data[index] = data[index], data[i]
        swaps.append((i, index))
        sift_down(data, index, n, swaps)


def main():
    choice = input("Enter 'I' for interactive input or 'F' for file input: ")
    if choice == "I":
        n = int(input("Enter the number of elements: "))
        data = list(map(int, input("Enter the elements separated by spaces: ").split()))
        assert len(data) == n
    elif choice == "F":
        file_path = input("Enter the file path: ")
        with open(file_path, 'r') as file:
            n = int(file.readline())
            data = list(map(int, file.readline().split()))
            assert len(data) == n
    else:
        print("Invalid input. Please enter 'I' or 'F'.")
        return

    swaps = build_heap(data)
    assert len(swaps) <= 4 * n
    print("Number of swaps:", len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()

