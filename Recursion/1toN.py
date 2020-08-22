
# def fun(n):
#     if (n==1):
#         print(n) 
#         return 
#     print(n)   
#     return fun(n-1)
# fun(10)

def fun(n):
    if (n==10):
        print(n) 
        return 
    print(n)   
    return fun(n+1)
fun(1)