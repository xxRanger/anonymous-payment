import numpy as np 
import matplotlib.pyplot as plt 
deltas = [-24,  -32,  -40]
epsilons = np.linspace(0.3,3.3,16)

# overhead is the tuple of (epsilon, overhead)
overheads = np.array([
	[18.1881,10.9142,7.74669,6.02134,4.94896,4.19396,3.62448,3.24526,2.85784,2.59597,2.36693,2.24286,2.06773,1.93782,1.81172,1.7436],
	# [20.5753,12.3383,8.77454,6.82658,5.62828,4.77351,4.12058,3.62475,3.29189,2.9835,2.72826,2.53616,2.32956,2.16579,2.06522,1.9341],
	[22.9767,13.7731,9.80672,7.61288,6.25628,5.32801,4.60318,4.08318,3.6313,3.32977,3.05911,2.82389,2.59172,2.38719,2.31817,2.07668],
	# [25.3514,15.2107,10.8285,8.40557,6.92346,5.87597,5.10169,4.49914,4.04977,3.63209,3.35214,3.09592,2.84675,2.62297,2.54837,2.3317],
	[27.7265,16.6597,11.8476,9.19833,7.55838,6.41852,5.57684,4.90335,4.39261,4.00187,3.63174,3.3676,3.11041,2.85491,2.76976,2.58856]])
marker = ["o","x","^","*","s","v"]
labels = []
plt.ylabel("Average dummy words ratio")
plt.xlabel("Ɛ")

for delta, overhead,m in zip(deltas, overheads,marker):
	label = "δ = 2^" + str(delta)
	plt.plot(epsilons, overhead, label = label,marker = m)
	labels.append(label)
plt.legend(labels)
plt.show()