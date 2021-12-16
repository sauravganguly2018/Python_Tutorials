import time
from functools import lru_cache

@lru_cache(maxsize=3)
def some_work(n):
    time.sleep(n)
    return n

if __name__=='__main__':
    print("Now calling the function")
    some_work(3)
    some_work(1)
    some_work(4)
    some_work(2)
    print("Done calling the function")
    some_work(3)
    print("called again")

