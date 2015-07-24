from pandas.io.data import DataReader as DR
from datetime import datetime as dt
import pylab as p
import numpy as np

# Dowloads daily data for a counter called Malayan Banking 
start = dt(2012, 1, 1)
end = dt(2015, 12, 31)
data = DR("1155.KL", 'yahoo', start, end) #download from yahoo

# Pick the data for at least 3 years
data = p.array(data)
closing = data[:,3]
sum = closing.cumsum()
print(closing)

# Take 5-day moving average
average_days = 5

