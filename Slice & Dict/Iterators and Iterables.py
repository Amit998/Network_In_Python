# nums=[12,3,4,5]
# for num in nums:
#     print(num)
# i_nums=nums.__iter__()
# i_nums=iter(nums)

# while True:
#     try:
#         item=next(i_nums)
#         print(item)
#     except  StopIteration:
#         break

# print(i_nums)
# print(next(i_nums))
# print(dir(nums))


class MyRange:
    def __init__(self,start,end):
        self.val=start
        self.end=end
    def __iter__(self):
        return self
    
    def __next__(self):
        if (self.val>= self.end):
            raise StopIteration
        current=self.val
        self.val+=1
        return current

def my_range(start,end):
    current=start
    while current < end:
        yield current
        current += 1

nums=my_range(1,10)
for num in nums:
    print(num)
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))