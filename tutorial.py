# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 18:30:43 2020

@author: econo
"""
#%%
x1 = 5
type(x1)
print(type(x1))
x2= 4.75
print(type(x2))
int(x2)
print(int(x2))
x3= True
print(type(x3))
y= 10
print (str(y) +  " dollars")
16/3
16%3
x= 5**3
print(x)
x== 125
##Line continuation
2*5+ \
5
##Indexation
"Friday"[3]
#Identation
def five(x):
    x= 5
    return x
print(five(3))
#basic if function
x=1
if x>3:
    print("Good")
else:
    print("Bad")
#%%
#List, Tuples and Sets

courses = ['History', 'Math','English', 'CompSci']
courses2 = ['Art', 'Spanish']
courses.extend(courses2) # adding to a list
print(courses)
courses.reverse() #from last to first
print(courses)
courses.sort() #ascending order
print(courses)
courses.sort(reverse = True)#descending order
print(courses)
popped = courses.pop()# remove the last item in the list
sorted_courses = sorted(courses) #a sorted list from ascending order
print(courses)
print(courses.index('History'))
#print(sorted_courses)
#print('Art' in courses) #Check to see if the subject is in the list
for index, item in enumerate(courses, start = 1): #indexing a For loop with starting number
    print(index,item)
courses_str =', '.join(courses) #separate the list with a comma
print(courses_str)
cs_courses = {'History','Math','Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}
#print(cs_courses.intersection(art_courses))# What two sets have in common
#print(cs_courses.difference(art_courses)) What courses they dont have in common
#print(cs_courses.union(art_courses)) Combining sets
#%%
#Dictionaries

student = {'name': 'Alex', 'age': 25, 'courses': ['Math, Compsci']}
student['phone'] = '555-5555' # adding a key with a value
print(student['name']) # get the value from a specified key
student.update({'name':'John','age':31,'phone':'234-1234'})# updating multiple keys with respective value
print(student.get('phone'))# retrieving the value from a specified key and returning 'None' if it is not there
print (student.get('phone', 'It nuh deh deh'))
#age = student.pop('age')# deleting a key and its value
print(student.items())# gives us keys and values
print(student.keys())
print(student.values())
for key, value in enumerate(student.items(), start = 1):
    print( key, value)
    #%%
#Conditionals and Booleans, If, Else, and ELIF Statements

user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('It good')
else:
    print('It nuh good')

user = 'Admin'
logged_in = False

if user == 'Admin' and logged_in:
    print('It good')
else:
    print('It nuh good')

user = 'Admin'
logged_in = False

if user == 'Admin' or logged_in:
    print('It good')
else:
    print('It nuh good')

#%% Loops and Iterations

nums = [1,2,3,4,5]

for num in nums:
    if num == 3:
        print('Found it!')
        break
    print(num)

nums = [1,2,3,4,5]

for num in nums:
    if num == 3:
        print('Found it!')
        continue
    print(num)

for i in range(1,11):
    print(i)

x= 0
while x<10:
    if x ==5:
        break
    print(x)
    x+= 1

x= 0
while True:
    if x ==5:
        break
    print(x)
    x+= 1
#%%  Directory

import os
print(os.getcwd())

#%% Pandas

import pandas as pd

df = pd.read_excel('prudentials.xlsx')
df.info   
df.columns
df.iloc[23]    #integer location
df.set_index( 'name of column', inplace= True) #changing index
df.reset_index(inplace= True) #reset index
df.sort_index() #sort index
df.sort_index(ascending=False)

#%%
import datetime
import pytz
 
d = datetime.date(2009, 7, 24)
print(d)
tday= datetime.date.today()
print(tday)
print(tday.year)
print(tday.isoweekday())
tdelta = datetime.timedelta(days = 7)
print(tday + tdelta)
bday = datetime.date(2020, 9, 23)
tilbday = bday -tday
print(tilbday.days)
 #%% Real time Data
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time
 
 
api_key = 'Q7N86VBT9XLF99LY'
ts = TimeSeries(key = api_key, output_format = 'pandas')
data, metadata = ts.get_intraday(symbol = 'MSFT', interval = '1min', outputsize = 'full')
print(data)
 
i= 1
while i==1:
     data, metadata = ts.get_intraday(symbol = 'MSFT', interval = '1min', outputsize = 'full')
     data.to_excel("output.xlsx")
     time.sleep(60)
     
#%% Learning Pandas
import pandas as pd
import numpy as np
 
array_to_square = np.arange(0, 5)
 #%timeit array_to_square**2
print(array_to_square**2)
 
a1= np.array([1,2,3,4,5])
print(type(a1))
np.size(a1)
a3 = np.array([0]*3) # print 0 3x
print(a3)
 
np.array(range(10)) #list the numbers from 0 to 9
np.arange(0, 10) # list the numbers from 0 to 9
np.arange(10) # list the numbers from 0 to 9
np.zeros(10) # gives you 10 zeros
np.arange(0,10,2) #gives you the range of numbers with an increment of 2
np.arange(10,0,-1) #counitng down from 10 to 0, but we stop at 1
a2 =np.arange(0,10)
a2*2 # multiply each number by two
m = np.arange(0,20).reshape(5,4) #reshape from a 1x20 to a 5x4
print(m)
np.size(m) # number of elements
np.size(m,0) # number of rows
np.size(m,1) # number of columns
m[1,2]
m[1,] # all items in row 1
m[:,2] #all items in column 2
a = np.arange(5)
print(a)
a <= 2 #Boolean results
(a<2) | (a > 3) # Conditional Boolean
def exp(x):
     return x<3 or x>3
np.vectorize(exp)(a) #apply the function to all itmes in the array
r = a < 3 #Boolean select items less than 3
a[r]
np.sum(a<3) #counts the amount of items are less than 3; True =1 , False= 0
a1 = np.arange(1,10)
a1[3:8]
a1[::2] #every other item
a1[::-1] #reverse order
m[:,1:3] # all columns starting from position 1 excluding 3
m[[1,3,4],:] # rows 1, 3 and 4, and all columns
a =np.arange(9)
print(a)
m = a.reshape(3,3)
print(m)
raveled = m.ravel()
print(raveled)
reshaped = m.reshape(np.size(m))
print(reshaped)
a = np.arange(9).reshape(3,3)
b= (a+1)*10
print(a)
print(b)
np.hstack((a,b))
np.vstack((a,b))
a = np.arange(12).reshape(3,4)
np.hsplit(a,4)
np.hsplit(a,2)
 #%% Series Object
 
import numpy as np
import pandas as pd
 
pd.set_option('display.notebook_repr_html', False)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 10)
 
s1 = pd.Series(2)
print(s1)
 
s2 = pd.Series([1,2,3,4,5])
print(s2)
s2.values
 
s3= pd.Series([1,2,3], index = ['a','b','c']) #creating an index
print(s3)
 
s4 = pd.Series(2, index= s2.index)
print(s4)
 
np.random.seed(123456)
pd.Series(np.random.randn(5))
 
 #create series from dict
s6= pd.Series({'a':1,'b':2,'c':3})
print(s6)
 
s=(pd.Series([0,1,1,2,3,4,5,6,7, np.nan]))
print(s)

s3[['a', 'c']] #multiple items
 
s5 = pd.Series([1,3,2,4,5], index = np.arange(1,6,1))
print(s5)
 
s5[3] #search by index
s5.iloc[1] #search by position
s5.loc[[4,5]] #search by multiple index location
s5.iloc[[2,4]] #search by multiple position
 
s6 = pd.Series([1,2,3,4], index= ['a','b','c','d'])
s6
 
s7 =pd.Series([4,3,2,1], index = ['d','c','b','a'])
s7

data= pd.Series(np.arange(2,9))
data2= pd.Series(np.arange (3,10))
combined = pd.concat([data,data2])
combined.index = np.arange(0,len(combined))
pd.DataFrame({'numbers':combined})
print(combined)
d=pd.DataFrame({'num1':data, 'num2':data2})

diff = d['num1'] -d['num1'].shift(-1)
print(diff)

num = 3
num2 = 5
if num > num2:
    print('yes')
else:
    print('no')
 
s6+s7 # adding Series together with the same indexes
nda= np.array([1,2,3,4,5])
nda.mean()
 
nda = np.array([1,2,3,4,np.NaN])
nda.mean()
 
s =pd.Series(nda)
s.mean() #ignores NaN
 
s = pd.Series(np.arange(0,10))
s>5 # Boolean Results
 
LogicalResults = s>5
s[LogicalResults] #Select rows that are greater than 5
s[s>5] # Same as above
 
s[(s>5) & (s<8)]
 
s1= pd.Series(np.random.randn(3))
s2= pd.Series(np.random.randn(3))
combined = pd.concat([s1,s2])
print(combined)
combined.index = np.arange(0, len(combined))
print(combined)
 
s3 = pd.Series(['red', 'green', 'blue'], index = [0,3,5])
s3
 
s3.reindex(np.arange(0,7), method='ffill') #repeat last known index value
s3.reindex(np.arange(0,7), method='bfill') # repeat the next index value
 
 #%% DataFrames
import numpy as np
import pandas as pd
 
print(pd) 
 
df = pd.DataFrame(np.array([[0,1], [2,3]]), columns = ['c1','c2'], index =['r1','r2'])

s1 = pd.Series(np.arange(1, 6, 1))
s2 = pd.Series(np.arange(6, 11, 1))
pd.DataFrame({'c1': s1, 'c2': s2})

# read Sp500 file , use Symbol as index column and specify which columns to use
sp500 =pd.read_csv('sp500.csv', index_col = 'Symbol', usecols =[0,2,3,7])

sp500.head()

one_mon_hist = pd.read_csv("omh.csv")
one_mon_hist.head() # first five rows of data
one_mon_hist[:3] # first 3 rows of data
one_mon_hist.loc[[1,2]] #rows 1 and 2
sp500.Price.head() #Price data of the first 5 ticker/Symbols
sp500.Sector.head() #Sector data of the first 5 ticker/Symbols
sp500[['Price','Sector']].head() #getting data of Price and Sector columns

sp500[['Price']].head()
sp500.loc['MMM'] #identifying a ticker and the respective info is shown
sp500.loc[['ACE','ABBV']] #identifying multiple tickers and the respective info shown
sp500.iloc[[1,2]]# get info in positions 1 and 2 
sp500.at['MMM','Price'] #by label and column
sp500.Price<100
sp500[sp500.Price<100]
sp500[(sp500.Price<10) & (sp500.Price>0)] [['Price','Book Value']] # get only the Price where Price is <10 and >0 
df =sp500.rename(columns = {'Book Value': 'BookValue'}) #renaming columns
df =sp500.rename(columns = {'Book Value': 'BookValue'}, inplace = True) #permanently change/modify the column
df.head(2)
sp500.columns
a = sp500.index.get_loc('MMM') #get row index location
b = sp500.index.get_loc('A') #get row index location
f"{a}, {b}" #new formatting technique
copy = sp500.copy() #copy a datadrame
copy['TwicePrice'] = sp500.Price*2 #adding  new column
copy[:2] #first two rows of dataframe

r = sp500[(sp500.Price<10) & (sp500.Price>0)] [['Price']]
print(r)

copy = sp500.copy()
copy.insert(1,'TwicePrice', sp500.Price*2)  #adding the new column at a different location
copy[:2]
sp500[:3][['Price']] # first 3 rows from the price column
rcopy = sp500[:3][['Price']].copy() #subset of a dataframe
s = pd.Series ({'MMM': 'Is in the Dataframe', 'MSFT': 'Not in the Dataframe'})
rcopy['Comment'] = s
rcopy.head()

copy = sp500.copy()
copy.Price = sp500.Price*2 #replacing the contents of a column
copy.head()
copy.at['MMM', 'Price'] = 200 #changing a scalar value in the dataframe
copy[:5]
copy =sp500.copy()
del copy['Book Value'] #deleting a column
copy.head()

#Adding a Column
df = sp500.copy()   
df.insert(1, 'The One', pd.Series(1, index=df.index)) 
df.head()


#Adding rows to a dataframe
df1 = sp500.iloc[:3].copy()
df2 = sp500.iloc[[10,11,12]].copy()
combined = df1.append(df2)
combined.head()

#Adding a new row to the dataframe
ss = sp500[:3].copy()
ss.loc['Foo']= ['the sector', 100, 110]
ss.head()

#Deleting a row
sp =sp500.copy()
drop = sp.drop(['MMM','ABBV']) #drop a row
afterdrop = sp.drop(['Sector'], axis =1) #drop column by using axis =1
afterdrop.head()
drop.head()

#Using Boolean to create a sub dataframe
selection = sp500.Price>300
f"{len(selection)}, {selection.sum()}"
c = sp500[~selection]
print(c)

np.random.seed(4321)
df = pd.Dataframe(np.random.rand(5,4), columns = ['A','B','C','D'])
print(df)

reindexed = sp500.reset_index()
multi_fi = reindexed.set_index(['Sector', 'Symbol']) #multi_index
type(multi_fi.index)
print(multi_fi)
print(multi_fi.index)
multi_fi.index.levels[0] #shows all sectors
multi_fi.index.levels[1]# shows all tickers/symbols
multi_fi.xs('Industrials') #show all industrial stocks
multi_fi.xs('ALLE', level = 1, drop_level = False)
multi_fi.xs('Industrials', drop_level = False)
multi_fi.xs(('Industrials','UPS'))

one_mon_hist.mean() #mean in each column
one_mon_hist.mean (axis = 1) #mean for each row
one_mon_hist[['MSFT', 'AAPL']].idxmin() #location for the min value for both stocks
one_mon_hist[['MSFT', 'AAPL']].idxmax() #location for the min value for both stocks
one_mon_hist.describe()

msft =pd.read_csv('msft.csv', index_col = 'Date')
msft.head()

msft2 = pd.read_csv('msft.csv', header=0, index_col =0, names=['open','high','low','close','volume'])
msft2.head() # header= 0 tell the program that the first row is the title row

df = pd.read_csv('msft.csv', index_col = ['Date'], usecols =['Date','Close'])
df.head()