############################## Create a Series/DataFrame ##############################
import pandas as pd

pd.Series([3,-5,7,4])
pd.Series([3,-5,7,4], index = [11,12,13,14])
s = pd.Series([3,-5,7,4], index = ["a","b","c","d"])

s.drop(["a"]) # returns a value not inplace. Inplace = F by default

df = {
      "country" : ["belgium","india","brazil"],
      "capital" : ["brussles","delhi","brasilia"],
      "population":[10,30,20]      
      }
df = pd.DataFrame(df)
df

df.drop(1)
df.drop([1,2])

df.drop("capital", axis=1)
df.drop(["capital","country"], axis=1)




############################## Sorting ##############################
mtcars = pd.read_csv("data\\mtcars_rownames.csv", index_col = "Unnamed: 0")
mtcars = pd.read_excel("data\\mtcars_rownames.xlsx", index_col = "Unnamed: 0")

df
df.sort_values(by="country")
df.sort_values(["country"])
              
mtcars.sort_values(["cyl","vs","am","drat"])
mtcars.sort_index()

mtcars = pd.read_csv("data\\mtcars_rownames.csv", index_col = "Unnamed: 0").head(5)
iris = pd.read_csv("data\\iris_rownames.csv", index_col = "Unnamed: 0").head(5)

############################## Selecting df - row and column position ##############################
# give integer row positions and column positions only
mtcars.iloc[1,1] # int
mtcars.iloc[1,:] # series, regardless of datatypes inside the series, colon optional
# iris.iloc[:1] # first row, not recommended due to complexity of syntax
iris.iloc[[1],:] # DataFrame, and not a series since the inputs is list and not vector

mtcars.iloc[:,1] # series, regardless of datatypes inside the series, colon mandatory

mtcars.iloc[[1,2] ,[1,2]] # DataFrame
mtcars.iloc[: ,[1,2]] # DataFrame

mtcars.iat[1,1] # int, iat needs both x and y position, not recommended to use
# mtcars.iat[1,] # do not work
# mtcars.iat[:,1] # do not work
# mtcars.iat[[1,2] ,[1,2]] # do not work
# mtcars.iat[: ,[1,2]] # do not work
 
############################## Selecting df - by row and column label ##############################
# Input row names and column names only
mtcars.loc["Datsun 710","cyl"]
mtcars.loc["Datsun 710",] # series, colon optional
mtcars.loc["Datsun 710",:] # series, colon optional
# mtcars.loc[,"cyl"] # series, colon mandatory
mtcars.loc[:,"cyl"] # series, colon mandatory
# mtcars.loc[4,"cyl"] # failed, no rowname called 4
# mtcars.loc["Datsun 710","2"] # failed, no colname called 2

############################## Selecting df - by row and column label/position ##############################
# stopped working in newer version

############################## Selecting df - by boolean ##############################
mtcars.cyl # dtype int, type series 
type(mtcars.cyl)
(mtcars.cyl).dtypes

mtcars.cyl > 4 # dtype boolean, type series
type(mtcars.cyl > 4)
(mtcars.cyl > 4).dtypes

mtcars[mtcars.cyl > 4]
# mtcars[some_boolean_series]

s>3 #type series, dtype boolean
s[s>3] #type series, dtype int
s[(s>3)]
s[~(s>3)]
# s[!(s>3)] # does not work, negation happens using tilde ~
s[(s>3) | (s < -3) ]


############################## Access columns  ##############################
mtcars.hp
mtcars["hp"]



# s["b"]
# df[1]
# mtcars[1]

############################## methods/metadata and functions ##############################
mtcars.shape
mtcars.index # type = pandas.core.indexes.base.Index
mtcars.columns # # type = pandas.core.indexes.base.Index
mtcars.info()
mtcars.dtypes # a series
mtcars.count() # didnt understand

df.sum() # sum by each colunm, a series
mtcars.sum()
mtcars.cumsum() # a dataframe
mtcars.min() # a series
mtcars.idxmin() # rowlabel corresponding to lowest value in each column
mtcars.describe() # summary statistics
mtcars.mean() # mean of each colunm, a series


