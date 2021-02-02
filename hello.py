import math
def dhd(x,y) :
    if y>0 and x>0 :
        return x,y
    elif y<0 and x>0 :
        return x
    elif y>0 and x<0 :
        return y
    elif y<0 and x<0 :
        return 'none'
x = int(input('number x'))
y = int(input('number y'))
print(dhd(x,y))
