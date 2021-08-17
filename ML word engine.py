# ML word engine
listofwords = ['','']
while True:
    inp = input(' > ')
    entry = ''
    entrynum = 0
    
    try:
        while True:
            entry = listofwords[entrynum]
            if inp in entry:
                print('entry')

    except:
        blank = ''
        