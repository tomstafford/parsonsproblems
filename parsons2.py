import matplotlib.image as mpimg #image manipulation functions
plt.xlabel('greyscale values') #xlabel
plt.savefig(os.path.join('outputs','mona_histogram.png'))#export histogram as png


pixel_values=gray.flatten() #convert image data to a linear array of values (so we can plot the histogram)
def rgb2gray(rgb): #a function for converting image pixel values from RGB to greyscale
img = mpimg.imread(os.path.join('inputs','monalisa.jpg')) #load the image from file


    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114]) #return greyscale values
import matplotlib.pyplot as plt #plotting functions
import numpy as np #number functions
'''script to draw histogram of greyscale values of pixels in the mona lisa Image downloaded from Wikimedia Commons #https://commons.wikimedia.org/wiki/File:Mona_Lisa,_by_Leonardo_da_Vinci,_from_C2RMF_retouched.jpg '''
import os #file and folder function
plt.clf() #clear current plot (if there is one)
plt.title('Distribution of pixel values in the Mona Lisa') #title
plt.hist(pixel_values,bins=50,color='grey') #plot histogram


plt.ylabel('frequency') #ylabel
gray = rgb2gray(img)    #use function to convert pixel values to greyscale 
plt.imshow(gray, cmap = plt.get_cmap('gray')) #show the converted image to check conversion works

