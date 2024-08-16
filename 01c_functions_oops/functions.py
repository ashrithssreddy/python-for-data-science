import math
math.pi

math.pi() # fails

###################### Return ###################### 
# returns None when no value is specified
def my_fun(a,b):
    print(a)
    print(b)    
aa = my_fun(10, 20)
print(aa) # returns None

def my_fun(a,b):
    print(a)
    print(b)    
    return
my_fun(10, 20)
aa = my_fun(10, 20)
print(aa) # returns None

# function ends when return is encountered
def my_fun(a,b):
    print(a)
    return 10000
    print(b)    
my_fun(10, 20)

# return multiple values
def my_fun(a,b):
    print(a)
    print(b)    
    return 10000, 20000, 30000 # returns a tuple
my_fun(10, 20)

def my_fun(a,b):
    print(a)
    print(b)    
    return [10000, 20000, 30000]
my_fun(10, 20)

###################### Arguement matching ###################### 
complex(3,5)
complex(real=3, imag=5)
complex(imag=3, real=5)

complex(real = 3, 5) # error: positional argument follows keyword argument
complex(3, imag=5) # allowed
complex(3, real=5) # error: 2 arguements passed for real parameter

complex(imag = 3, 5) #error: positional argument follows keyword argument
# Rule: positional first, keyword next

complex(real= 3, real= 5) # error, obviously

###################### Function calling another ###################### 
def fn_mumbai():
    print("Im in Mumbai")
    fn_bangalore()
    
def fn_bangalore():
    print("Im in Bangalore")
    fn_delhi()

def fn_delhi():
    print("Im in Delhi")
    
fn_mumbai()

###################### Function defined inside function ###################### 
del fn_mumbai, fn_bangalore, fn_delhi

def fn_mumbai():
    def fn_bangalore():
        print("Im in Bangalore")
    
    print("Im in Mumbai")
    fn_bangalore()

fn_mumbai()
fn_bangalore() # not available outside fn_mumbai()

# function can return another function
def multiplier(n):    
    def temp(x):
        return x*n    
    return temp

multiplier_2 = multiplier(2)
multiplier_2(10)
multiplier_3 = multiplier(3)
multiplier_3(10)

###################### missing arguements ###################### 
def my_fun(x, y):
    print(x)
    
my_fun(10, 20) # works
my_fun(10) # fails

###################### default values ###################### 
def my_fun(x, y= 1000):
    print(x)
    print(y)
    
my_fun(10, 20) # works
my_fun(10) # works too, uses default


###################### scoping ###################### 
for iii in dir():
    if not iii.startswith("_"):
        del globals()[iii]
    del iii

# block 1
def f1(a,b):
    print(dir())
    print(a)
    print(b)

a = 10
b = 20
[x for x in dir() if not x.startswith("_")]
print(a)
print(b)
f1(a=100, b=200)
print(a)
print(b)

# block 2 - local variable, local values
def f1(a,b):
    print(dir())
    print(a)
    print(b)
    x = 999
    print(x)

x = 100
f1(a = 10, b=20)
print(x)

# block 3 - if a variable is absent in function, look one level above
def f1(a,b):
    print(dir())
    print(a)
    print(b)
    print(x)

x = 100
f1(a = 10, b=20)
print(x)

###################### recursion ###################### 
def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)
for i in range(10):
    print(i, factorial(i))


def fibonacci(n):
    
    assert isinstance(n, int)
    assert n>=0
    
    
    if n==0 or n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(100):
    print(i, fibonacci(i))

###################### Lambda function ###################### 
my_fun = lambda a : a + 10
my_fun(5)

###################### map ###################### 
list(map(lambda a : a + 10, [1,2,3,4,5]))

my_fun = lambda a : a + 10
list(map(my_fun , [1,2,3,4,5]))

    
