# - Merge 2 vectors at alternate positions (DO NOT USE LOOPS)
# - merge 11,13,15 and 12,14,16 into 11,12,13,14,15,16

#### Question 2: 
# - Collect elements at odd and even positions into 2 seperate vectors (DO NOT USE LOOPS)
# - i.e. split c(11,12,13,14,15) into 11,13,15 and 12,14

#### Question 6:
# - Rotate a vector with data in groups of 3   
# - i.e. 1 2 3 4 5 6 7 8 9 becomes 3 2 1 6 5 4 9 8 7  
# - and  1 2 3 4 5 6 7 8   becomes 3 2 1 6 5 4 8 7  
# - There are multiple cells for multiple inputs, ensure your code works fine for all use cases

# datatypes - container sequences

# containers - list
# mutable, ordered, indexable
l = ["apple","banana","carrot"]
l.append("gauva")
l

l[-1] # last element
l[-2] # second last

l = list("abcdefghij")
l[0:4]
l[0:4:1]
l[0:4:2]
l[0:5:2]

l[0:5][::-1]

l[0:-2] # 0 through last 2
l[0:0]
l[:4] # same as l[None:4]

l[0:4] # is same as 
l[0:-6]  # treat -6 as length(x)-6



l[::-1]
l[0:10:-1] # fails

l[10:0:-1] # works
# 10, 10-1, 10-1-1, ..., 
# if positive step used, start < stop
# if negative step used, start > stop

l[0:7][::-1] # most convenient way of getting in reverse

l[0:2] = ["aa","bb"]
l
l[0:2] = ["a","b"]
l

l.reverse() # reverses in place, not recommended
l

a = ["dog"]

l + a
l
a

l.extend(a) # a is a list, not a single string
l
a

l.extend(a)
l

# index of first occurence
l.index("dog")
l

# index of all occurences, always returns a list given its a list comprehension
[pos for pos, elem in enumerate(l) if elem=="dog"]
# or 
[pos for pos in range(len(l)) if l[pos]=="dog"]
# or itertools?

l = ['apple', 'banana', 'carrot', 'gauva', 'dog', 'dog']
l.pop(1) # remove element by an index
l

for pos in [1,2]:
    l.pop(pos)
l

# repeat lists
[11] * 3
[11, "apple"] * 3
[11, "apple"] * 3

# repeat each element of a list 3 times
[item for item in [11,"apple"] for n in range(3)]

l1 = [11,12,13]
l1[0] = [111, 112 ,113]
l1 # list of lists

l1 = [11,12,13]
l1[0:1] = [111, 112 ,113]
l1 # list of lists

# all elements except one
l1 = list("abcdefghij")
l1
l1[-1] # this gives the last one, not except one
[elem for pos, elem in enumerate(l1) if pos not in [2-1,4-1]] # works

# index by boolean - Not allowed
l1 = list("abcdefghij")
# l1[[2,3,4]] # fails, cannot index multiple elements
indices = [pos for pos, elem in enumerate([True, False] * 5) if elem==True]
[l1[index] for index in indices]


# filter a list
l = list(range(11,20))
l
list(filter(lambda x: x>15, l))
[x for x in l if x>15]

# what is map()
l = [1,2,3,4,5]
list(map(lambda x: x+100, l))

# what is reduce()
from functools import reduce
reduce(lambda x, y: x+y, [1,2,3,4,5,6])

list(range(11,20))
list(range(11,20,2))
# 11:15, not allowed

[x for x in [11,12,13,14,15] if x == 13]
[pos for pos, elem in enumerate([11,12,13,14,15]) if elem%2==1] # same as which(x%%2==1)

"y" in list("python")
"l" in list("python")


# recycle a list to a length
l1 = [1,2,3]
q, r = divmod(desired_length, len(l1))
l1*q + l1[:r]

# sorted - returns a value, not in place modification
l1=[1,2,3,4]
l2=[10,10,20,20]
[x+y for x,y in zip(l1,l2)]# does not recycle, but trims the shorter list

l1=[1,2,3,4]
l2=[10,20]
[x+y for x,y in zip(l1,l2)] # does not recycle, but trims the shorter list
list(zip(l1,l2))

# order of elements? Incomplete
x = [11,13,14,15,12]
sorted(x).index(11)
sorted(x).index(13)
sorted(x).index(14)
sorted(x).index(15)
sorted(x).index(12)
[sorted(x).index(i) for i in x]

# containers - tuple
# not mutable, indexable, memory-efficient than list, pairing
# need to be unpacked and zipped

# zipping
l_a = ["a","b","c"]
l_b = ["x","y","z"]

zip(l_a, l_b) # type is zip
l_ab_zip_list = list(zip(l_a, l_b)) #list of tuples

# recycyles? Nope, plainly chops to shorter length
list(zip(["a","b","c"], ["x","y"])) 
list(zip(["a","b"], ["x","y","z"])) 

# unpacking
a = l_ab_zip_list[0]
a # a is a tuple

a, b = l_ab_zip_list[0]
# a is a string, b is a string


