

def searching_element(len_array, element, array):
    left = 0
    right = len_array
    while left < right:
        middle = (left + right) // 2
        if array[middle] == element:
            return middle
        elif array[left] <= array[middle]:
            if array[middle] > element >= array[left]:
                right = middle
            else:
                left = middle + 1
        else:
            if array[middle] < element <= array[right - 1]:
                left = middle + 1
            else:
                right = middle - 1
    return -1


if __name__ == '__main__':
    len_array = int(input())
    element = int(input())
    array = list(map(int, input().split(' ')))
    print(searching_element(len_array, element, array))

# Код посылки 43455783