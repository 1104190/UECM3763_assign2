import pylab as p
import numpy as np

# Setup Parameters

# Values of Mu and Sigma is given 
mu=0.1;  
sigma=0.26; 
S0=39; # Price at time zero
n_path=1000; # Total number of simulations
n= n_partitions = 1000; # Number of partitions in the interval 

# Create Brownian Paths 
t = p.linspace (0,3,n+1); 
dB = p.randn(n_path,n+1) / p.sqrt(n);
dB[:,0] = 0; 
B=dB.cumsum(axis=1);

# Calculate stock prices
nu = mu - sigma*sigma/2;
S =p.zeros_like(B);
S[:,0] = S0
S[:,1:] = S0*p.exp(nu*t[1:]+sigma*B[:,1:]);

#Plot the 5 realizations with x label and y label 
S_plot= S[0:5]
p.plot(t,S_plot.transpose());
p.xlabel('Time, t');
p.ylabel('Stock prices, RM');
p.title('5 REALIZATIONS OF THE GEOMETRIC BROWNIAN MOTION')
p.show();

# Calculate the expected value of S(3)
last_price_x = p.array(S[:,-1]);
expected_price_S3 = np.mean(last_price_x);
print('Expected value, E[S(3)] = ',expected_price_S3);

# Calculate the variance of S(3)
variance_S3 = np.var(last_price_x);
print('Variance, Var[S(3)] = ',variance_S3);

# Calculate P[S(3)>39]
y = last_price_x > 39; #find out all the values that are larger than 39
total = p.sum(y) #add together all the values that are larger than 39 
probability= total/n_path 
print('P[S(3)>39] = ' ,probability);

# Calculate E[S(3)|S(3)>39]
z = p.sum(last_price_x * y) 
expected_value = z/total
print('E[S(3)|S(3)>39] = ' ,expected_value);
 