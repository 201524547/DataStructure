import sys

def qsort(arr):
    if len(arr) <= 1:
        return arr

    left_arr = []
    right_arr = []
    equal_arr = []

    pivot = arr[0]

    for num in arr:
        if num < pivot:
            left_arr.append(num)
        elif num > pivot:
            right_arr.append(num)
        else:
            equal_arr.append(num)

    return qsort(right_arr) + equal_arr + qsort(left_arr)


if __name__=="__main__":
    n = int(sys.stdin.readline())
    a = []

    while n > 0:
        a.append(n%10)
        n = n // 10

    a = qsort(a)

    k = 0

    while a:
        k = k*10
        k += a[0]
        a = a[1:]

    print(k)