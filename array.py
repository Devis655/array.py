def max_Product(arr):
    arr_len = len(arr)
    if (arr_len < 2):
        print("No pairs exist")
        return

    # Initialize maximum product pair
    a = arr[0]
    b = arr[1]

    # Traverse through every possible pair
    for i in range(0, arr_len):
        for j in range(i + 1, arr_len):
            if (arr[i] * arr[j] > a * b):
                a = arr[i]
                b = arr[j]

    return a, b


nums = [2, 6, 8, 9, 12, 16, 1, 4]
print("Original array:", nums)
print("Maximum product pair is:", max_Product(nums))

nums = [-1, -4, -3, -6, 0, -8, -5, -2]
print("Original array:", nums)
print("Maximum product pair is:", max_Product(nums))
