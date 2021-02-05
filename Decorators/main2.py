import time


def times(function):
    def wrapper(*args,**kwargs):
        before=time.time()
        value=function(*args,**kwargs)
        after=time.time()

        fname=function.__name__
        print(f"{fname}  took {after-before} seconds to executes")

        return value

    return wrapper


@times
def myFunction(X):
    result=1
    for i in range(1,X):
        result +=i
    return result



print(myFunction(1000000))