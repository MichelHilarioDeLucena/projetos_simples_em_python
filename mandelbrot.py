import tkinter
from math import *

import pygame

w,h,=600,900
root = tkinter.Tk()
root.geometry(f'{w}x{h}')
canvas=tkinter.Canvas(root)
canvas.pack(fill='both',expand=True)
counter=1000
color_c=255
half_w=w/2
third_h=h/3
def rgb_to_hex(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'

def mapC(n,start1,stop1,start2,stop2):
    return  (n - start1) / (stop1 - start1) * (stop2 - start2) + start2 
    
n=20
escape_v=20
for x in range(w):
    for y in range(h):
        a=mapC(y-100,0,w,-2,2)
        b=mapC(x+half_w,0,h,-2,1)
        c=0
        la,lb=a,b
        while c<n:
            ka=a**2-b**2
            kb=2*a*b+lb
            a=ka+la
            b=kb+lb
            if (a**2+b**2>32):break
            c+=1
        r,g,b=0,0,0
        if c!=n:
            r=int(abs(cos(c*2))*color_c)        
            g=int(abs(cos(c))*color_c)
            b=int(abs(sin(c))*color_c)
        canvas.create_rectangle(x,y,x+1,y+1,fill=rgb_to_hex(r,g,b),outline='')
canvas.update()
canvas.mainloop()