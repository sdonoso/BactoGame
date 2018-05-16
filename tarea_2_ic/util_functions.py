import csv, operator
from random import shuffle
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import auc

def openCsv(dataSet, PULSAR, NOT_PULSAR):
    """
    creat two arrangement pulsar and not pulsar with his data

    :param dataSet: all data in a csv archive
    :param PULSAR: arrangement of pulsar data
    :param NOT_PULSAR: arrangement of not pulsar data
    :return:
    """
    with open(dataSet) as csvregistry:
        spamreader = csv.reader(csvregistry, quoting=csv.QUOTE_NONNUMERIC)
        for row in spamreader:
            if row[8] == 0:
                NOT_PULSAR.append(row)
            else:
                PULSAR.append(row)

def divideProportional(notPulsar, pulsar, perOfOverall):
    """
    create a new arrangement of pulsar and not pulsar with the correct proportion and percent of overall
    :param notPulsar: arrangement of not pulsar data
    :param pulsar: arrangemetn of pulsar data
    :param perOfOverall: percentage of overall
    :return: an arrangement with pulsar and not pulsar
    """
    shuffle(notPulsar)
    shuffle(pulsar)
    total = len(pulsar) + len(notPulsar)
    newSet = []
    proportion = round(len(notPulsar) / len(pulsar))
    prop = proportion
    lenNewSet = round(total * perOfOverall)
    for i in range(lenNewSet):
        if prop == 0:
            newSet.append(pulsar.pop())
            prop = proportion
        else:
            newSet.append(notPulsar.pop())
            prop -= 1
    return newSet
def sub_cjt(arrangment, n):
    shuffle(arrangment)
    return arrangment[0:n]

def separate_feat_class(arrangement,a_feat,a_class):
    for data in arrangement:
        a_feat.append(data[0:8])
        a_class.append(data[-1])

def tpv_tpf(score, ar_class):
    asd = np.linspace(-10, 30, 300)
    tap = []
    afp = []
    for t in asd:
        t_p = 0
        f_p = 0
        t_n = 0
        f_n = 0
        for j, i in enumerate(score):
            if i > t and ar_class[j] == 1:
                t_p += 1
            elif i > t and ar_class[j] == 0:
                f_p += 1
            elif i < t and ar_class[j] == 0:
                t_n += 1
            elif i < t and ar_class[j] == 1:
                f_n += 1

        tap.append(t_p / (t_p + f_n))
        afp.append(f_p / (f_p + t_n))
    return tap, afp

def plot_roc(true_p, false_pos, c, kernel, sigma=None, grad=None):
    plt.plot(false_pos, true_p, 'b', label="area " + str(round(auc(false_pos, true_p), 4)))
    plt.legend(loc='lower right')
    if grad != None:
        plt.title("Curva ROC Kernel " + kernel + "y  C=" + c + "grad=" + grad)
    elif sigma != None:
        plt.title("Curva ROC Kernel " + kernel + "y  C=" + c + "sigma=" + sigma)
    else:
        plt.title("Curva ROC Kernel " + kernel + "y  C=" + c)

    plt.xlabel("Tasa de Falsos Positivos")
    plt.ylabel("Tasa de Verdaderis Positivos")

    plt.show()

