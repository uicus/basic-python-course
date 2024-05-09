# n! = 1 * 2 * 3 * 4 * ... * (n-1) * n

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)

# factorial_recursive(5) # returned ...
 # |
 # |
 # v
 # factorial_recursive(4) # returned ...
  # |
  # |
  # v
  # factorial_recursive(3) # returned ...
   # |
   # |
   # v
   # factorial_recursive(2) # returned 2 to factorial_recursive(3)
    # |
    # |
    # v
    # factorial_recursive(1) # returned 1 to factorial_recursive(2)


def factorial_with_accumulator(n):
    def factorial_with_accumulator_helper(n, acc):
        if n == 1:
            return acc
        print("QQQ", n)
        return factorial_with_accumulator_helper(n-1, acc*n)
        print("Aktualne n:", n)
    return factorial_with_accumulator_helper(n, 1)


def factorial_exceptional(n):
    def factorial_exceptional_helper(n, acc):
        if n == 1:
            raise Exception(acc)
        else:
            print("QQQ", n)
            factorial_exceptional_helper(n-1, acc*n)
            print("Aktualne n:", n)
    try:
        factorial_exceptional_helper(n, 1)
    except Exception as wrapped_result:
        return int(str(wrapped_result))


print(factorial(15))
print(factorial_recursive(15))
# print(factorial_with_accumulator(15))
print(factorial_exceptional(15))
