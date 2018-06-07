def transcode(s):
    k=[]
    for i in s:
        if i=='.':
            k.append('0')
        elif i=='-':
            k.append('1')
        elif i=='#':
            k.append('#')
        else:
            return -1
    return k

def transbin(m):
    total=[]
    i=0
    while i<len(m):
       while i

kk=transcode('..--..--..##..')
print(transbin(kk))
