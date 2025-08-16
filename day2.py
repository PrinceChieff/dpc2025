def find_missing(arr, n):
    return n*(n+1)//2 - sum(arr)

# Example
arr = [1, 2, 4, 5]
n = len(arr) + 1
print(find_missing(arr, n))  # Output: 3
