x = [3,2,1,4,5]
x
import numpy as np
np.mean(x)


#### Missing values ####?
# Functions to identify missing values?


x = [3,2,1,4,5.2,'apple']
[isinstance(i, int) for i in x]
[isinstance(i, float) for i in x]
[isinstance(i, str) for i in x]

y = 10
y.is_integer() # True

y = 10.0
y.is_integer() # True

y = 10.2
y.is_integer() # False


float(20)
float('20')

int('20')
int(20.2)

str(201)




