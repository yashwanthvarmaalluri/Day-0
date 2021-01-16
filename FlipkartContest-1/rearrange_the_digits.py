class Solution:
    def smallestnum (self,N):
        l=[int(i) for i in N]
        l.sort()
        c=0
        f=0
        ans=""
        if(l[0]==0):
            for i in l:
                if i==0:
                    c+=1
                    f=1
                else:
                    if(f==1):
                       ans+=str(i)
                       ans+="0"*c
                       f=0
                    else:
                        ans+=str(i)
            return ans
        else:
            for i in l:
                ans+=str(i)
            return ans
      
#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = input()
        ob = Solution()
        ans = ob.smallestnum(N)
        print(ans)

# } Driver Code Ends
