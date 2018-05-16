from random import shuffle
from time import time

import numpy as np

# se cargan los datos
from sklearn.cross_validation import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt
from util_funtctions import class_separate, count_c, divide_proportional, verf, separate_feat_class, \
    plot_confusion_matrix

train_val = np.load("train_val.npy")
test = np.load("test.npy")

# separar caracteristicas de clases
train_val_feat = []
class_train_val = []
separate_feat_class(train_val, train_val_feat, class_train_val)
test_feat = []
class_test = []
separate_feat_class(test, test_feat, class_test)
# red neuronal
N = 50
start_time = time()
clf = MLPClassifier(activation='logistic', hidden_layer_sizes=(N), early_stopping=True, validation_fraction=0.25)
X, X_val, y, y_val = train_test_split(train_val_feat, np.ravel(class_train_val), random_state=clf.random_state,
                                      test_size=clf.validation_fraction)
clf.fit(train_val_feat, np.ravel(class_train_val))

test_prediccion = clf.predict(test_feat)
elapsed_time = time() - start_time
print("tiempo transcurrido desde entrenamiento hasta prediccion: %0.10f segundos" % elapsed_time)
conf_m = confusion_matrix(class_test, test_prediccion)

plt.figure()
m_norm = plot_confusion_matrix(conf_m, normalize=True, classes=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
                               title='Matriz de Confusión Capa Oculta:' + str(N) + " neuronas función sigmoide")
diagonal = []
for i in range(10):
    diagonal.append(m_norm[i][i])
print("promedio diagonal " + str(np.mean(diagonal)))
plt.show()
