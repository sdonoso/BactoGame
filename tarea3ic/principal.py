from random import shuffle
import numpy as np

# se cargan los datos
from sklearn.cross_validation import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt

from util_funtctions import class_separate, count_c, divide_proportional, verf, separate_feat_class, \
    plot_confusion_matrix

with open("Dataset_d_gitos_para_tarea_3.txt") as f:
    dataset = f.read().splitlines()
data = []
for a in dataset:
    data.append(list(map(int, a.split(","))))
TOTAL = len(data)

separate = class_separate(data)

num = count_c(separate)
print(num)
print(TOTAL)

train_val, o_prop = divide_proportional(TOTAL, 0.8, separate, num)
test = []
for i in range(10):
    test += (separate['c_' + str(i)])
print(len(test))
print(len(train_val))

# se verifica si estan correctas las proporciones
verf(train_val, o_prop)
# se guardan los conjuntos de entramiento validacion y test
np.save('test', test)
np.save('train_val', train_val)

