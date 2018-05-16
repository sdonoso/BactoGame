import numpy as np
from util_functions import openCsv, divideProportional, separate_feat_class, sub_cjt
TOTAL_PULSAR = 1639
TOTAL_NPULSAR = 16259
# priemero saco un subconjunto de 2000 para que siga siendo representativo saco 181 pulsar y 1819 no pulsar
PULSAR = []
NOT_PULSAR = []

openCsv('HTRU_2.csv', PULSAR, NOT_PULSAR)
# priemero saco un subconjunto de 2000 para que siga siendo representativo saco 181 pulsar y 1819 no pulsar
PULSAR = sub_cjt(PULSAR, 181)
NOT_PULSAR = sub_cjt(NOT_PULSAR, 1819)
TEST = divideProportional(NOT_PULSAR, PULSAR, 0.2)
VALI = divideProportional(NOT_PULSAR, PULSAR, 0.25)  # ya que ahora queda el 80% del cjto original
TRAINING = NOT_PULSAR + PULSAR
def verification():
    t_p = 0
    t_np = 0
    for a in TEST:
        if a[8] == 1:
            t_p += 1
        else:
            t_np += 1
    v_p = 0
    v_np = 0
    for a in VALI:
        if a[8] == 1:
            v_p += 1
        else:
            v_np += 1
    tr_p = 0
    tr_np = 0
    for a in TRAINING:
        if a[8] == 1:
            tr_p += 1
        else:
            tr_np += 1

    print("proporcion test " + str(t_np / t_p))
    print("proporcion validacion " + str(v_np / v_p))
    print("proporcion training " + str(tr_np / tr_p))
    print(len(TEST) + len(VALI) + len(TRAINING))

verification()
np.save('test', TEST)
np.save('vali', VALI)
np.save('training', TRAINING)

