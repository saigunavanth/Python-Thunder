"""
Problem Task: Tower of Hanoi
Problem Link:https://edabit.com/challenge/3ZtykTsx3GSoPHyBb

"""

n=int(input())
def towerofhanoi(n):
	if(n==0):
		return 0
	if(n==1):
		return 1
	if(n>1):
		return (2**n)-1
print(towerofhanoi(n))