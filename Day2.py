# # Task
# # Complete the code in the editor below. The variables , , and  are already declared and initialized for you. You must:

# # Declare  variables: one of type int, one of type double, and one of type String.
# # Read  lines of input from stdin (according to the sequence given in the Input Format section below) and initialize your  variables.
# # Use the  operator to perform the following operations:
# # Print the sum of  plus your int variable on a new line.
# # Print the sum of  plus your double variable to a scale of one decimal place on a new line.
# # Concatenate  with the string you read as input and print the result on a new line.

# # Note: If you are using a language that doesn't support using  for string concatenation (e.g.: C), you can just print one variable immediately following the other on the same line. The string provided in your editor must be printed first, immediately followed by the string you read as input.




i = 100
d = 25.66
s = "Hackerrank"

try:
    
    i2 = int(input("Enter an integer: ").strip())  
    d2 = float(input("Enter a double (float): ").strip())  
    s2 = str(input("Enter a string: ").strip())  
    
    # Print the sum of both integer variables
    print(i + i2)

    # Print the sum of the double variables to one decimal place
    print(f"{d + d2:.1f}")

    # Concatenate and print the String variables
    print(s + s2)

except ValueError:
    print("Invalid input! Please enter valid data types.")

