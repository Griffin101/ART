from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import numpy as np

x,y = make_blobs(n_samples=500, centers=2, random_state=0, cluster_std=0.40)
plt.scatter(x[:,0],x[:,1],c=y,s=50,cmap='spring')

m,b,d=(1,0.65,0.33)
xfit=np.linspace(-1,3.5)

yfit=m*xfit+b
plt.plot(xfit,yfit, '-k')

plt.fill_between(xfit,yfit-d,yfit+d, edgecolor='none', color='#AAAAAA', alpha=0.4)

plt.xlim(-1,3.5)
plt.show()
