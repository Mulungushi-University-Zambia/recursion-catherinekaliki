def factorial(n):
"""Compute n! using an iterative approach."""
   if n < 0:
         return "Error: Factorial is not defined for negative numbers."
        result = 1
        i = 1
        while 1 <= n:
            result =  result * i
            i = i + 1
        return results


#---Main Program---

try:
   n = int(input("Enter a non-negative integer: "))
   answer = factorial(n)
   print(f"Factorial of {n} = {answer}")
except ValueError:
   print("Invalid input. Please enter a whole number.")


   