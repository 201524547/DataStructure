import sys
def Merge(a, b):
    result = []
    while len(a) > 0 or len(b) > 0:

        if len(a) > 0 and len(b) > 0:
            if a[0] > b[0]:
                result.append(a[0])
                a = a[1:]
            else:
                result.append(b[0])
                b = b[1:]

        elif len(a) > 0:
            result.append(a[0])
            a = a[1:]

        elif len(b) > 0:
            result.append(b[0])
            b = b[1:]

    return result

def MergeSort(list):

    if len(list) <= 1:
        return list

    mid = len(list) // 2

    right = list[mid:]
    left = list[:mid]

    right = MergeSort(right)
    left = MergeSort(left)

    return Merge(left, right)

if __name__=="__main__":
    n = int(sys.stdin.readline())
    a = []

    while n > 0:
        a.append(n%10)
        n = n // 10

    a = MergeSort(a)

    i = 0
    k = 0

    while a:
        k = k*10
        k += a[0]
        a = a[1:]

    print(k)