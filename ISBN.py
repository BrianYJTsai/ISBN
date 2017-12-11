#  File: ISBN.py

#  Description: Program outputs the validity of an ISBN number to another file. User inputs a text file of ISBN numbers
#  and the output is another file with all valid and invalid ISBN numbers

#  Student Name: Brian Tsai

#  Student UT EID: byt76

#  Course Name: CS 303E

#  Unique Number: 51850

#  Date Created: 4/15/17

#  Date Last Modified: 4/15/17

# Checks whether the ISBN number has the correct format first
def is_Valid(char_list):

	# Check that the number has only number digits, "x", "X", and "-"
	for char in char_list:
		if (char.isdigit() or char == "-" or char == "X" or char == "x"):
			continue
		else:
			return False
	
	# Removes all hyphens from the number
	line = ""
	for char in char_list:
		if (not char == "-"):
			line += char		
	
	# Determines if the number is the proper length
	if (len(line) != 10):	
		return False
	# Determines whether the first 9 characters are digit and the last one is either a digit or special character	
	if (not line[0:9].isdigit() or (not line[9].isdigit() and line[9] != "X" and line[9] != "x")):
		return False

	# Return true if all format tests pass
	return True
			
# Calculates the partial sum of the number 
def partial_sum(char_list):
	partial_sumList = []
	
	# Appends the partial sum of the original list to a new list
	for num in range(len(char_list)):
		partial_sumList.append(partial_sum_calculator(0, char_list, num))
	return partial_sumList	

# Recursively calculate the sum of a sequence of numbers 
def partial_sum_calculator(start, char_list, end):
	if (start > end):
		return 0
	else:
		return char_list[start] + partial_sum_calculator(start + 1, char_list, end)			 

# Format the list to remove all hyphens and replace special characters with 10
def format_list(char_list):
	corrected_list = []
	for char in char_list:
		
		# Remove hyphens 
		if (char == "-"):
			continue
		# Replace special character "X" or "x" with 10
		elif (char == "X" or char == "x"):
			corrected_list.append(10)
		# Else append the character as an int
		else:
			corrected_list.append(int(char))
	return corrected_list

def main():
	ISBN_input = open("isbn.txt", "r")
	ISBN_output = open("isbnOut.txt", "w")

	# Iterate through all the lines
	for line in ISBN_input:
		
		# Remove carriage return
		line = line.strip("\n")
		# Convert the input string to a list of strings
		char_list = [str(x) for x in line]
		
		# First check if the string is in the proper format
		if (is_Valid(char_list)):
			
			# Format the list to calculate the partial sum
			char_list = format_list(char_list)
			
			# s1 is a list of the partial sum of the original list
			s1 = partial_sum(char_list)

			# s2 is a list of the partial sum of s1
			s2 = partial_sum(s1)
		
			# Determine whether the sum of s1 is divisible by 11
			if (s2[len(s2)-1] % 11 == 0):

				ISBN_output.write(line + " valid" + "\n")
			
			# If not, the number is invalid
			else:
				ISBN_output.write(line + " invalid" + "\n")
		
		# If the format of the string is incorrect, the number is invalid 
		else:
			ISBN_output.write(line + " invalid" + "\n")
	
	ISBN_input.close()
	ISBN_output.close()					 
main()			