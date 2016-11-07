'''
Team Members: Zachary Sang, Dominic Farolino, Kurt Lewis

How to run program:
    * Note - you must run this program with a Python3 interpreter, not Python2
	1: Run 'python Permutations.py'
	2: Follow prompt for 'n: ', enter number of items to permute (Eg: if want to permute {1,2,3,4}, enter '4'), and hit the 'Enter' key
	3: Follow prompt for 'k: ', enter the kth permutation you want, and hit the 'Enter' key
	4: View results

Note about counting backwards from last permutation: To count starting from the last permuation, simply use negative indices (Eg: k = -1 = 24 in the case of permutations of 4 objects)


Sample runs can be found at the end of this program file along with discussion of complexity
'''

import math
import sys

# Generates a list of incremental numbers up to k
# O(n) time complexity
def listGen(n):
	return list(range(1, n+1))


# Tail recursive function to take the kth permutation of objects in permList
# O(n^2) time complexity (due to factorial function time complexity)
# O(1) space complexity through tail recursion
def perm(k, permList, acc=[]):

	# n holds the number of objects remaining to be permutated
	n = len(permList)
	if n > 0:
		# Get location in set of the next digit
		digitLoc = math.floor((k)/(math.factorial(n-1))) % n

		# Use calculated location to grab next value
		value = permList[digitLoc]

		return perm(k, permList[:digitLoc] + permList[digitLoc+1:], acc + [value])

	else:
		return acc

# Get inputs from user
N = input("n: ")
K = input("k: ")

# Check user inputs
if N == "" or K == "":
	print("Insufficient values given")
	sys.exit()
else:
	N = int(N)
	K =  int(K) - 1 if int(K) > 0 else int(K)
	if(K < -1*math.factorial(N) or K > math.factorial(N)):
		print("Given K value out of bounds (max permutations is {})...Exiting!".format(math.factorial(N)))
		sys.exit()

# Output result
print("Output: " + str(perm(K,listGen(N))))

'''
Sample Runs)

Example A: python Permutations.py
	n: 4
	k: 5
	Output: [1, 4, 2, 3]

Example B: python Permutations.py
	n: 4
	k: 1
	Output: [1, 2, 3, 4]

Example C: python Permutations.py
	n: 4
	k: 24
	Output: [4, 3, 2, 1]

Example D: python Permutations.py
n: 4
k: 30
Given K value out of bounds (max permutations is 24)...exiting!


Bonus Questions

    1.) By entering negative values for 'k', the user is able to count back from the last permutation (See note at top of documentation by intructions for running)

    2.) We chose to submit the project in Python(3) because we get the ability to handle very very large integers for free, and since handling large integers is the main issue when calculating the kth permutation of a very large set (9+ elements) Python handles this with no problems, thus we've solved #2 as well.


Performance analysis - 
If n is the length of the list we'd like to permutate, then this program runs in O(n^2) time.

This is because for every element in n, the factorial of n must be computed. This is an O(n) operation. Because the factorial must be found n times,
the algorithm itself is O(n^2).
Permutating the list means calculating the permutated item for each index, an O(C)[constant] computation if you consider finding the factorial seperate. This
does not contribute to the complexity of the program in a meaningful way. 

Additionally, the number of primitive operations, such as comparisons or basic arithmetic operations (Eg: + or -), within the body of our 'perm' function contributes to a constant 'c' that is applied to the complexity of this program.
This constant however, is disregarded as it is insignificant to the overall complexity. That is c*O(n^2) is considered to be equivalent to O(n^2) in terms of complexity.
'''
