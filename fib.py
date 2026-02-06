from functools import lru_cache  # keep cache of previous function calls
from functools import wraps  # to wrap metadata of fib function
import time  # for timer
import matplotlib.pyplot as plt

execution_times = []
ns = []


def timer(func):
    """Adds timer feature to specific function"""

    @wraps(func)
    def wrapper(*args, **kwargs):

        # Calculate execution time
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time

        # Append n to ns for execution t ime graph
        n = args[0]
        ns.append(n)

        # Append execution_time to list for execution time graph
        execution_times.append(execution_time)

        # Build readable argument - string representations of args and kwargs
        arg_list = [str(arg) for arg in args]
        kw_list = [f"{key}={str(val)}" for key, val in kwargs.items()]
        final_argument = ", ".join(arg_list + kw_list)

        # Print formatted execution time of result
        print(
            f"Finished in {execution_time:.8f}s: {func.__name__}({final_argument}) -> {result}"
        )
        return result

    return wrapper


@lru_cache
@timer
def fib(n: int) -> int:
    """Default function to calculate the Fibonacci value for an Integer n"""

    # Calculate the fibonacci value
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    fib(100)

    # Plot execution time line graph
    plt.plot(ns, execution_times)
    plt.show()
