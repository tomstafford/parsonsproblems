
y = np.sin(x) #get the corresponding y values 

plt.ylabel('sin(x)')  #add ylabel
import os #file and folder functions
''' script to draw a sine wave '''
import matplotlib.pyplot as plt #plotting functions
import numpy as np #number functions
plt.clf() #clear current plot (if there is one)
plt.xlabel('x (radians)') #add xlabel

plt.plot(x,y) #plot the points
plt.savefig(os.path.join('outputs','sine.png')) #export graph as png
x = np.linspace(-6,6,100) #get x values for the points
