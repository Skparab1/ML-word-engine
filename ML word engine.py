# ML word engine
listofwords = ['a','abandon','ability',]
while True:
    inp = input(' > ')
    entry = ''
    entrynum = 0
    
    try:
        while True:
            entry = listofwords[entrynum]
            if inp in entry: #finds if one letter is missing at beginning or end
                print(entry)

            if inp[:4] == entry[:4]:
                print(entry)

            i = 1
            try:
                while True:
                    if inp[i:] == entry[i+1:] and inp[:i-1] == entry[i-1]:
                        print(entry)
                    i += 1
            except:
                blank = ''
            
            entrynum += 1

    except:
        blank = ''
        