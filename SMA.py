import numpy as np

data = np.loadtxt("data.txt", dtype=float, delimiter=',')

t = []
Rt = []
n = len(data)
y = 3
z = 6
predicted_values = 2

for i in range(n):
    t.append(data[i][0])
    Rt.append(data[i][1])

def media_mobila(data):
    Ma = np.zeros((n, z - y + 1))
    er = np.zeros((n, z - y + 1))
    MSE = [0] * (z - y + 1)
    for x in range(y, z + 1):
        start = 0
        for i in range(x, n):
            for j in range(start, start+x):
                Ma[i][x-y] = Ma[i][x-y]+Rt[j]
                # print(Ma)
            Ma[i][x-y] = Ma[i][x-y]/x
            start = start + 1
        for i in range(x, n):
            er[i][x-y] = (data[i][1]-Ma[i][x-y]) ** 2
            MSE[x-y] = MSE[x-y] + er[i][x-y]
        MSE[x-y] = MSE[x-y] / (n-x)

    print("Ma:")
    print(Ma)
    print("Er:")
    print(er)
    print("MSE:")
    print(MSE)
    MSEMIN = MSE[0]
    poz = 0
    for i in range(1, z-y + 1):
        if MSE[i]<MSEMIN:
            MSEMIN = MSE[i]
            poz = i
    return poz+y

def prognozaMA(nr, MSEMIN):
    for i in range(nr):
        t.append(len(t)+1)
        Rt.append(0)
        for i in range(len(Rt)-MSEMIN-1, len(Rt)-1):
            Rt[len(Rt)-1] = Rt[len(Rt)-1] + Rt[i]
            # print(Rt)
        Rt[len(Rt)-1] = Rt[len(Rt)-1]/MSEMIN
    print(Rt)

prognozaMA(predicted_values, media_mobila(data))