10,20 # always a tuple, even without brackets
(10,20)
x=10; y=20;
(x,y)
x,y
x = 10,20
x

for element in l_ab_zip_list:
    print("***")
    print(element)

for idx, element in l_ab_zip_list:
    print("***")
    print(idx)
    print(element)
    
len(l_ab_zip_list[0])

("butter","asvasdvah")
len(("butter","asvasdvah"))

("butter",) # still a tuple of length 1
len(("butter",))
type(("butter",))

("butter") # not a tuple, but a string
type(("butter"))
len(("butter")) # length 6 string


# containers - set
# mutable, unordered, unique - no duplicates allowed
# in alphabetical order always
# heterogenous

my_set = {'apple', 'banana', 'carrot'}
my_set

# typically created from a list
my_l = ['carrot','banana','apple','apple','banana','carrot']
my_set=  set(my_l)
my_set

# typically created from a list
my_l = ['carrot','banana','apple','apple','banana','carrot', 20]
my_set=  set(my_l)
my_set


my_set.add("gauva") # adds if unique, updates inplace 
my_set

my_set.add("carrot") # adds if unique, updates inplace 
my_set


my_set.update(["asd","as2"]) # pass only a list or tuple
my_set

my_set.update({"hjy","rgre"})
my_set

my_set.update("hjyiukyuyukyukyku")
my_set


# delete an element from set
my_l = ['carrot','banana','apple','apple','banana','carrot']
my_set=  set(my_l)
my_set

my_set.discard("apple")
my_set

my_set.discard("asdasd") # no error if element absent
my_set

my_set.pop() # removes arbitrary element. error if empty set
my_set

set_a = set(['a','b','c'])
set_b = set(['d','e','c'])

set_a.union(set_b)
set_a.intersection(set_b)
set_a - set_b # same as set_a.difference(set_b)
set_b - set_a



# always alphabetical? looks like it
s = {5,2,7,1,8}
s



# containers - dictionary
# iterable

# my_dict = dict()
my_dict = {}
my_dict

my_dict['key_1'] = 1
my_dict['key_2'] = 2
my_dict

my_dict['new'] = {'key_1': 1, 'key_2': 2}
my_dict

my_dict['new']

# iterate over 
for my_key in my_dict:
    print("###########")
    print(my_key)
    print(my_dict[my_key])
    
# Not allowed, only keys can be extracted as for loop    
for my_key, my_value in my_dict:
    print("###########")
    print(my_key)
    print(my_value)
    
for my_key, my_value in my_dict.items():
    print("###########")
    print(my_key)
    print(my_value)

my_dict.keys() # type: dict_keys
type(my_dict.keys())
list(my_dict.keys()) # list

my_dict.values() # type: dict_values
type(my_dict.values())
list(my_dict.values()) # list 

my_dict.get('key_1') 

my_dict['not_a_key'] # error for a missing key
my_dict.get('not_a_key') # no error thrown for a missing key

my_dict.get('not_a_key', 99999)


my_dict[2] = 1000;
my_dict

my_dict[2] # indexing by number not allowed, unless the key is a number itself

my_dict_list = list(my_dict.items()) # list of tuples

sorted({'key_1':10,'key_3':20,'key_2':15}) # returns sorted keys, not valuess
{'key_1':10,3:20,'key_2':15} # allowed heterogenous datatype for keys
sorted({'key_1':10,3:20,'key_2':15}) # avoid heterogenous datatype for keys

# update dict
my_dict = {}
my_dict['key_1'] = 1
my_dict['key_2'] = 2
my_dict
my_dict.update({'key_3': 1000})
my_dict

my_dict.update({'key_1': 999}) # adds a new key-value pair if key not present, updates if key already present
my_dict

my_dict.update({'key_4': 999}) # adds a new key-value pair if key not present, updates if key already present
my_dict

del my_dict['key_4']
my_dict

my_dict.pop('key_3')
my_dict


my_dict.get('key_1')
my_dict.get('key_999') # no error for bad key
my_dict['key_999'] # error for bad key

'key_1' in my_dict # check for presense of a key
'key_000' in my_dict 
# same as 
'key_1' in my_dict.keys()
'key_000' in my_dict.keys()

############################################################### containers - collections ###############################################################
from collections import Counter

l = ['a','b','c','b','a']

c1 = Counter(l)
c1
type(c1) # collections.Counter
dict(c1)

c1.most_common(2)
type(c1.most_common(2)) # list of tuples
c_temp = c1.most_common(2)
[x[1] for x in c_temp]

############################################################### containers - zip ###############################################################
nums = [1, 2, 3, 4]
fruit = ["Apples", "Peaches", "Pears", "Bananas"]

z1 = zip(nums, fruit) # datatype: zip


############################################################### junk ###############################################################
x = 10
y = 20
print(x,y) # type is NoneType

print(f"x is {x}")


import csv

csvfile = open("mtcars.csv", "r")
for row in csv.reader(csvfile):
    print("")
    print(row)

csvfile.close()

