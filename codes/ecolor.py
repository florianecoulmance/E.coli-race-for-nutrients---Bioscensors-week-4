#!usr/bin/python3
# -*- coding: utf-8 -*-

# we import all librairies needed: matplotlib for graphs, numpy to calculate
import matplotlib.pyplot as plt
import numpy as np
import pylab as pl



def lecture(fichier):#we open the file containing all data and we convert it into an array (matrix)
	l=np.loadtxt(fichier)
	return l
        fichier.close()

def name(array):
	D=np.transpose(array)
	X=D[0]
	nbRFP=D[1:6]
	szRFP=D[6:11]
	nbCRFP=D[11:16]
	szCRFP=D[16:21]
	nbGFP=D[21:29]
	szGFP=D[29:37]
	nbCGFP=D[37:45]
	szCGFP=D[45:53]
	return X,nbRFP,szRFP,nbCRFP,szCRFP,nbGFP,szGFP,nbCGFP,szCGFP


def moyenne(array):
	stddev = np.std(array, axis=0)
	somme=np.sum(array, axis=0)
	nomarray=somme/5
	print nomarray
	return nomarray, stddev

def bar(y, y2, fig,title,ylabel,stddev1, stddev2): # this function will create the bar chart: it takes as parameters the list to plot in the x axis, in the y axis, the number of the figure in which the graph has to be drawn, the name of the x axis, the name of the y axis, and the standard deviation on y to draw error bars
	N=5
	ind=np.arange(N)
	width=0.5
	fig, ax = plt.subplots()
	rects1 = ax.bar(ind, y, width, color='r', yerr=stddev1,  ecolor = 'k', edgecolor = "none")
    	rects2 = ax.bar(ind + width, y2, width, color='g', yerr=stddev2, ecolor = 'k', edgecolor = "none")
	ax.set_ylabel(ylabel, fontsize = 16)
	ax.set_title(title, fontsize = 22)
	ax.set_xticks(ind + 2*width)

def normalizesize(array):
	for i in range(len(array[1])):
		for k in range(len(array)):
			if array[k][i]<2.5:
				array[k][i]=1
			elif array[k][i]<5:
				array[k][i]=2
			else:
				array[k][i]=4
	return array

def prod(zone, nb, size):
	prod=zone*nb*size
	return prod

def coeff(array):
	coeff=np.sum(array, axis=1)
	

def autolabel(rects, i, fig):  
    # attach some text labels 

	kolor = ["GFP","", "RFP"]
	fig, ax = plt.subplots()   
	for rect in rects:  
		height = rect.get_height()  
		ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
		'%s' % kolor[i],
		ha='center', va='bottom')  
		
def graphcoeff(y, y2, fig,title,ylabel,stddev1, stddev2):
	loc2 = [np.mean([50])]
  	error2 = [1.915000000000191]  
 
	N = 1  
   
	ind = np.arange(N)  # the x locations for the groups  
	width = 1./3   # the width of the bars   
   
	fig, ax = plt.subplots()  
	rects1 = ax.bar(ind, y, width, color='r', yerr=stddev1,  ecolor = 'k', edgecolor =  'none'  )  
	rects2 = ax.bar(ind + width, loc2, width, color='w', yerr=error2, ecolor = 'w', edgecolor =   'none'  )
	rects3 = ax.bar(ind + 2*width, y2, width, color='g', yerr=stddev2, ecolor = 'k', edgecolor =   'none'  )
   
	plt.xlim(-0.5, 1.5)
	ax.set_ylabel(ylabel, fontsize = 14)  
	ax.set_title(title, fontsize = 20)  
	ax.axes.get_xaxis().set_visible(False)
 
	autolabel(rects1,0, 3)  
	autolabel(rects2,1, 3)
	autolabel(rects3,2, 3)

	plt.show() 

def main():
	l=lecture("ecolor.tsv")
	X,nbRFP,szRFP,nbCRFP,szCRFP,nbGFP,szGFP,nbCGFP,szCGFP=name(l)
	moynbR, stddevnbR=moyenne(nbRFP)
	moynbG, stddevnbG=moyenne(nbGFP)
	bar(moynbR, moynbG, 1, "Number of colonies for an increasing concentration of nutriments", "number of colonies", stddevnbR, stddevnbG)
	
	moyszR, stddevszR=moyenne(szRFP)
	moyszG, stddevszG=moyenne(szGFP)
	bar(moyszR, moyszG, 2, "Size of colonies for an increasing concentration of nutriments", "size of colonies", stddevszR, stddevszG)
	
	NszRFP=normalizesize(szRFP)
	NszGFP=normalizesize(szGFP)
	prodRFP=prod(X,nbRFP,NszRFP)
	prodGFP=prod(X,nbGFP,NszGFP)
	moyprodRFP1, stddevprodRFP1=moyenne(prodRFP)
	coeffRFP=np.sum(moyprodRFP1)
	stddevprodRFP=np.sum(stddevprodRFP1)
	moyprodGFP1, stddevprodGFP1=moyenne(prodGFP)
	coeffGFP=np.sum(moyprodGFP1)
	stddevcoeffGFP=np.sum(stddevcoeffGFP1)

	graphcoeff(moycoeffRFP, moycoeffGFP, 3,"Gradient response", "Gradient response of RFP and GFP", stddevcoeffRFP, stddevcoeffGFP)


main ()


	
