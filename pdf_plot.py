def pdf_plot(fig2, indata, i, xbrs, ybrs, munits):
	''' creates a Gaussian pdf plot of any array. If the array has multiple dimensions
	it is flattened first. Relies on the Python "Statistics"  and "Matplotlib" libraries. '''

	import statistics as st
	import numpy as np
	import matplotlib.pyplot as plt
	from scipy import stats
	colours=['Teal', 'MediumBlue', 'DodgerBlue', 'DarkTurquoise', 'Chartreuse', 'Green', 'Yellow', 'Red', 'Orange', 'Chocolate', 'DarkRed', 'Black']
	
	pshape=np.zeros((12))
	ploc=np.zeros((12))
	pscale=np.zeros((12))
	
	##flatten array if necessary 
	#indata=indata.flatten(1)
	
	# adjust weight or bandwidth
	#weight=[1]*len(z4)
	#h1=bandwidth(z4,weight,"Epanechnikov")
	#h2=bandwidth(z4,weight,"Gaussian")
	
	# do pdf calculation
	y0,x0=st.pdf(indata)
	yg,xg=st.pdf(indata, kernel="Gaussian")
	if i > 10:
		plt.plot(x0,y0,color='black',linewidth=2.5)
		plt.title(' ')
		plt.title('1961-1990', fontsize=14)
	else:
		plt.plot(x0,y0,colours[i])
		plt.title(' ')
		plt.title('2061-2090', fontsize=14)
	
	# limits axes
	yy1=ybrs[0]
	yy2=ybrs[1]
	xx1=xbrs[0]
	xx2=xbrs[1]
	plt.ylim((yy1,yy2))
	plt.xlim((xx1,xx2))
	plt.locator_params(nbins=7)
	# set axis label size 
	plt.rc('font', size=12)
	#fig2.set_xlabel(munits, fontsize=11)

	x=[5,25,50,75,95]
	index_pdf = stats.norm.pdf(x) 
	
	pshape[i], ploc[i], pscale[i] = stats.lognorm.fit(indata, floc=0)
	
	#return index_pdf
