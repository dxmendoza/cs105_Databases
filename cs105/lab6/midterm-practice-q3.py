# Question 3: Please write a Python function called zero_count
# which takes as input a single list of integers.
# This function counts the number of integers contained inside
# the input list, and returns this count as output.
# For example, zero count([0,2,4,-1,0,2,0]) should produce the value 3.
# You may either use recursion or loops: whichever you prefer.

def zero_count(x):
    # Initialize a variable 'counter' to 0.
    # This will keep track of how many zeros are in the list.
    counter = 0

    # Loop through each element 'e' in the input list 'x'.
    for e in x:
        # Check if the current element 'e' is equal to 0.
        if e == 0:
            # If it is, increment the 'counter' by 1.
            counter = counter + 1

    # After the loop ends, return the value of 'counter'.
    # This is the total number of zeros found in the list.
    return counter


print(zero_count([0, 2, 4, -1, 0, 2, 0]))
