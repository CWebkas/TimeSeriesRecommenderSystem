
from tsfresh import extract_features
import tsfel
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import AffinityPropagation
from tsfresh import feature_selection
from xgboost import XGBClassifier
import xgboost as xgb
import pandas as pd
from sklearn.decomposition import PCA



def tsfresh_py_extractor(ts_dat):
    extracted_features = extract_features(ts_dat, column_id="id", n_jobs=0, disable_progressbar=True)
    return extracted_features

""""
def tsfel_py_extractor(ts_dat):
  cfg = tsfel.get_features_by_domain()
  extracted_features = 1
  extracted_features = tsfel.time_series_features_extractor(cfg, ts_dat)
  return extracted_features
"""
def adder(a, b,d):
  c = a+b+d
  return c

def py_scaler(data):
  mms = MinMaxScaler()
  mms.fit(data)
  data_transformed = pd.DataFrame(mms.transform(data))
  return(data_transformed)
  

def py_affinity_modeler(dat):
  clustering_truth = AffinityPropagation(random_state=5, preference = -65).fit(dat)
  return(clustering_truth)
  
def py_affinity_labeller(clustering_truth):
  #clustering_truth = AffinityPropagation(random_state=5, preference = -65).fit(dat)
  return(clustering_truth.labels_)
  
  
def py_affinity_predictor(clustering_truth, dat):
  preds = clustering_truth.predict(dat)
  return(preds)
  

def py_feature_relevance(dat, labs):
  tbl = feature_selection.relevance.calculate_relevance_table(X=dat, y=labs)
  return(tbl)
  
  
def py_affinity_centers(clustering_truth):
  reps = clustering_truth.cluster_centers_indices_
  return(reps)
  
def py_affinity_propagation(dat):
  clustering_truth = AffinityPropagation(random_state=5, preference = -65).fit(dat)
  return(clustering_truth, clustering_truth.labels_, clustering_truth.cluster_centers_indices_+1)
  
  
def py_xgbooster(data):
  X = data.drop('cls_label',1)
  y = data.cls_label.apply(str)
  model=XGBClassifier()
  model.fit(X, y)
  nms = model.get_booster().feature_names
  imps = model.feature_importances_
  scores = pd.concat([pd.DataFrame(nms, columns=['names']),pd.DataFrame(imps, columns=['importances'])], axis=1)
  importance_sorted = scores.sort_values(by=['importances'])
  return(importance_sorted)
  

def py_pca_demo(data, ncomp): 
  pca = PCA(n_components = int(ncomp))
  pca.fit(data)
  return(pca.explained_variance_ratio_)

def py_pca(data, ncomp): 
  pca = PCA(n_components = int(ncomp))
  pca.fit(data)
  transf = pca.transform(data)
  return(transf)
  
  
  
