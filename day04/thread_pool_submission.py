import concurrent.futures
import time

def process(number):
    _ = number * 1_000_000 ** 1_000_000
    print("Finished Computation")

if __name__ == "__main__":
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        x = executor.submit(process, 3)
        y = executor.submit(input, "Enter a number: ")
    end_time = time.time()
    print(end_time - start_time)