def binary_search(myl, token):
    found = False
    left = 0
    right = len(myl)-1
    while left <= right and not found:
        mid = (right+left)//2
        if myl[mid] == token:
            found = True

        if myl[mid] > token:
            right = mid - 1
        else:
            left = mid + 1
    return found

myl = [5,4.3,0,29,4.2]
token = 0

print(binary_search(myl, token))
