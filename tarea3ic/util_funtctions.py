# se separan por clases
from random import shuffle
import matplotlib.pyplot as plt
import numpy as np
import itertools



def class_separate(data):
    arr_class = {'c_0': [], 'c_1': [], 'c_2': [], 'c_3': [], 'c_4': [], 'c_5': [], 'c_6': [], 'c_7': [], 'c_8': [],
                 'c_9': []}
    for i in data:
        arr_class['c_' + str(i[64])].append(i)
    return arr_class


def count_c(data):
    num = []
    for i in range(10):
        num.append(len(data['c_' + str(i)]))
    return num


def divide_proportional(total, per, arrays, nums):
    # se calcula el largo del arreglo dependiendo de que porcentaje se quiera
    len_newarr = round(total * per)
    # se calcula la proporcion
    proportions = [x / total for x in nums]
    new_data = []
    for j, n in enumerate(proportions):
        shuffle(arrays['c_' + str(j)])  # se desordenan los arreglos
        for i in range(round(n * len_newarr)):
            new_data.append(arrays['c_' + str(j)].pop())
    return new_data, proportions


def verf(data, originalprop):
    a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in data:
        a[i[64]] += 1
    new_prop = [x / len(data) for x in a]
    for n in range(10):
        # si algun error es mayor al 5% se avisa
        if originalprop[n] - new_prop[n] > 0.05:
            print(" Error falló proporción")


def separate_feat_class(arrangement, a_feat, a_class):
    for data in arrangement:
        a_feat.append(data[0:63])
        a_class.append(data[-1])


def plot_confusion_matrix(cm, classes, normalize=False, title='Confusion matrix', cmap=plt.cm.jet):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('Real')
    plt.xlabel('Predicción')
    return cm
