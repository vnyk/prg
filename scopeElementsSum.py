"""
The absolute difference between two integers,  and , is written as . The maximum absolute difference between two integers in a set of positive integers, , is the largest absolute difference between any two integers in .

The Difference class is started for you in the editor. It has a private integer array () for storing  non-negative integers, and a public integer () for storing the maximum absolute difference.

Task 
Complete the Difference class by writing the following:

A class constructor that takes an array of integers as a parameter and saves it to the  instance variable.
A computeDifference method that finds the maximum absolute difference between any  numbers in  and stores it in the 
maximumDifference instance variable.
Constraints

, where 
Output Format

You are not responsible for printing any output; the Solution class will print the value of the  instance variable.

"""




class Difference:
    def __init__(self, a):
        self.__elements = a
        # Add your code here
    
    def computeDifference(self):
        #self.maximumDifference = max(abs(a[i]-a[i+1]) for i in range(len(a)-1))
        self.maximumDifference = max(a)-min(a)

        return(self.maximumDifference)
        
        # End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)

''' ======================RESULT=================='''
Input (stdin)Download
3
1 2 5
Expected OutputDownload
4
