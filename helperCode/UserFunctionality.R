# Preparations

if (!require("pacman")) install.packages("pacman")
pacman::p_load(tidyverse, ggfortify, zoo, forecast, tsfeatures, parallel, data.table, tictoc, purr)
library(M4metalearning)
#library(tsibble)
#library(feasts)
#library(feasts.tsfresh)
library(reticulate)
#library(testthat)

#pd <- import("pandas")
#tsfresh <- import("tsfresh")
py_config()

# Install tsfresh R repo
#devtools::install_github("mitchelloharawild/feasts.tsfresh")
#feasts.tsfresh::install_tsfresh()


# specify path to python
#use_python("C:/Users/lukas/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Python 3.9/")


# tstrun
#py_install("tsfresh")
#conda_install("r-reticulate","tsfel")

source_python('helperCode/add.py')


tsfresh_extractor <- function(lst_elm){
  source_python('helperCode/add.py')
  # extract tsfresh feats via py function
  lst_elm$tsfresh_features <- data.frame(lst_elm$x) %>% 
  rename(Y = 1) %>% 
  mutate(id = lst_elm$Index) %>% 
  tsfresh_py_extractor() %>% as_tibble()
  
  return(lst_elm)
}


# Run Affinity Propagation
affinity_propagator <- function(dat){
  source_python('helperCode/add.py')
  # extract tsfresh feats via py function
  out <- py_affinity_propagator(dat)
  
  return(out)
}




seriesrenamR <- function(data){
  data$x<- data$Series
  data$h <- data$ForecastHorizon
  SPdata_reduced_feats[[i]]$features<-SPdata_reduced_feats[[i]]$Features
  SPdata_reduced_feats[[i]]$Features <- NULL
  data$Series <- NULL
  data$ForecastHorizon <- NULL
  return(data)}






dfConvertr <- function(data){
  # just focus on ts
  dat<- data$Series
  
  # convert to df - keep timestamp
  #out <- data.frame(Y=as.matrix(dat), date=as.Date(time(dat)))
  return(dat)
}