############################## apply functions ##############################
f = lambda x: x + 1000
mtcars.apply(f)

f_mean = lambda x: x.mean()
mtcars.apply(f_mean) # mean of each column

f = lambda x: x + 1000
mtcars.applymap(f)




###################### Aggregate ###################### 
import pandas as pd
df = pd.read_csv(r"C:\Users\Ashrith Reddy\My Drive\02_learning\python\01_datatypes\mtcars.csv")

# aggregate entire dataset
f_mean = lambda x: x.mean()
df.apply(f_mean) # mean of each column, returns a series

df.groupby('am').apply(f_mean) # # mean of each column, for each group

df_grouped = df.groupby('am')
df_grouped
type(df)
type(df_grouped)
df_grouped.obj # a pandas dataframe

# all attributes of grouped dataframe
df_grouped.__dict__.keys() # same as vars(df_grouped)

f_sum = lambda x: x.mean()
temp = df_grouped.apply(f_sum)
temp # wierd behavior: aggregate the grouping column



df.groupby(['vs','am']).agg(sum).reset_index()
df.groupby(['vs','am']).agg("sum").reset_index() # quotes work for built-in functions

df.groupby(['vs','am']).agg(sum,max).reset_index() # fails
df.groupby(['vs','am']).agg(["sum","max"]).reset_index()

my_sum = lambda x: x.sum()
# df.groupby(['vs','am']).agg("my_sum").reset_index() # quotes fail for UDF
df.groupby(['vs','am']).agg(my_sum).reset_index() # no quotes preferred
df.groupby(['vs','am']).agg(lambda x: x.sum()).reset_index()

def my_sum_2(x):
    return x.sum()
df.groupby(['vs','am']).agg(my_sum_2).reset_index()

# single groupby variable, single aggregating column
df['disp'].groupby('vs') # wont work
df['disp'].groupby(df.vs) # works
df['disp'].groupby(df['vs']) # works
df['disp'].groupby(df.vs).mean() 

# multiple groupby variable, single aggregating column
df['disp'].groupby(df.vs, df.am) # fails
df['disp'].groupby([df.vs, df.am]) # works
df['disp'].groupby([df.vs, df.am]).mean().reset_index()

# multiple groupby variable, multiple aggregating column
df[['disp','hp']].groupby([df.vs, df.am]).mean().reset_index()

# extras
df.groupby(['vs', 'am']).size().reset_index()

for group, group_data in df.groupby(['vs','am']):
    print("###############")
    print(group)
    print(group_data)

# interchangable order of writing
df[['disp','hp']].groupby([df.vs, df.am]).mean() # is same as 
df.groupby([df.vs, df.am])[['disp','hp']].mean() # is same as 
df.groupby(["vs", "am"])[['disp','hp']].mean() # preferred


# multiple aggregating functions
df.groupby(["vs", "am"])[['disp','hp']].agg(max) # max applied on disp and hp
df.groupby(["vs", "am"])[['disp','hp']].agg([max,min]) # max applied on disp and hp, and min applied on disp and hp

df.groupby(["vs", "am"])[['disp','hp']].agg({'disp':'max', 'hp':'min'}) # works
df.groupby(["vs", "am"])[['disp','hp']].agg({'disp':max, 'hp':min}) # works
df.groupby(["vs", "am"]).agg({'disp':max, 'hp':min}) # works

# multiple aggregating functions - different functions for each aggregating column
df.groupby(["vs", "am"]).agg({
    'disp':max, 
    'hp':min,
    'gear':lambda x: x.max() - x.min()
    })

df.groupby(["vs", "am"]).agg({
    'disp':[max, min, lambda x: x.max() - x.min()], 
    'hp':min,    
    })

df.groupby(["vs", "am"]).agg({
    'disp':lambda x: x.max() - x.min(), 
    'hp':lambda x: x.min() - x.max(),    
    })


# rename columns after aggregating
temp = df.groupby(["vs", "am"]).agg({
    'disp':[max, min, lambda x: x.max() - x.min()], 
    'hp':min,    
    })
