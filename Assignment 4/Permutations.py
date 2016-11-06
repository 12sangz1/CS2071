'''
Team Members: Zachary Sang, Dominic Farolino, Kurt Lewis

How to run program: 
	1: Run 'python Permutations.py'
	2: Follow prompt for 'n: ', enter number to permutate (Eg: if want to permutate {1,2,3,4}, enter '4'), and hit the 'Enter' key
	3: Follow prompt for 'k: ', enter the kth permutation you want, and hit the 'Enter' key
	4: View results

Sample runs can be found at the end of this program file
'''
import math
import sys

#generates a list of incremental numbers up to k
def listGen(n):
	if n == 0:
		return []
	else:
		return (listGen(n-1) + [n])


#Function to take kth permutation of objects in permList
def perm(k, permList,acc=[]):

	#n holds the number of objects remaining to be permutated
	n = len(permList)
	if n > 0:
		#get location in set of the next digit
		digitLoc = math.floor((k)/(math.factorial(n-1))) % n

		#use calculated location to grab next value
		value = permList[digitLoc]

		#repeat for remaining digits
		return perm(k,permList[:digitLoc]+permList[digitLoc+1:],acc + [value])
		
	else:
		return acc

#get inputs from user
N = input("n: ")
K = input("k: ")

#check user inputs
if N == "" or K == "":
	print("Insufficient values given")
	sys.exit()
else:
	N = int(N)
	K = int(K) - 1
	if(K < 0 or K > math.factorial(N)):
		print("Given K value out of bounds (max permutations is {})...Exiting!".format(math.factorial(N)))
		sys.exit()

#output result
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

Performance analysis - 
If n is the length of the list we'd like to permutate, then this program runs in O(n^2) time.

This is because for every element in n, the factorial of n must be computed. This is an O(n) operation. Because the factorial must be found n times,
the algorithm itself is O(n^2).
Permutating the list means calculating the permutated item for each index, an O(C)[constant] computation if you consider finding the factorial seperate. This
does not contribute to the complexity of the program in a meaningful way. 
'''