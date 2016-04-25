arr = [10,-3,2,20,3,-1]

def insert(data, d):
    if len(data)==0:
        data.append(d)
        return
    if d < data[-1]:
        t = data.pop()
        insert(data,d)
        data.append(t)
    else:
        data.append(d)
def getBottom(data,top):
    if len(data)==0:
        return top
    return getBottom(data,data.pop())


def sort_stack(data):
    if len(data) == 0:

        return
    d = data.pop()
    sort_stack(data)
    insert(data,d)
    return

sort_stack(arr)
print (arr)