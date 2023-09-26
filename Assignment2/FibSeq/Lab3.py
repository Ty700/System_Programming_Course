#Tyler Scotti - Didn't forget this time
import time

# Naive recursive Fibonacci function
def fibonacci_naive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_naive(n-1) + fibonacci_naive(n-2)

# Memoization-based Fibonacci function
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]

    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)

    return memo[n]

def main():

    n = int(input("Enter in an integer: "))

    #Naive
    start_time_naive = time.time()

    result_naive = fibonacci_naive(n)

    end_time_naive = time.time()

    result_time_naive = end_time_naive - start_time_naive

    #Memo
    start_time_memo = time.time()

    result_memo = fibonacci_memo(n)

    end_time_memo = time.time()

    result_time_memo = end_time_memo - start_time_memo

    #Outputs

    print("Naive Result: {}\nNaive time: {:.4f}s\nMemo Result: {}\nMemo Time: {:.4f}s"
          .format(result_naive, result_time_naive, result_memo, result_time_memo))

if __name__ == "__main__":
    main()