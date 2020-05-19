import time

def benchmark(func):
    """
    Декоратор, выводящий время, которое заняло
    выполнение декорируемой функции
    """
    def wrapper(*args):
        start = time.time()
        func(*args)
        print(func.__name__, "время выполнения: ", time.time() - start)
    return wrapper
