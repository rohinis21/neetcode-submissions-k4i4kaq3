class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
           return False

        check = set()
        
        for num in nums:
            if num in check:
                return True
            
            check.add(num)
            
        return False
    