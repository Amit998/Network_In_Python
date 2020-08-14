nums =[1,2,3,4,5,6,7,8,9,10]

my_list=[]
for n in nums:
    my_list.append(n)
print(my_list)

my_list=[n for n in nums]
print(my_list)



my_list=[]
for n in nums:
    my_list.append(n*n)
print(my_list)

my_list=[n*n for n in nums]
print(my_list)

my_list=list(map(lambda n: n*n , nums))
print(my_list)

For Even number

my_list=list(filter(lambda n: n%2 == 0,nums ))
print(my_list)


For Even number

my_list=list(filter(lambda n: n%2 == 0,nums ))
print(my_list)

I want a letter,number pair list

my_list=[]

for letter in 'abcd':
    for num in range(4):
        my_list.append((letter,num))
print(my_list)


my_list =[]


my_list=[ (n,l) for l in 'abcd' for n in range(5)]
print(my_list)


names=['A','B']
heros=['Antman','Batman']

print(list(zip(names,heros)))

my_dict={}
for name,hero in zip(names,heros):
    my_dict[name]=hero
print(my_dict)

my_dict={name : hero for name, hero in zip(names,heros) if name != 'B' }
print(my_dict)


nums=[1,1,3,3,2,2,5,6,7,8,6,4,9,8,10]
my_set=set()

for n in nums:
    my_set.add(n)
print(my_set)

my_set={ n for n in nums  }
print(my_set)

def gen_function(nums):
    for n in nums:
        yield n * n

my_gen=gen_function(nums)

for i in my_gen:
    print(i,end=' ')

my_gen= (n*n for n in nums )
print(set(my_gen))
