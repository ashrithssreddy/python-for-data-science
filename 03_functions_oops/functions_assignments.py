# - Write a code to print all prime numbers from 30 to 100. Do not use a loop
[x for x in range(30,100) if all([x%i!=0 for i in range(2,x-1)])]

# recursive function to print a list in reverse
# l = list(range(11,16))
# def print_rev(x):
#     print("x is ", x)
    
#     if(not isinstance(x, list)): #  and len(x)==1
#         print(x)
#     else:
#         print(x[0])
#         print_rev(x[1:len(x)])
# print_rev(l)

l = list(range(11,16))
def print_rev(x, idx):
    if idx < len(x):
        print_rev(x, idx + 1)
        print(x[idx])
print_rev(l, 0)

# which rows has maximum number of 9s
import numpy as np
import pandas as pd

l = np.random.choice(range(0,10),100*20)
df = pd.DataFrame(l.reshape(100,20))
df["count_nine"] = df.apply(lambda x: sum(x==9), axis = 1)
df["count_nine"].sort_values(ascending=False).head(1)

# Find number of negative entries in each row of matrix
l = np.random.choice(range(-5,5+1),100*20)
df = pd.DataFrame(l.reshape(100,20))
df["count_negative"] = df.apply(lambda x: sum(x<0), axis = 1)
df["count_negative"].sort_values(ascending=False).head(1)

