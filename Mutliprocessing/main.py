import multiprocessing
import time
import concurrent.futures

start = time.perf_counter()


def do_something(sleep):
    print(f'Sleeping {sleep} second(s)...')
    time.sleep(sleep)
    return f'Done Sleeping...{sleep}'



# with concurrent.futures.ProcessPoolExecutor() as executor:
#     f1=executor.submit(do_something,1)
#     print(f1.result)

if __name__ == "__main__":   
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs=[10,2,34,5,6]

        results= executor.map(do_something,secs)

        # for result in results:
        #     print(result)


        # result=[executor.submit(do_something,sec) for sec in secs ]

        # for f in concurrent.futures.as_completed(result):
        #     print(f.result())


        # f2=executor.submit(do_someth ing,2)

        # print(f1.result())
        # print(f2.result())





    # p1= multiprocessing.Process(target=do_something)
    # p2= multiprocessing.Process(target=do_something)
    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()
    # proccesses=[]
    # for _ in range(10):
    #     p1= multiprocessing.Process(target=do_something,args=[1.5])
    #     p1.start()
    #     # p1.join()
    #     proccesses.append(p1)

    # for proccess in proccesses:
    #     proccess.join()





# with concurrent.futures.ProcessPoolExecutor() as executor:
#     secs = [5, 4, 3, 2, 1]
#     results = executor.map(do_something, secs)

#     for result in results:
#         print(result)

finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')


# from multiprocessing import Process
# import time
# # from dask import Client

# def func1():
#     print("Func 1 called.")
#     time.sleep(1)
#     print("1 sec later, func 1 ended.")

# def func2():
#     print("Func 2 called.")
#     time.sleep(2)
#     print("2 sec later, func 2 ended.")

# if __name__ == "__main__":
#     f1 = Process(target=func1())
#     f2 = Process(target=func2())
#     f1.start()
#     f2.start()