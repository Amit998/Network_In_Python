# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary

a={
    1:"amit",
    1:"amit",
    2:'Dutta',
    2:'lol',
    3:'Dip'
}
a[2]='Rajnikant'
a[4]='Dhoni'
print(a)
# print(a.clear())
b=a.copy
print(b)
print(a.values())
print(a.items())
print(a.keys())
print(a.pop(2))
print(a)
print(a.popitem())
print(a)

print(a.setdefault(1))
myDictonary=dict(key1='amit',key2='Koel')
print(myDictonary)
a={1:2,2:4,3:4}
print(a.fromkeys(myDictonary))


squad={
    'Batsman':{
        'Rohit Sharma':{
            'Match':200,
            'Avvg':50,
        },
        'Shikhar Dhawan':{
            'Match':200,
            'Avvg':50,
        },
        'Virat Kohili':{
            'Match':200,
            'Avvg':50,
        }
    },
    'All-Rounder':{
        'Hardik Pandeya':{
            'Match':200,
            'Avvg':50,
        },
        'Ravi Dhawan':{
            'Match':200,
            'Avvg':50,
        },
        'Virat Patel':{
            'Match':200,
            'Avvg':50,
        }
    },
}
import pandas as pd
df1=pd.DataFrame(squad['Batsman']['Rohit Sharma'],index=[1])
print(df1)

myList=[1,1,2,3,3,2,1,3,45,4,3]
myList=list(dict.fromkeys(myList))
print(myList)