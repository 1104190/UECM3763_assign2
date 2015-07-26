from pandas.io.data import DataReader as DR
from datetime import datetime as dt
import pylab as p
import numpy as np

# Dowloads daily data for a counter called Malayan Banking 
start = dt(2011, 1, 1)
end = dt(2014, 12, 31)
data = DR("1155.KL", 'yahoo', start, end) #download from yahoo

# Pick the data for at least 3 years
data = p.array(data)
closing = data[:,3]
sum = closing.cumsum()
print(closing)

# Take 5-day moving average
average_days = 5

matrix = np.zeros((2,(len(sum)-average_days+1)))
matrix[0,:] = sum[(average_days-1):]
matrix[1,1:] = sum[:-(average_days)]

moving_average = (matrix[0] - matrix[1]) / average_days

# Plot the 5 days moving average of Malayan Banking
p.plot(moving_average)
p.xlabel('Days');
p.ylabel('5 days average');
p.title('5-DAYS MOVING AVERAGE OF MALAYAN BANKING FROM 01/01/2011 TO 31/12/2014');
p.show()

# Correlation of Malayan Banking
complete_data = ['^KLSE','1155.KL']
cor = DR(complete_data, 'yahoo', start, end)['Close']
correlation = cor.corr()

print('THE CORRELATION OF MALAYAN BANKING IS ')
print(correlation)