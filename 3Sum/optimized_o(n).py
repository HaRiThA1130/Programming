class Solution(object):
    def threeSum(self, nums):
        # res=[]
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             if i!=j and i!=k and j!=k:
        #                 if nums[i]+nums[j]+nums[k]==0:
        #                     if (sorted([nums[i],nums[j],nums[k]])) not in res:
        #                         res.append(sorted([nums[i],nums[j],nums[k]]))
        # return res      
        res= []
        nums.sort()
        n = len(nums)
        for i in range(len(nums)):
            a = nums[i]
            b = i + 1
            c = n - 1
            while b < c:
                if nums[b] + nums[c] == -a and [a, nums[b], nums[c]] not in res:
                    res.append([a, nums[b], nums[c]])
                    b += 1
                    c -= 1
                elif nums[b] + nums[c] < -a:
                    b += 1
                else:
                    c -= 1
        return res

        # [-4, -1, -1, 0, 1, 2]


        
