#%%
#Carga de módulos y librerías
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn import *
from mpl_toolkits.mplot3d import Axes3D
#Filtrar alertas (futurewarnings)
from warnings import simplefilter
simplefilter(action = 'ignore', category = FutureWarning)

#%%
#Cargar datos

data = pd.read_csv('ex1data1.txt', sep=',',names=['X1','Y'])

#%%
# Separar datos en X y Y------> X_train, Y_train, X_test, Y_test
array = data.values
X = array[:,0:(np.size(array,1)-1)]; Y = array[:,(np.size(array,1)-1):np.size(array,1)]
X_train,X_test,Y_train,Y_test = model_selection.train_test_split(X,Y,test_size=0.3,random_state=1)

m = np.size(X,0); n = np.size(X,1)

#%%
#Funciones para gradiente, costo, predicción
def matrizX0(X):#! Arroja: X con X0 en la primera columna
	##Agrega el X0 en la matriz X---------> Queda una matriz de m x n+1
	Xc = np.insert(X,0,np.ones(np.size(X,0)),axis=1)

	return(Xc)

def computeCost(Xc,Y,theta):#! Arroja: J
	w = np.dot(Xc,theta)
	
	J = (1/(2*m)) * np.sum( (w - Y)**2)
	return J

def gradientDescent(Xc, Y, theta, alpha):##! Arroja:  theta,J_history, No_iter
	  
	J_history = []        
	iteracion = 0
	while True:
		w = np.dot(Xc,theta)

		temp1 = theta[0] - alpha * (1/m) * ( np.sum( np.transpose((w - Y )) * Xc[ : , 0] ))
		temp2 = theta[1] - alpha * (1/m) * ( np.sum( np.transpose((w - Y )) * Xc[ : , 1] ))

		theta[0] = temp1
		theta[1] = temp2

		J_history.append(computeCost(Xc,Y,theta))
		if iteracion != 0:
			if J_history[iteracion-1] - J_history[iteracion] > (1/1e5):            
				iteracion+=1
				continue            
			else:
				break
			
		iteracion+=1
	return theta,J_history,iteracion

def hipotesis(Xc,theta):#!Arroja: h   "Predict"
	### X debe ser una matriz (m x n) y theta un vector (n x 1)--------> h queda con dimensión  m x 1
	h=np.dot(Xc,theta)
	return(h)

def graficarJ_theta(Xc,Y):
	theta0_vals = np.linspace(-10,10,100)
	theta1_vals = np.linspace(-1,4,100)
	J_vals = np.zeros((len(theta0_vals),len(theta1_vals)))
	for i in range(len(theta0_vals)):
		for j in range(len(theta1_vals)):
			t = [theta0_vals[i],theta1_vals[j]]
			J_vals[i,j] = computeCost(Xc,Y,t)    
	theta0_vals,theta1_vals = np.meshgrid(theta0_vals,theta1_vals)

	J_vals = np.transpose(J_vals)
	fg = plt.figure()
	ax = fg.add_subplot(111, projection ='3d')
	
	surf = ax.plot_surface(theta0_vals, theta1_vals, J_vals, cmap = plt.cm.winter_r)
	ax.set_xlabel('theta 0');ax.set_ylabel('theta 1'),ax.set_zlabel('J')
	plt.show()

def graficarJ_iteraciones(J_history,No_iter):
	fg = plt.figure()
	iteraciones = np.linspace(0,No_iter+1,No_iter+1)
	plt.plot(iteraciones,J_history)
	plt.xlabel("Iteraciones"),plt.ylabel("Costo de la función")
	plt.show()

#%%
#Inicializar variables
Xc = matrizX0(X)
Xc_train=matrizX0(X_train)
Xc_test=matrizX0(X_test)
alpha = 0.03
theta_inicial = np.zeros((n+1,1))

#%%
#Calcular todo
theta,J_history,No_iter = gradientDescent(Xc_train,Y_train,theta_inicial,alpha)
predict = hipotesis(Xc_test,theta)
#%%
#Verificar error
LR=linear_model.LinearRegression()
LR.fit(X_train,Y_train)
predictSK = LR.predict(X_test)

print("R2SCORE de SKlearn: %.4f\nR2SCORE propio: %.4f"  %(metrics.r2_score(Y_test,predictSK),metrics.r2_score(Y_test,predict)))

print("RMSE de SKLearn: %.4f\nRMSE propio: %.4f" %(metrics.mean_squared_error(Y_test,predictSK),metrics.mean_squared_error(Y_test,predict)))    
Comparativa = np.column_stack((predict,predictSK,Y_test))
Resultados = pd.DataFrame(Comparativa,columns=["Propia","SKlearn","Y_test"])
#Resultados.to_excel("Datos\ex1ML\ex1data1_Resultados.xls")


fg = plt.figure()
plt.plot(X_test,Y_test,marker="x",color="red",MarkerSize=5,linestyle="")
plt.plot(X_test,predict,color="blue",label='propio')
plt.plot(X_test,predictSK,color="green",label='sklearn')
plt.ylabel('Profit in $10.000s')
plt.xlabel("Population of City in 10,000's")
plt.legend(loc='upper left')
plt.show()



#%%
graficarJ_theta(Xc,Y)
#%%
graficarJ_iteraciones(J_history,No_iter)

# %%
