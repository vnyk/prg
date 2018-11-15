'''Task 
Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum.

Input Format

There are  lines of input, where each line contains  space-separated integers describing 2D Array ; every value in  will be in the inclusive range of  to .'''

import sys
if __name__ == '__main__':
    arr = [*map(int, sys.stdin.read().split())]

    a = max(arr[i]+arr[i+1]+arr[i+2]+arr[i+7]+arr[i+12]+arr[i+13]+arr[i+14] for i in range(22) if i%6<4)
    print(a)