print(temp)
temp.columns = ['_'.join(x) for x in temp.columns]
print(temp.reset_index())


# name columns while aggregating :)
df.groupby(["vs", "am"]).agg(
    min_disp=('disp','min'),
    max_disp=('disp','max'),
    max_hp=('hp','max'),
    min_hp=('hp',min),
    range_hp=('hp',lambda x: x.max()-x.min()),  # interestingly, a comma is allowed after last aggegation
    )

# additional features
df.groupby(["vs", "am"], as_index = False).agg(
    min_disp=('disp','min'),
    )# avoid having to reset_index()

df.groupby(["vs", "am"]).agg(
    min_disp=('disp','min'),
    )# avoid having to reset_index()


############################## grouped-mutate ##############################
# import numpy as np
# df.groupby("cyl").apply(max(hp))
df.groupby("cyl")["hp"].transform("sum") 
df.groupby("cyl")["hp"].transform(sum)
df.groupby("cyl")["hp"].transform(lambda x: sum(x)/(1000 + 10))
df.groupby("cyl")[["hp","mpg"]].transform(lambda x: sum(x))

def temp_fun(x):
    # print("###########################")
    # print(x)
    answer = sum(x.vs) - sum(x.am)
    return answer

# df.groupby("cyl").transform(temp_fun)

temp = df.groupby("cyl").\
    apply(temp_fun).\
    to_frame().\
    rename(columns={0:"vs_as"}).\
    reset_index()
df.merge(temp)


# lambda x: 
# sum(x)
    # sum(x[0]-x[1])
    # print("")

# [["hp","mpg"]]
# .groupby("cyl")






############################## advanced functions ##############################
# first value, count, 
df.groupby('cyl').agg(first_disp=('disp',nth(0)))
df.groupby('cyl')["disp","hp"].nth(0)
df.groupby('cyl')["disp","hp"].nth(1)
agg(first_disp=('disp',))

nth(0)
df.nth(1)


############################## Others ##############################
df["new"] = 999
df
df["new"] = None

df.head(3)
df.tail(3)

df.shape

############################## spread and gather/pivot ##############################


############################## data alignment ##############################
s
s3 = pd.Series([100,100,100], index = ["a","c","d"])
s3 

s + s3


# replace a value in DF
mtcars = pd.read_csv(r"C:/Users/Ashrith Reddy/My Drive/02_learning/python/02_data_analysis/mtcars.csv")
mtcars.iloc[0,0] = 999
mtcars.loc[:,"newcol2"] = 999 
mtcars.loc[:,"newcol2"] = [999, 1000] # Does not recycle


mtcars.columns
mtcars.describe()
type(mtcars) == pandas.core.frame.DataFrame # Fails
isinstance(mtcars, pd.DataFrame)

mtcars_1 = mtcars[mtcars.cyl==4]
mtcars_2 = mtcars[mtcars.cyl==6]
# bind with mismatching column/row count?
pd.concat(mtcars_1, mtcars_2) # fails
pd.concat([mtcars_1, mtcars_2]) 
[mtcars_1, mtcars_2] # list of dataframes
# OR 
mtcars_1.append(mtcars_2)


mtcars_1 = mtcars.iloc[:,0:5]
mtcars_2 = mtcars.iloc[:,5:12]
mtcars_1_2 = pd.concat([mtcars_1, mtcars_2], axis = 1) # correct way
mtcars_1_2_bad = pd.concat([mtcars_1, mtcars_2], axis = 1, ignore_index=True) # screws up the column names

############################ Pending ############################ 
# apply a function to every element of data.frame
# like apply(X= mat,MARGIN=c(1,2),FUN=sqrt) # Instructs to apply sum on mat, row-wise and col-wise. i.e. on each element of matrix

# Question: Get the number of missing values in each column of credit dataset
# mat <- matrix(runif(24,-10,10),6,4) # runif generates 24 random numbers between -10 and 10
# Question: Find number of negative entries in each row of matrix


