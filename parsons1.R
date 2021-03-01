# script to extract filename from full path

trialname=parse_number(trialname) #remove the exension
library(tidyverse)


name <- "files/0023/expt_A_trial_002.png"
print(paste0("this is trial ",trialname)) #outputtrialname=str_split(filename,"_",simplify=TRUE)[4] #get the trial name + extension


filename=str_split(name,"/",simplify=TRUE)[3] #get just the filename
