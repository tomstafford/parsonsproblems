# script to draw a sine wave '''
library(here) #file location functions
library(tidyverse) #graphing and wrangling functions

x <-  seq(-6,6,0.1) #get x values for the points
y = sin(x) #get the corresponding y values 

p <- ggplot(data.frame(x,y),aes(x,y)) #make plot object 
p + geom_point() + #add layer to show points
  xlab('x in radians') + #add labels
  ylab('sin(x)')

ggsave(here("outputs","sine.png")) #export graph as png
