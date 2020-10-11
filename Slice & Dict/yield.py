# Yield doesnt store value its wait for the next one to come

# def square_numbers(nums):
#     result=[]
#     for i in nums:
#         yield(i*i)


# my_nums=square_numbers([1,2,3,4,5,6])
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))

# my_nums=[ x*x for x in [1,2,3,4,5,6]]

my_nums=(x*x for x in [1,2,3,4,5,6])
print(my_nums)
for num in my_nums:
    print(num ,end='')