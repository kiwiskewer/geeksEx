def listComb(str):
    for n in range(1,1<<len(str)):
        s = ''
        i = 0
        while n:
            if n & 1:
                s += str[i]
            i += 1
            n >>= 1
        print (s)

tests = 'abcde'

listComb(tests)

