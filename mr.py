import pylab as p 
import numpy as np

# Setup Parameters 
alpha = 1
theta = 0.064
sigma = 0.27
R0 = 3 
t = 1 
n_path = 1000 # total number of simulations  
n = n_partitions = 1000 # number of partitions in the interval 

# Create Brownian Paths 
T = p.linspace (0,t,n+1)[:-1]; 
dt = t/n
dB = p.randn(n_path,n+1) / p.sqrt(n);
dB[:,0] = 0; 
B=dB.cumsum(axis=1);

# Generate the R 
R = p.zeros_like(B)
R[:,0] = R0
for col in range(n):
    R[:,col+1] = R[:,col] + (theta-R[:,col])*dt + sigma*R[:,col]*dB[:,col+1]

# Plot the 5 realizations
R_plot= R[0:5,:-1]
p.plot(T,R_plot.transpose());
p.xlabel('Time, t');
p.ylabel('R(t)');
p.title('5 REALIZATIONS OF THE MEAN REVERSAL ')
p.show()

# Calculate the expected value of R(1)
x = p.array(R[:,-1]);
expected_value_R1 = np.mean(x)
print('Expected Value, E[R(1)] = ' ,expected_value_R1)

# Calculate the P[R(1)>2]
y = x > 2;
total = p.sum(y)
probability = total/n_path
print('P[R(1)>2] = ' ,probability)


