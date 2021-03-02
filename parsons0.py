


'''script to extract filename from full path'''


name='files/0023/expt_A_trial_002.png'
trialname=trialname[:-4] #remove the exension
filename=name.split('/')[2] #get just the filename
trialname=filename.split('_')[3] #get the trial name + extension
print("this is trial " + trialname) #output
