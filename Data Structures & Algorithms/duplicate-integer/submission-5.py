class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        I’m using a hash set for constant lookup.
        I iterate through the array once.
        If an element already exists in the set,
        I return True immediately.
        Otherwise, I add it to the set.
        If iteration completes, no duplicates exist.
        
        """
        seen = set()
        
        for num in nums:
            if num in seen:
                return True
            
            seen.add(num)
        return False