'''
 @param mas
 @return 1(bytes) | 2(bytes)
'''
def find_last_bit(mas):
    if mas[-1]==0:
        return 2
    len_mas = len(mas)
    temp = []
    for i in reversed(range(len_mas)):
        if mas[i]!=0:
            temp.append(mas[i])
        else:
            if mas[i-1]==1:
                temp.append(mas[i])
                break
            else:
                temp.append(mas[i])
    res = 0
    kol_bit=0
    for i in reversed(temp):
        if i==1:
            if kol_bit==1:
                res = 2
            else:
                res = 1
                kol_bit = 0
        else:
            if kol_bit > 1:
                kol_bit = 1
            else:
                kol_bit +=1
    return res

print(find_last_bit([0,1,1,1,0,0,0,0,0,0,0,0,0,0,0]))
