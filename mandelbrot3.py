from math import *
import threading
import sys
import pygame as pg

w,h,=600,900
qh=h*2/5
pg.init()
canvas=pg.display.set_mode((w,h))
alive=True
color_c=255
half_w=w/4
n=50

pix_a=pg.PixelArray(canvas)


def rgb_to_hex(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'
def mapC(n,start1,stop1,start2,stop2):
    return  (n - start1) / (stop1 - start1) * (stop2 - start2) + start2 
for x in range(w):
    for y in range(h):
        a=mapC(y-qh,0,w,-1.5,1.5)
        b=mapC(x+half_w,0,h,-1.5,1.5)
        c=0
        la,lb=a,b
        while c<n:
            ka=a*a-b*b
            kb=2*a*b
            a=ka+la
            b=kb+lb
            if (a**2+b**2>4):break
            c+=1
        r,g,b=0,0,0
        if c!=n:
            r=int(abs(cos(c*2))*color_c)        
            g=int(abs(cos(c))*color_c)
            b=int(abs(sin(c))*color_c)
        pix_a[x,y]=(r,g,b)
pix_a.close()
pg.display.update()

while alive:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            alive=False
pg.quit()


