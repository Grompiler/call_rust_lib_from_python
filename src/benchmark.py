from datetime import datetime

def time_it(name: str):
    def time_it_inner(fn):
        def inner(*args):
            print("------------------------------")
            print(f"> STARTING {name} {fn.__name__}")
            start = datetime.now()
            r = fn(*args)
            end = datetime.now()
            print(f"> ELAPSED TIME: {end-start}")
            return r
        return inner
    return time_it_inner
