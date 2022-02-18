import numpy as np
import matplotlib.pyplot as plt
rectas = []
vector = []
ori = []

num_vector = int(input("¿Cual es el numero de vectores que deseas agregar?"))
for i in range(num_vector):
    ori.append([0,0]) 
    print("Vector #{}".format(i+1))
    punto1 = list(map(int,input("Ingrese los dos valores del vector con una coma\n").split(",")))
    vector.append(punto1)

origen = np.array(ori)
vectores = np.array(vector)
fig,ax = plt.subplots(1)

ax.quiver(*origen,vectores[:,0],vectores[:,1],scale = 15)
