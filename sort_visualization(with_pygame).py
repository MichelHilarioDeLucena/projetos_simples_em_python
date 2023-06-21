import copy
import random
import math 
import pygame as pg

w,h=400,800
temp=0
sroot=40
temp=0
size=sroot**2
array0=[i for i in range(size)]
scale:int=w/sroot

rect=pg.Rect(0,0,scale,scale)

pg.init()
win=pg.display.set_mode((w,h))
c_win=pg.Surface(size=(w,h))

win.fill('white')

pg.display.update()

def shuffle():
    temp=0
    for i in range(len(array0)):
        r_i=random.randint(0,len(array0)-1)
        temp=array0[r_i]
        array0[r_i]=array0[i]
        array0[i]=temp

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

def quickSort(array, low, high):    
    draw_matrix(yo=sroot*scale)
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)



def draw_matrix(xo=0,yo=0):
    for x in range(sroot):
        for y in range(sroot):
            c=pg.Color(150,int((array0[x*sroot+y])*255/sroot/sroot/4),int((array0[y*sroot+x])*255/sroot/sroot/2))
            rect.x,rect.y=xo+x*scale,yo+y*scale
            pg.draw.rect(win,c,rect)
    pg.display.update()
    
    
shuffle()
draw_matrix()
quickSort(array0,0,len(array0)-1)

def run():
    while True:
        for event in pg.event.get():
            if event.type==pg.QUIT:
                pg.quit()
                return
        
        
run()