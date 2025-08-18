def merge(arr1, arr2):
    import math
    
    m, n = len(arr1), len(arr2)
    total = m + n
    gap = math.ceil(total / 2)

    while gap > 0:
        i, j = 0, gap
        while j < total:
            # Case 1: both in arr1
            if i < m and j < m:
                if arr1[i] > arr1[j]:
                    arr1[i], arr1[j] = arr1[j], arr1[i]

            # Case 2: i in arr1, j in arr2
            elif i < m and j >= m:
                if arr1[i] > arr2[j - m]:
                    arr1[i], arr2[j - m] = arr2[j - m], arr1[i]

            # Case 3: both in arr2
            else:
                if arr2[i - m] > arr2[j - m]:
                    arr2[i - m], arr2[j - m] = arr2[j - m], arr2[i - m]

            i += 1
            j += 1

        # Reduce gap
        if gap == 1:
            gap = 0
        else:
            gap = math.ceil(gap / 2)

