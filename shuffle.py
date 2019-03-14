'''
this is not a problem!
the lines are in the correct order
this is the script I used to shuffle the lines in the other scripts
run it again if you want them in a different order
'''

import glob #filename functions
import os #file and folder functions
import random #randomisation functions

#get list of python scripts in the solutions folder
filelist=glob.glob(os.path.join('solutions','*.py'))


#loop through each file
for filename in filelist:

    #get each line, put it in a list
    lines = open(filename).readlines()
    
    #shuffle the list
    random.shuffle(lines)
    
    #write to an output file of the same name, but in the root folder
    outF = open(os.path.basename(filename), "w")
    outF.writelines(lines)
    outF.close()

