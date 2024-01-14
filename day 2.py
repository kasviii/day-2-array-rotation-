def rotate_left(arr, steps):
    n = len(arr)
    steps = steps % n  # Handle cases where steps are greater than array length
    return arr[steps:] + arr[:steps]

def rotate_right(arr, steps):
    n = len(arr)
    steps = steps % n  # Handle cases where steps are greater than array length
    return arr[-steps:] + arr[:-steps]

if __name__ == "__main__":
    # Example usage:
    input_array = [1, 2, 3, 4, 5]
    steps_to_rotate = 2

    rotated_left = rotate_left(input_array, steps_to_rotate)
    rotated_right = rotate_right(input_array, steps_to_rotate)

    print("Original array:", input_array)
    print("Array rotated to the left:", rotated_left)
    print("Array rotated to the right:", rotated_right)
