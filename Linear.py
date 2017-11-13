def linear_search(myl, token):
    found = False
    for number in myl:
        if number == token:
            found = True
            break
    return found



myl = [1, 18, 42, 62, 33 -92]
token = 62
print(linear_search(myl, token))
    
