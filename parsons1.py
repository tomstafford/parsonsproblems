plt.xlabel('x (radians)') #add xlabel
plt.ylabel('sin(x)')  #add ylabel
y = np.sin(x) #get the corresponding y values 
import os #file and folder functions


plt.clf() #clear current plot (if there is one)

import matplotlib.pyplot as plt #plotting functions
x = np.linspace(-6,6,100) #get x values for the points
import numpy as np #number functions
''' script to draw a sine wave '''
plt.savefig(os.path.join('outputs','sine.png')) #export graph as png
plt.plot(x,y) #plot the points
