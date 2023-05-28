# python3


def convert_to_heap(n, a):
    swaps = []

    def sift_down(i):
        min_index = i
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        if left_child < n and a[left_child] < a[min_index]:
            min_index = left_child

        if right_child < n and a[right_child] < a[min_index]:
            min_index = right_child

        if i != min_index:
            a[i], a[min_index] = a[min_index], a[i]
            swaps.append((i, min_index))
            sift_down(min_index)

    for i in range(n // 2 - 1, -1, -1):
        sift_down(i)

    return swaps


# Read input
n = int(input())
a = list(map(int, input().split()))

# Convert array to heap
swaps = convert_to_heap(n, a)

# Print the number of swaps
print(len(swaps))

# Print the swap operations
for swap in swaps:
    print(swap[0], swap[1])
