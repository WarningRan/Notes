import numpy as np
import matplotlib.pyplot as plt  # plt
#导入相应的包
 
x_data = []
y_data = []

with open('C:/Users/user/Desktop/data1.txt') as f:
    res = f.readlines()
    for dat in res:
        dat.strip()
        a = dat.split(',')
        x_data.append(float(a[0]))
        y_data.append(float(a[1]))

x = np.arange(-200, -100, 1) # bias
y = np.arange(-5, 5, 0.1) # weight
Z = np.zeros((len(x), len(y)))
X,Y = np.meshgrid(x, y)
for i in range(len(x)):
    for j in range(len(y)):
        b = x[i]
        w = y[j]
        Z[j][i] = 0
        for n in range(len(x_data)):
            Z[j][i] = Z[j][i] + (y_data[n] - b - w*x_data[n])**2
        Z[j][i] = Z[j][i]/len(x_data)
 
# yadata = b + w*xdata
b = -120 # intial b
w = -4 # intial w
lr = 1 # learning rate
iteration = 100000
 
# store initial values for plotting
b_history = [b]
w_history = [w]
 
lr_b=0
lr_w=0
 
# iterations
for i in range(iteration):
 
    b_grad = 0.0
    w_grad = 0.0
    for n in range(len(x_data)):
        b_grad = b_grad - 2.0*(y_data[n] - b - w*x_data[n])*1.0
        w_grad = w_grad - 2.0*(y_data[n] - b - w*x_data[n])*x_data[n]
    
    lr_b=lr_b+b_grad**2
    lr_w=lr_w+w_grad**2
    # update parameters
    b = b - lr/np.sqrt(lr_b)*b_grad
    w = w - lr/np.sqrt(lr_w)*w_grad
 
    # store parameters for plotting
    b_history.append(b)
    w_history.append(w)
 
# plot the figure
plt.contourf(x, y, Z, 50, alpha=0.5, cmap=plt.get_cmap('jet'))
plt.plot([-188.4], [2.67], 'x', ms=12, markeredgewidth=3, color='orange')
plt.plot(b_history, w_history, 'o-', ms=3, lw=1.5, color='black')
plt.xlim(-200, -100)
plt.ylim(-5, 5)
plt.xlabel(r'$b$', fontsize=16)
plt.ylabel(r'$w$', fontsize=16)
plt.show()
