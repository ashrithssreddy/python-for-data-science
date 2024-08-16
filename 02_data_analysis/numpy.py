import numpy as np


############################## Creating Arrays  ##############################
np.array([1,2,3])
np.array(range(100))

a = np.array([1,2,3])
type(a) # numpy.ndarray
a.dtype

b = np.array([(1.5,2,3), (4,5,6)]) # , dtype = float
type(b) # numpy.ndarray
b.dtype # float64

b2 = np.array([(1.5,2,3), (4,5,6)], dtype = float) # 
type(b2) # numpy.ndarray
b2.dtype # float64

c = np.array([[(1.5,2,3), (4,5,6)],[(3,2,1), (4,5,6)]], dtype = float)
type(c) # numpy.ndarray
c.dtype # float64


np.zeros((3,4)) #Create an array of zeros

np.ones((3,4)) 
np.ones((2,3,4),dtype=np.int16) #Create an array of ones

np.arange(10,26,5)
d = np.arange(10,25,5) #Create an array of evenly spaced values (step value)
print(d)

np.linspace(0,2,9) #Create an array of evenly spaced values (number of samples)

np.full((2),7) # tuple for dimensions
e = np.full((2,2),7) #Create a constant array
print(e)

f = np.eye(2) #Create a 2X2 identity matrix
f

np.random.random((2,2)) #Create an array with random values
# np.random.random((2,2), dtype = int) # dtype not allowed?

np.empty((3,2)) #Create an empty array (garbage numbers assigned)

############################## I/O ##############################
np.save('my_array' , a)
np.savez('array.npz', a, b)
np.load('my_array.npy')


np.info(np.ndarray.dtype)

############################## Inspecting Your Array ##############################
a.shape #Array dimensions
len(a) #Length of array
b.ndim #Number of array dimensions
b.size # 3 x 2  = 6
e.size #Number of array elements
b.dtype #Data type of array elements
b.dtype.name #Name of data type
b.astype(int) #Convert an array to a different type


a==b
a[1] # returns 2. type = numpy.int32 not np.ndarray
a[a>1] # retuns array [2,3]

b_temp = np.array([(1,2,3),(1,2,4) ])
b_temp 
b_temp  == a
a == b_temp
np.array_equal(a,b) # False
np.array_equal(a,a) # True




############################## Aggregate functions ##############################
a
a.sum()
a.max()

b
b.max(axis = 0)
b.max(axis = 1)


h = a.view()
a_copy = np.copy(a)
del(h)
h = a.copy()
h


a = np.array([2,3,1])
a.sort() # sorts in place

a = np.array([2,3,1])
sorted(a) # does not solve in place, returns a copy

b_copy = np.random.random((2,3))
b_copy 
b_copy.sort() # sorts each row left to right
b_copy 


b_copy = np.random.random((2,3))
b_copy 
# sorted(b_copy)
b_copy.sort(axis=0) # sorts each row left to right
b_copy 

# flatten
np.array([[1, 2, 3], [2, 4, 5], [1, 2, 3]])
np.array([[1, 2, 3], [2, 4, 5], [1, 2, 3]]).flatten()
np.array([[1, 2, 3], [2, 4, 5], [1, 2, 3]]).flatten(order = "F")

np.array([[1, 2, 3], [2, 4, 5], [1, 2, 3]]).reshape([1,9])
np.array([[1, 2, 3], [2, 4, 5], [1, 2, 3]]).reshape((1,9))

######## Slice and Dice #####
a = np.array([1,2,3,4,5,6,7])
a[2]
a[a>1]
a
a[0:2]
a[:4]
a[::-1]
a[5:0:-1]
# a.rev

b
b[1,2]
b[b<3]
b[:,2] # same as b[...,2]

############################## Array Manipulation ##############################
b
b.T
np.transpose(b)


a = np.array([1,2,3])
a
b
g = a-b

b.ravel()
g.reshape(3,2)
g.reshape(3,-2)


h = a.copy()
# h.resize((2,6))
h.resize((6,2))
h

h
g
np.append(h, g)

a = np.array([1,2,3])
a = np.insert(a,1,5) # returns a copy, not in place
a
a = np.delete(a, 1)
a



############################## Concatenate ##############################
a
d
np.concatenate((a,d),axis=0)
np.concatenate((a,d),axis=1)

a
b
np.vstack((a,b))

np.vstack((a,a)) # stack them vertically, one below the other
np.c_[a,a] # stack them as columns

np.hstack((a,a)) # stack them hori, one besides the other
np.r_[a,a] # ?


a
d
np.concatenate((a,d),axis=0)

a
b
np.vstack((a,b))

e
f
np.r_[e,f]
np.vstack((e,f))

np.hstack((e,f))

a
d
np.column_stack((a,d)) # same as np.c_[a,d]

a
np.hsplit(a,3)

c
np.hsplit(c,2)


