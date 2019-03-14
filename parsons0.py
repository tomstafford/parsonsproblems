

filename=name.split('/')[2] #get just the filename
trialname=filename.split('_')[3] #get the trial name + extension

name='files/0023/expt_A_trial_002.png'

'''script to extract filename from full path'''

trialname=trialname[:-4] #remove the exension
print("this is trial " + trialname) #output
