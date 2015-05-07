from plotting import plot
from image import file2image
from image import color2gray
from math import pi, e

S = {2 + 2j, 3 + 2j, 1.75 + 1j, 2 + 1j, 2.25 + 1j, 2.5 + 1j, 2.75 + 1j, 3 + 1j, 3.25 + 1j}

# task 1.4.1
#plot(S, scale=5, hpath='htmls/task141.html')

#task 1.4.3
#plot({1+2j+z for z in S}, scale=5, hpath='htmls/task143.html', plot='plot - translation')

#task 1.4.7
#plot({z/2 for z in S}, scale=5, hpath='htmls/task147.html', title='plot - scaled by 1/2')

#task 1.4.8
#plot({z*0.5j for z in S}, scale=5, hpath='htmls/task148.html', title='plot - rotated by 90 degree and scaled by 1/2')

#task 1.4.9
#plot({z*0.5j+2-1j for z in S}, scale=5, dot_size=2, hpath='htmls/task149.html', title='plot - rotate scale and shift')



data = list(reversed(file2image('img01.png')))
#print(len(data))
data = color2gray(data)
width = len(data[0])
height = len(data)
print(width, height)
pts =[complex(x,y) for y in range(len(data)) for x in range(len(data[y])) if data[y][x] < 120]
#print(pts)


#task 1.4.10
#plot(pts, scale=len(data), dot_size=2, hpath='htmls/task1410.html', title='image filter')


#task 1.4.11

#task 1.4.12
#plot({z*0.5j for z in pts}, scale=len(data), dot_size=2, hpath='htmls/task1412.html', title='plot - rotated by 90 degree and scaled by 1/2')

#task 1.4.17
n = 20
w = e**(2j*pi/n)
l = [w**i for i in range(n)]
#plot(l, dot_size=2,hpath='htmls/task1417.html', title='Euler')

#task 1.4.18
rotated = {z*e**(1j*pi/4) for z in S}
#plot(rotated, dot_size=2,hpath='htmls/task1418.html', title='Euler Rotate')

#task 1.4.19
rotated = {z*e**(1j*pi/4) for z in pts}
#plot(rotated, scale=len(data), dot_size=2,hpath='htmls/task1419.html', title='Euler Rotate')

#task 1.4.20
rotated = {(z-(width/2+1j*height/2))*(e**(1j*pi/4))*0.5 for z in pts}
plot(rotated, scale=len(data), dot_size=2,hpath='htmls/task1420.html', title='Euler Rotate')