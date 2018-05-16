from sklearn import svm
import numpy as np
from util_functions import openCsv, divideProportional, separate_feat_class, sub_cjt, tpv_tpf, plot_roc
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.metrics import auc, roc_curve

TRAINING = np.load("training.npy")
TEST = np.load("test.npy")
VALI = np.load("vali.npy")
feat_training = []
class_training = []
separate_feat_class(TRAINING, feat_training, class_training)
feat_vali = []
class_vali = []
separate_feat_class(VALI, feat_vali, class_vali)
feat_test = []
class_test = []
separate_feat_class(TEST, feat_test, class_test)
# normalizar los datos
scaler = StandardScaler().fit(feat_training)  # mean and std
norm_data_training = scaler.transform(feat_training)
norm_data_val = scaler.transform(feat_vali)
norm_data_test = scaler.transform(feat_test)
#crear clasificador y entrenar
clf = svm.SVC(C=1, kernel='linear')
clf.fit(norm_data_training, class_training)
#evaluar datos en clasificador
score_vali = clf.decision_function(norm_data_val)
score_train = clf.decision_function(norm_data_training)
score_test = clf.decision_function(norm_data_test)
#obtener arreglo de falsos positivos y verdaderos positivos
# para obtener arreglos de otros kernel seria mas preciso modificar umbral
tp_test, fp_test = tpv_tpf(score_test, class_test)
tp_training, fp_training = tpv_tpf(score_train, class_training)
tp_training, fp_training = tpv_tpf(score_train, class_training)
#plotear graficos roc este caso lineal y c= 1 para conjunto de test
plot_roc(tp_test,fp_test,'1','lineal')


