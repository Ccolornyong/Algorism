def solution(arr, queries):
    for i,j in queries:
        swap = arr[i]
        arr[i] = arr[j]
        arr[j] = swap
    return arr