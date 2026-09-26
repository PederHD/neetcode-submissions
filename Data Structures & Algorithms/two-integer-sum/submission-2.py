class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = dict()
        for i,num in enumerate(nums):
            check[num] = i
        
        for i,num in enumerate(nums):
            to_check = target-num
            if to_check in check:
                index_to_check = check[to_check]
                if index_to_check !=i:
                    return [i,index_to_check]
            
        
        return 