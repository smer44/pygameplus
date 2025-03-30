import math
import pprint as pp

size = 8;
arr = [[0 for _ in range(size)] for _ in range(size)]

arr_out = [[0 for _ in range(size)] for _ in range(size)]

for i in range(4):
    for j in range(4):
        arr[j+2][i+2] = i+1+j*4



root2 = 1.414/2
a = 60
sin_22_5= math.sin(math.radians(a)) #0.38268
cos_22_5 =math.cos(math.radians(a))# 0.923879

def minmax(v,a,b):
    return max(a,min(b,v))

def rotate_45_pixelart(arr,arr_out):
    for j in range(8):
        for i in range(8):
            cell = arr[j][i]
            if cell:
                ii,jj = i - 3.5, j-3.5
                ii,jj = ii*cos_22_5 + jj*sin_22_5 + 3.5, -ii*sin_22_5 + jj * cos_22_5 + 3.5
                ii,jj = minmax(round(ii),0,7), minmax(round(jj),0,7),
                #now simple put:
                arr_out[jj][ii] = cell

rotate_45_pixelart(arr,arr_out)

pp.pprint(arr)
pp.pprint(arr_out)