import numpy as np
def costFunction(theta0,theta1,data):
   
    totalError=0
    for i in range(0, len(data)):
         y=data[i,1]
         x=data[i,0]
         totalError+=(y-(theta1*x+theta0))**2
    return totalError/float(len(data))
def run():
    data=np.genfromtxt("data.csv", delimiter=",")
    X=[[0 for i in range(2)] for j in range(len(data))]
    Y=[0 for i in range(len(data))]
    for i in range(0,len(data)):
        X[i][0]=1
        X[i][1]=data[i,0]
        Y[i]=data[i,1]
    Xt=np.transpose(X)
    XtX_ =np.linalg.inv(XtX) 
    XtX_Xt=(XtX_).dot(Xt)
    [Theta0, Theta1]=XtX_Xt.dot(Y)
    print('Theta0=',Theta0,'Theta1=', Theta1)
    print('costfunction=',costFunction(Theta0,Theta1,data))
    y1=70.34607562*Theta1 + Theta0
    print('pridected vale=',y1)
if __name__ == '__main__':
    run()