def logged(function):
    # print(function,' check')
    def wrapper(*args, **kwargs):
        value=function(*args, **kwargs)
        with open('logfile.txt','a+') as f:
            fname=function.__name__
            f.write(f"{fname} returned {value}\n" )
            print(f"{fname} returned {value}\n" )
        return value
    return wrapper

@logged
def add(x,y):
    # print(x+y)
    return x+ y

print(add(10,11))