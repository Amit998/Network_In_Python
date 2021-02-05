def mydecorater(function):

    def wrapper(*args,**kwargs):
        
        return_value= function(*args,**kwargs)
        print("I am decorating your function!")

        return return_value
    return wrapper

# @mydecorater
# def hello(person):
#     print(f"Hello {person}")
# def hello_world():
#     print("Hello World")
# fun=mydecorater(hello_world)()


@mydecorater
def hello(person):
    print(f' this is {person}')
    return f"Hello {person}"

print(hello('Amit'))