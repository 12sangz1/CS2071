'''
Team Members: Zachary Sang, Dominic Farolino, Kurt Lewis

How to run program:
    * Note - you must run this program with a Python3 interpreter, not Python2
	1: Run 'python Permutations.py'
	2: Follow prompt for 'n: ', enter number of items to permute (Eg: if want to permute {1,2,3,4}, enter '4'), and hit the 'Enter' key
	3: Follow prompt for 'k: ', enter the kth permutation you want, and hit the 'Enter' key
	4: View results

Sample runs can be found at the end of this program file
'''

import math
import sys

# Generates a list of incremental numbers up to k
# O(n) time complexity
def listGen(n):
	return list(range(1, n+1))


# Tail recursive function to take the kth permutation of objects in permList
# O(n) time complexity
# O(1) space complexity through tail recursion
def perm(k, permList, acc=[]):

	# n holds the number of objects remaining to be permutated
	n = len(permList)
	if n > 0:
		# Get location in set of the next digit
		digitLoc = math.floor((k)/(math.factorial(n-1))) % n

		# Use calculated location to grab next value
		value = permList[digitLoc]

		# Repeat for remaining digits
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
	K = int(K) - 1
	if(K < 0 or K > math.factorial(N)):
		print("Given K value out of bounds (max permutations is {})...Exiting!".format(math.factorial(N)))
		sys.exit()

# Output result
print("Output: " + str(perm(K,listGen(N))))

'''
Sample Runs)

A: python Permutations.py
	n: 4
	k: 5
	Output: [1, 4, 2, 3]

B: python Permutations.py
	n: 4
	k: 1
	Output: [1, 2, 3, 4]

C: python Permutations.py
	n: 4
	k: 24
	Output: [4, 3, 2, 1]

D: python Permutations.py
n: 4
k: 30
Given K value out of bounds (max permutations is 24)...exiting!

--------------------

Bonus Questions

    1.) The way we are handling the permutation generation does not actually depend on whether or not we start at the beginning or end of the permutation list so we've solved #1 through the simplicty of our algorithm.

    2.) We chose to submit the project in Python(3) because we get the ability to handle very very large integers for free, and since handling large integers is the main issue when calculating the kth permutation of a very large set (9+ elements) Python handles this no problem, thus we've solved #2 as well.

'''
