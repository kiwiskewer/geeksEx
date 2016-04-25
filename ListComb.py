def listComb1(str):
    for n in range(1,1<<len(str)):
        s = ''
        i = 0
        while n:
            if n & 1:
                s += str[i]
            i += 1
            n >>= 1
        print (s)

tests = 'abc'

#listComb1(tests)

def listComb2(comb, str, l, r):

    for i in range(l,r+1):
        comb += str[i]
        print(comb)
        listComb2(comb, str, i+1, r)
        comb = comb[:-1]

sol = ''
listComb2(sol, tests, 0, len(tests)-1)