plt.ylabel('sin(x)')  #add ylabel

import numpy as np #number functions
y = np.sin(x) #get the corresponding y values 
''' script to draw a sine wave '''
x = np.linspace(-6,6,100) #get x values for the points
import os #file and folder functions
plt.clf() #clear current plot (if there is one)
plt.plot(x,y) #plot the points


import matplotlib.pyplot as plt #plotting functions
plt.savefig(os.path.join('outputs','sine.png')) #export graph as png
plt.xlabel('x (radians)') #add xlabel
