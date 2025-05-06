my_list = ["apple", "banana", "carrot", "dragonfruit"]
my_list 

##################### enumerate ##################### 
enumerate(my_list)
type(enumerate(my_list)) # enumerate
e1_list = list(enumerate(my_list)) # list of tuples returned when enum converted to list
e1_list
e1_list[0]
type(e1_list[0]) # tuple

# change starting position of index from 0 to 11
list(enumerate(my_list, 11))

# loop over an enum
# prefer to use pos, element instead of a, b
for a, b in enumerate(my_list):
    # a is int, b is str
    print("###")
    print(a)
    print(type(a))
    print(b)
    print(type(b))
    
for a in enumerate(my_list):
    # b is optional 
    # if b not mentioned, a is a tuple
    print("###")
    print(a)

##################### zip ##################### 

##################### range ##################### 
list(range(10))
[x for x in range(10)]
[range(10)] # weird, avoid.

##################### itertools ##################### 

##################### more-itertools ##################### 


##################### if-else blocks ##################### 
x = 4
x = 5
x = 10
if(x>5):
    print("greater than five")
elif(x<5):
    print("less than five")
elif(x==5):
    print("equals five")    
# else if does not work, use elif


age = list(range(10,51,10))
['young' if x < 15 else 'old' for x in age]
['young' if (x < 15) else 'middleage' if (x < 35) else 'old' for x in age]
# [a if condition_1 else b if condition_2 else c for _ in _]






##################### switch ##################### 
# does not readily exist

##################### for loop ##################### 
my_num = list(range(0,51,10))
for x in my_num:
    print(x)
x

for x in my_num:
    print(x)
    if x>30:
        break

for x in my_num:
    if x==30:
        continue
    print(x)    
    
for x in range(10):
    print(x)
    del x

##################### while loop ##################### 
i = 0
while(i < 10):
    print(i)
    i = i + 1

i = 0
while 1:
    print(i)
    i = i + 1
    
    if(i==10):
        break
