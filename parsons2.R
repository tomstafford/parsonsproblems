
# script to draw a sine wave 

y = sin(x) #get the corresponding y values 

x <-  seq(-6,6,0.1) #get x values for the points
  xlab('x in radians') + #add labels
p + geom_point() + #add layer to show points
p <- ggplot(data.frame(x,y),aes(x,y)) #make plot object 
library(tidyverse) #graphing and wrangling functions
library(here) #file location functions
  ylab('sin(x)')
ggsave(here("outputs","sine.png")) #export graph as png
