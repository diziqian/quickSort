def quickSort(Arr, L, R):
    if L > R:
        return

    # Pos = (int)((L+R) / 2)
    Pos = L
    KV = Arr[Pos]
    i = L
    j = R

    while i < j:
        while Arr[j] >= KV and i < j:
            j -= 1

        Arr[i] = Arr[j]

        while Arr[i] <= KV and i < j:
            i += 1

        Arr[j] = Arr[i]
        # if i < j:
        #     tmp = Arr[j]
        #     Arr[j] = Arr[i]
        #     Arr[i] = tmp
        #     i += 1
        #     j -= 1

    Arr[i] = KV
    quickSort(Arr, L, i-1)
    quickSort(Arr, i+1, R)

if __name__ == "__main__":
    Arr = [1, -1, 7, 7, 10, 3, 6, 8, 11, 4, 5]
    quickSort(Arr, 0, len(Arr)-1)

    print("Arr",)
    print(Arr)