
class Solution:
    def convertToWave(self, arr, N):
        i=0
        while(i<N-1):
            arr[i],arr[i+1]=arr[i+1],arr[i]
            i+=2
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math
def main():
    T=int(input())
    while(T>0):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ob.convertToWave(arr,N)
        for i in arr:
            print(i,end=" ")
        print()
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
