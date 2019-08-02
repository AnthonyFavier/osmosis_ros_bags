import matplotlib.image as mpimg
import numpy as np

file=open("pose.txt","r")
data=""
nbligne=0
for l in file:
	data=data+l
	nbligne=nbligne+1
file.close()

LX=[]
LY=[]
data=data.replace('\n',',')
data=data.split(',')
del(data[3])
del(data[2])
del(data[1])
del(data[0])
nbligne=nbligne-1

for i in range(nbligne):
	LX.append(data[4*i+1])
	LY.append(data[4*i+2])

for i in range(len(LX)):
	"""Conversion from coordinate to pixels
	You will have to change those formulas if you change the image,
	as resolution might not be the same. We also used a little arbitrary shift
	to reach a better precision on the blagnac image"""
	LX[i]=int((float(LX[i])+80)*(828/160)*1.04)
for i in range(len(LY)):
	LY[i]=int((80-float(LY[i]))*(740/160)*1.15)

image=mpimg.imread("blagnac.jpg")

for i in range(len(LX)):
	for epx in range(2):
		for epy in range(2):
			bleu=int(len(LX)-i)/9
			vert=255-int(len(LX)-i)/9
			image[LY[i]+epy][LX[i]+epx]=(0,vert,bleu)
			image[LY[i]+epy][LX[i]-epx]=(0,vert,bleu)
			image[LY[i]-epy][LX[i]+epx]=(0,vert,bleu)
			image[LY[i]-epy][LX[i]-epx]=(0,vert,bleu)


xob1=int((float(50+80)*float((828/160))*1.04))
xob2=int((float(37.5+80)*float((828/160))*1.04))
yob1=int((80-float(10))*float((740/160))*1.15)
yob2=int((80-float(4))*float((740/160))*1.15)
exit()
for epx in range(3):
	for epy in range(3):
		image[yob1+epy][xob1+epx]=(255,0,0)
		image[yob1+epy][xob1-epx]=(255,0,0)
		image[yob1-epy][xob1+epx]=(255,0,0)
		image[yob1-epy][xob1-epx]=(255,0,0)

		image[yob2+epy][xob2+epx]=(255,0,0)
		image[yob2+epy][xob2-epx]=(255,0,0)
		image[yob2-epy][xob2+epx]=(255,0,0)
		image[yob2-epy][xob2-epx]=(255,0,0)

mpimg.imsave("chemin.png",image)
