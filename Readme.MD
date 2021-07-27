# Time Series Classification
### Master Thesis by Lukas Weixler (University of Konstanz) at s-peers AG 
- University Supervisors: Prof. Dr. Susumu Shikano and Prof. Dr. Peter Selb
- Company Supervisors: Dr. Dominik Bertsche and Dr. Stefan Lieder


## Intro
- Goal: 
![image](https://user-images.githubusercontent.com/81747670/119829875-ff0c5880-befb-11eb-828e-32213fc5d2f0.png)
- Why is this useful
- Use of the approach determined through the following criterion: Automated Recommending of time series forecasting algorithms to a user based on a classifier will result in a better performance than naive forecasting 

## Literature
Literature is added and categorized throughout the entire process. View the current literature collection [here](https://github.com/s-peers/TSClassification/blob/master/theory/literature.MD)

## Theory
#### Key Argument
  - Automated Recommending of time series forecasting algorithms to a user based on a classifier will result in a better performance than naive forecasting
    - Why: Feature based classification also sorts the time series based on the performance of the algorithms
      - Example: Unstructured time series will have more precise naive forecasts; Stationary time series will have more precise ETS forecasts
      - Literature: Hyndman FFORMA
#### Additional Arguments
 - Using cluster labels as features will still result in a better performance of the recommended algorithms, compared to naive forecasting
 

#### Assumptions
  - Define Time Series
  - Define time series discrimination - feature based in my case
  - Define performance
    - Evaluation Scores: Classification Error, Selected OWI, Weighted OWI, Naive Weighted OWI, Oracle OWI, Single method OWI, Average OWI 
    - Description can be found [here](https://github.com/robjhyndman/M4metalearning/blob/master/docs/metalearning_example.md)
    - Focus in distinguishing weighted and unweighted approach
  - Define clustering and classifying



#### Clustering
  - Feature Extraction
    - Features are from the `M4Metalearning` and the `tsfresh` packages. The latter is a python package and was imported to R via reticulate
    - Description and summary of the features can be found [here](https://github.com/s-peers/TSClassification/blob/master/theory/Features.MD)   
  - Affinity Propagation
    - [Basic explanation](https://towardsdatascience.com/unsupervised-machine-learning-affinity-propagation-algorithm-explained-d1fef85f22c8)
    - Potential Algorithms:
      - Hierarchical Clustering (linkage)
      - KMeans
      - DBScan
      - HDBScan
      - EM (Gaussian Mixture)
      - Optics
      - Dynamic Time warping (with pure ts data)

    - Final Choice: Affinity Propagation
      - Reason: n clust is automatically determined, representatives of each cluster are inherently provided
      - Compromise: Stratified sample of at least 10% for each ts-length stratum, prediction for all non-sampled time series
    - Evaluate the clustering 
      - feature importance is the focus. Measuring clustering quality is unrealistic for unlabeled data - find literature legitimizing affinity propagation
      - Feature importance evaluated in tsfresh, but only gave significance values - I want impact strength
      - Getting impact strength through "embedded approach" (Literature) via XGBoost feature importance for each cluster
      - Representative's features are to be determined 
      - Compare values of important features for each cluster with overall mean of feature and representative ts
      - Determine Softmax for best prediction, Compare to Hyndman's approach in later step


#### Forecast Recommender System
  - Advantage of such a recommender system
    - Previous approach: Combine domain knowledge with results from all applied forecasting algorithms
    - Approach in this paper: Train a XGBoost classifier on different types of ts to determine the best forecasting algorithm for a newly incoming time series
    - Advantages: 
      - Reduced computational cost to forecast a newly incoming time series
      - Additional information on classes of time series made available through clustering and XGBoost classifier
    - Challenge: Train data might not cover all ts profiles equally
      - Clustering gives user the option to manually search for a useful prediction algorithm     
  - Approach by Rob Hyndman
    - Describe computation workflow
    ![image](https://user-images.githubusercontent.com/81747670/119799934-d9238b80-bedc-11eb-9fe1-d38ef99b950d.png)

    - Describe the [forecasting algorithms and potential performance implications for different types of time series](https://github.com/s-peers/TSClassification/blob/master/theory/algorithms.md)
  - Modified clustering approach of this thesis 
    - Describe computation workflow
    ![image](https://user-images.githubusercontent.com/81747670/119819330-8ce24680-bef0-11eb-8d61-4b2883d5fbb0.png)

    - Restress the advantages of a cluster- than label approach
      - Scalability
      - Less computation power
    - Justify theoretically why we 'd still expect a sufficient performance



## Model
- Describe XGBoost in this specific environment (80-20 split, hyperparameter tuning didn't help, softmax approach) - Use Hyndman, since I also use his package

## Data
- Check this [link](https://cloud.uni-konstanz.de/index.php/s/STq79pjw9LgiG7z) to acesss the RData objects.
- How many companies, how many hierarchies, domain
- How many TS, length, seasonality etc
- Deleted due to duplicates, inability to calculate an error
- Descriptive overview on the data, using affinity propagation and feature importance measurement approach
  - [Most important features for singular clusters](https://github.com/s-peers/TSClassification/issues/8)
  - Plot the clusters using pca

## Results
- Show evaluation scores from the Hyndman package and interpret them.
- Show cluster-specific performances and interpret them

## Discussion
- Relate evaluation scores to key argument from the Theory chapter
- Relate cluster-specific performances to additional arguments from the Theory chapter

## Conclusion
- Achivements
  - Shown that Hyndman approach has domain-specific applicability
  - Demonstrated Affinity propagation as attractive alternative to conventional clustering algorithms
  - Shown a new approach of ts data description through feature extraction, clustering and embedded classification
  - Foundation for a more scalable model through clustering is provided
 - Challenges
  - Make weighted approach usable for these types of data
  - Other domains with other TS structures
  - Make cls approach scalable 

