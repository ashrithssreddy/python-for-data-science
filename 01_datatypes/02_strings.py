################################### Datatype ###################################
x = "apple"
type(x)
len(x)
x[0]


x = ["banana","apple","carrot"]
type(x)
len(x)
x[0]


x = ["banana","apple","carrot"]
set(x)
list(set(x)) # order changed

x = ["banana","apple","carrot"]
max(x)
min(x)
len(x)


sorted(x) # returns a value
x.sort() # in place
x

type(x) == list # True
type(x) is list # True

"apple" + "banana"
" ".join(["apple", "banana"])

l1 = ["apple","banana"]
l2 = ["carrot","dragonfruit"]
[a + b for a, b in zip(l1, l2)]

"apple".upper()
"APPLE".lower()
"APPLE A day doctoR away".title()

"APPLE A day doctoR away".replace("apple","--")
"apple a day doctoR away".replace("apple","--")
"apple a day doctoR away apple".replace("apple","--")

# replace only the first n instances?

# string extract all or some instances?

len("apple")

l = "abcdefghijklmnopqrstuvwxyz"
l[2:2]
l[2:3]
l[2:10]
l[2:10:2]

many_strings = ["north carolina","south carolina","new hampshire","north dakota"]


"north carolina".find("carolina")
"new hampshire".find("carolina") # -1 means not found
[x.find("carolina") for x in many_strings] # return position of match
[x for x in many_strings if x.find("carolina")>0] # return value that matches

[pos for pos, x in enumerate("hawaii") if x=="i"]
[pos for pos, x in enumerate("mississippi") if x=="s"]


"welcome to hotel california".split(" ")


# puzzle: identify strings with alternating letter?





################################### re package ###################################
import re

txt = "The rain in Spain"
re.findall("ai", txt)



################################### String Modification - Position ###################################
s = list("an apple")
s[0:0] = list("a banana and ")
"".join(s)

################################### String Modification - Pattern ###################################

################################### Substring Search - RegEx ###################################




################################### Assignments ###################################
## remove duplicates in a string, maintain order
s = "an apple a day keeps doctor away"

# list(s)
# "".join(set(s))

unique = []
[unique.append(x) for x in s if x not in unique]
# [unique.append(x) for x in s if x not in unique or x== " "]
"".join(unique)

"".join(list(dict.fromkeys("an apple")))

## common characters in 2 strings?
s1 = list("tell")
s2 = list("late")

## check if a string is palindrome
s = "nitin"
s == s[::-1]

## check if 2 strings are anagrams
from collections import Counter
s1 = "talee"
s2 = "latee"
c1 = Counter(s1).most_common()
c2 = Counter(s2).most_common()
c1
c2
# sorted(s1) == sorted(s2) # works too


## Remove first 3 duplicates of a string
# e.g. abbabbaaccccab should become abcab
import pandas as pd
df = pd.DataFrame(list("abbabbaaccccab"))
df["temp"] = df.groupby(0, as_index = False).cumcount()+1
df[(df["temp"]<=1) | (df["temp"]>=5)][0].tolist()
"".join(df[(df["temp"]<=1) | (df["temp"]>=5)][0].tolist())
