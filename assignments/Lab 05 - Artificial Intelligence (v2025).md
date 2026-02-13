# Lab 05 - Artificial Intelligence

This lab is a little different than past ones. It's going to involve practice with LLMs like chatGPT. Be sure to watch the lecture recording about how large language models work and how to use chatGPT specifically.

Upload a document that answers the following questions:

1. Make an account on [https://chat.openai.com](https://chat.openai.com) if you don't have one. Ask the model to generate a Python program that does *something* simple but interesting. You have freedom of choice here. Try running the program in replit. Include the source code and explain whether it worked as intended.

   1. The prompt you used

      > *Your answer here*

   2. The source code it produced

      > *Your answer here*

   3. Did it work?

      > *Your answer here*

2. Take the following python program, which has a problem, and ask chatGPT to explain what's wrong with it and fix it. Test the code. Did it work? Include the fixed code in the document. Now ask chatGPT to re-organize the code so it has a main function that asks for the limit on the console. Does it work? Here's the broken program:

   ```python
   def sieve_of_eratosthenes(limit):
       if limit < 2:
           return []

       # Initialize a list of boolean values. All numbers are initially assumed to be prime.
       is_prime = [True] * (limit + 1)
       is_prime[0:2] = [False, False]  # 0 and 1 are not prime numbers

       # Iterate through the numbers and mark their multiples as non-prime
       for number in range(2, limit**0.5 - 1):
           if is_prime[number]:
               for multiple in range(number*number, number, limit + 1):
                   is_prime[multiple] = False

       # Collect all prime numbers
       primes = [number for number, prime in enumerate(is_prime) if prime]

       return primes

   # Example usage
   limit = 200
   primes = sieve_of_eratosthenes(limit)
   print(primes)
   ```

   1. The prompt you used to request the code be fixed

      > *Your answer here*

   2. The response from chatGPT

      > *Your answer here*

   3. Did it work?

      > *Your answer here*

3. What are your overall thoughts about using chatGPT for coding?

   > *Your answer here*
