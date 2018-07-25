def amChecker(lst):
    for l in lst:
        if((ord(l[0]) > 64) & (ord(l[0]) < 78)):
            print(ord(l[0]))
            print(l)
