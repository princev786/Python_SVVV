#second largest and third smallest logic
import math
lst = eval(input("Enter a list"))

max,smax=lst[0],lst[0]
min,smin,tmin =math.inf,math.inf,math.inf
for i in lst:
    if i>max:
        smax = max
        max = i
    else:
        if i>smax:
            smax = i

    if i<min:
        tmin = smin
        smin = min
        min = i
    elif i<smin:
        tmin = smin
        smin = i
    elif i<tmin:
        tmin =i 
print(smax,tmin)