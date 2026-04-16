# ICT102 - Lab Work 2: Fibonacci
 
def Fibonacci(n):
   """Print the first n+1 terms of the Fibonacci sequence."""
   if n < 0:
      return "Error: n must be a non-negative integer."
   
   a = 0
   b = 1
   i = 1

   print(a, end=" ")  # print F(0)

   while i <= n:
    
       temp = a + b
       a   =  b
       b   =  temp
       print(a, end=" ")
       i = i + 1

   print()

#---Main Program---
try:
   n = int(input("How many Fibonacci terms? Enter n: "))
   print(f"Fibonacci sequence (first {n+1} terms):")
   Fibonacci(n)
except ValueError:
      print("Invalid input. Please enter a whole number.")