def selectsort(L):
    for slot in range(len(L)-1, 0, -1):
        positionOfMax = 0
        for location in range(1, slot+1):
            if L[location] > L[positionOfMax]:
                positionOfMax = location
                temp = L[slot]
                L[slot] = L[positionOfMax]
                L[positionOfMax] = temp
                return(L)

print(selectsort(2, 3))

                
