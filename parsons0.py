
'''script to extract filename from full path'''
filename=name.split('/')[2] #get just the filename
print("this is trial " + trialname) #output
trialname=filename.split('_')[3] #get the trial name + extension


trialname=trialname[:-4] #remove the exension


name='files/0023/expt_A_trial_002.png'
