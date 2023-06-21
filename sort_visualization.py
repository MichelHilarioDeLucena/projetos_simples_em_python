import tkinter
import random

h,w=800,400
temp=0
sroot=20
size=sroot**2
count=0
array0=[i for i in range(size)]
scale=w/sroot
count=0

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
    
    draw_matrix(yo=scale*sroot)
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

root = tkinter.Tk()
root.geometry(f'{w}x{h}')
canvas=tkinter.Canvas(root)
canvas.pack(expand=True,fill='both')

def fixed_draw(xo=0,yo=0):
        
    for i in range(size):
        x,y=int(i/sroot)*scale,i%sroot*scale
        color=hex(int(array0[i]*2048/size))[2:].zfill(3)        
        canvas.create_rectangle(x+xo,y+yo,x+scale+xo,y+scale+yo,fill=f'#{color}000555',outline='')
    canvas.update()

def draw_matrix(xo=0,yo=0):    
    rects=[]    
    for i in range(size):
        x,y=int(i/sroot)*scale,i%sroot*scale
        color=hex(int(array0[i]*2048/size))[2:].zfill(3)        
        rects.append(canvas.create_rectangle(x+xo,y+yo,x+scale+xo,y+scale+yo,fill=f'#{color}000555',outline=''))
    canvas.update()
    for item in rects:canvas.delete(item)
     
shuffle()
fixed_draw()
canvas.update()
quickSort(array0,0,len(array0)-1)
fixed_draw(yo=scale*sroot)

print('end')
root.mainloop()