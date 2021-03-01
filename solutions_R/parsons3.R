'''script to draw histogram of greyscale values of pixels in the mona lisa Image downloaded from Wikimedia Commons #https://commons.wikimedia.org/wiki/File:Mona_Lisa,_by_Leonardo_da_Vinci,_from_C2RMF_retouched.jpg '''

import matplotlib.pyplot as plt #plotting functions
import matplotlib.image as mpimg #image manipulation functions
import os #file and folder function
import numpy as np #number functions

def rgb2gray(rgb): #a function for converting image pixel values from RGB to greyscale
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114]) #return greyscale values

img = mpimg.imread(os.path.join('inputs','monalisa.jpg')) #load the image from file
gray = rgb2gray(img)    #use function to convert pixel values to greyscale 
plt.imshow(gray, cmap = plt.get_cmap('gray')) #show the converted image to check conversion works


pixel_values=gray.flatten() #convert image data to a linear array of values (so we can plot the histogram)

plt.clf() #clear current plot (if there is one)
plt.hist(pixel_values,bins=50,color='grey') #plot histogram
plt.xlabel('greyscale values') #xlabel
plt.ylabel('frequency') #ylabel
plt.title('Distribution of pixel values in the Mona Lisa') #title
plt.savefig(os.path.join('outputs','mona_histogram.png'))#export histogram as png

