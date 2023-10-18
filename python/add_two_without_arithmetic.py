"""
Add without using any arithmetic operation
intVar1 = 9
strVar2 = "10"
print(add_two(intVar1, strVar2))
19
"""

#Probably can do it with slamming if-statements for generic 0 through 9 plus 0 through 9, but it's a 10^2 if statements

# Instead I will use arrays

def add_two(value_input1, value_input2):
	value_int1, value_input2 = int(value_input1), int(value_input2)

	# add a try statement
	# add a word to int translation

	return_array = []

	for _ in range(value_input1):
		return_array.append("x")

	for _ in range(value_input2):
		return_array.append("y")
	# technically x & y variables are irrelevant for this challange

	return len(return_array)


if __name__ == '__main__':
	print(add_two(1, "9"))
	intVar1 = 9
	strVar2 = "10"
	print(add_two(intVar1, strVar2))

"""
time to resolve: 9 to 13 minutes & 1 re-run (b/c of typo in the problem statement & ended up copy-pasta the error over)

* Overall senior-level speed, but the solution provided could be a bit more robust. It would take like 1 minute to slap a a generic try/except Exception as ex: or something like that.

* Smarter decision would be use a bit-wise addition imo, but if the code works it works - kind of makes you look mid to junior level dev.
	def add_two(value1, value2):
	    MAX_INT = 0x7FFFFFFF  # Max 32-bit signed integer

	    # Convert input values to integers, handling potential errors
	    try:
	        value1 = int(value1)
	        value2 = int(value2)
	    except ValueError:
	        raise ValueError("Both input values must be integers or convertible to integers.")

	    while value2 != 0:
	        carry = value1 & value2  # Calculate the common set bits
	        value1 = value1 ^ value2  # XOR to get the sum
	        value2 = carry << 1  # Carry is shifted by one position

	    # Handle overflow by checking if the result exceeds the maximum integer value
	    if value1 > MAX_INT:
	        return -(MAX_INT - (value1 % MAX_INT))
	    return value1

	if __name__ == '__main__':
	    intVar1 = 9
	    strVar2 = "10"
	    print(add_two(intVar1, strVar2))  # Output: 19



Nit-picks:
* This solution wouldn't work in C, but for the occassion it is technically correct lol

* Almost fcked up 	if __name__ == '__main__': lmao

* Use vim or neovim
  Stop using tabs, use spaces - you can configure vim to replace tabs with spacing
  make sure you learn majority of pre-defined short-cuts so your hands stay on the sauce at all times. + don't forget to customize ur own configs

* A bit better w/ hands on the keyboard, but still avoid keying back&forth for opening & closing {[""]}. Also for top speeds, you gots to forget about the existance of the mouse :))
"""
