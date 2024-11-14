'''Question: Two Sum
Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
'''

nums = [2,7,11,15] 
target = 9
n = len(nums)
for i in range(n):
    for j in range(i+1,n):
        if nums[i] + nums[j] == target:
            in = i,j
            print(list(in))

