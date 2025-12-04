class Solution(object):
    def threeSum(self, nums):
        res=[]
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if i!=j and i!=k and j!=k:
                        if nums[i]+nums[j]+nums[k]==0:
                            if (sorted([nums[i],nums[j],nums[k]])) not in res:
                                res.append(sorted([nums[i],nums[j],nums[k]]))
        return res                    

        
