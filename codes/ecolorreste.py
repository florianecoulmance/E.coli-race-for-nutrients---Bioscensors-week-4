#we do the same for size of colony
	moyszRFPt1, stddevszt1=moyenne(szRFPt1)
	print moyszRFPt1
	moyszRFPt2, stddevszt2=moyenne(szRFPt2)
	print moyszRFPt2
	moyszRFPt3, stddevszt3=moyenne(szRFPt3)
	print moyszRFPt3
	T2sz, T3sz=sous(moyszRFPt1, moyszRFPt2, moyszRFPt3)
	print T2sz, T3sz
	stack(moyszRFPt1, stddevszt1, T2sz, stddevszt2, T3sz, stddevszt3,4, 'Size of colonies depending on nutrient gradient at three distinct times','Size of colonies')
        plt.axis([0, 5, 0, 10])
	plt.show()

#we do the same for size control
	moyszCRFPt1, stddevszCt1=moyenne(szCRFPt1)
	moyszCRFPt2, stddevszCt2=moyenne(szCRFPt2)
	moyszCRFPt3, stddevszCt3=moyenne(szCRFPt3)
	T2szC, T3szC =sous(moyszCRFPt1, moyszCRFPt2, moyszCRFPt3)
	stack(moyszCRFPt1, stddevszCt1, T2szC, stddevszCt2, T3szC, stddevszCt3,5, 'Size of colonies for controls at three distinct times','Size of colonies')
        plt.axis([0, 5, 0, 10])
	plt.show()
