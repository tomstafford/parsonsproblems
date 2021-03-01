plt.savefig(os.path.join('outputs','mona_histogram.png'))#export histogram as png

import matplotlib.pyplot as plt #plotting functions
def rgb2gray(rgb): #a function for converting image pixel values from RGB to greyscale
plt.clf() #clear current plot (if there is one)
pixel_values=gray.flatten() #convert image data to a linear array of values (so we can plot the histogram)
plt.xlabel('greyscale values') #xlabel
import matplotlib.image as mpimg #image manipulation functions
plt.hist(pixel_values,bins=50,color='grey') #plot histogram

plt.ylabel('frequency') #ylabel



plt.imshow(gray, cmap = plt.get_cmap('gray')) #show the converted image to check conversion works

gray = rgb2gray(img)    #use function to convert pixel values to greyscale 
'''script to draw histogram of greyscale values of pixels in the mona lisa Image downloaded from Wikimedia Commons #https://commons.wikimedia.org/wiki/File:Mona_Lisa,_by_Leonardo_da_Vinci,_from_C2RMF_retouched.jpg '''
img = mpimg.imread(os.path.join('inputs','monalisa.jpg')) #load the image from file

import numpy as np #number functions
import os #file and folder function
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114]) #return greyscale values
plt.title('Distribution of pixel values in the Mona Lisa') #title
