def bt_permu(a,l,r):
    if l == r:
        print(a)
        return
    for i in range(l,r+1):
        a[i],a[l] = a[l], a[i]
        bt_permu(a,l+1,r)
        a[i],a[l] = a[l], a[i]


tstr = ['a','b','c']

bt_permu(tstr, 0,len(tstr)-1)