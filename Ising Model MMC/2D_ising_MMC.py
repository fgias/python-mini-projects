from __future__ import division
import matplotlib
import numpy as np
from numpy.random import rand
import matplotlib.pyplot as plt

# Simulating the Ising model

class Ising():
	''' Simulating the Ising model '''
	## Monte Carlo moves
	def mcmove(self, config, N, beta):
	    ''' Monte Carlo move using Metropolis algorithm '''
	    for i in range(N):
	        for j in range(N):
	            a = np.random.randint(0, N)
	            b = np.random.randint(0, N)
	            s = config[a, b]
	            nb = config[(a+1)%N, b] + config[(a-1)%N, b] \
	                + config[a, (b+1)%N] + config[a, (b-1)%N]
	            cost = 2*s*nb
	            if cost < 0:
	                s *= -1
	            elif rand() < np.exp(-cost/beta):
	                s *= -1
	            config[a, b] = s
	    return config


	def simulate(self):
		''' This module simulates the Ising model '''
		N, temp = 64, 3       # Initialise the lattice
		config = 2*np.random.randint(2, size=(N,N)) - 1
		f = plt.figure(figsize=(15, 15), dpi=800)
		self.configPlot(f, config, 0, N, 1)

		msrmnt = 1001
		for i in range(msrmnt):
			self.mcmove(config, N, 1.0/temp)
			if i == 1:         self.configPlot(f, config, i, N, 2)
			if i == 4:         self.configPlot(f, config, i, N, 3)
			if i == 32:        self.configPlot(f, config, i, N, 4)
			if i == 100:       self.configPlot(f, config, i, N, 5)
			if i == 1000:      self.configPlot(f, config, i, N, 6)


	def configPlot(self, f, config, i, N, n_):
		''' This module plots the configuration once passed to it along with time etc '''
		X, Y = np.meshgrid(range(N),range(N))
		sp = f.add_subplot(3, 3, n_)
		plt.setp(sp.get_yticklabels(), visible=False)
		plt.setp(sp.get_xticklabels(), visible=False)
		plt.pcolormesh(X, Y, config, cmap=plt.cm.RdBu)
		plt.title("Time=%d"%i)
		plt.axis("tight")