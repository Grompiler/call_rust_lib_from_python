from datetime import datetime

def time_it_rs(fn):
    def inner(*args):
        print("------------------------------")
        print(f"> STARTING RS {fn.__name__}")
        start = datetime.now()
        r = fn(*args)
        end = datetime.now()
        print(f"> ELAPSED TIME: {end-start}")
        return r
    return inner

def time_it_py(fn):
    def inner(*args):
        print("------------------------------")
        print(f"> STARTING PY {fn.__name__}")
        start = datetime.now()
        r = fn(*args)
        end = datetime.now()
        print(f"> ELAPSED TIME: {end-start}")
        return r
    return inner
