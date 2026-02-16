Requirement to write the Collatz Sequence program.

Write a function named collatz () that has one parameter named number. 
\If number is even, then collatz should print number // 2 and return this value. 
If number is odd, then collatz() should print and return 3 * number + 1.
   Then write a program that lets the user type in an integer and that keeps calling collatz () on that number until the function returns the value 1.
   Remember to convert the return value from input() to an integer with the int() function; otherwise, it will be a tring value.
   Hint: An integer number is even if number % 2 == 0, and it is odd if number % 2 == 1.
   The output of this program should look something like this:

   Enter Number:
   3
   10
   5
   16
   8
   4
   2
   1

   Input Validation
   Add try and except statements to the previous project to detect wheter the user types in an nonintigerb string . Normally, the int() function will 
   raise a ValueError error if it is passed a noninteger string, as an int('puppy). In the except clause, 
   print a message to the user  saying they must enter an integer.
   
