class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        # sets dont take duplicates

        for num in nums: # loop thru entire list
            # only one int that appears two or more times
            if num not in seen:
                seen.add(num)
            else:
                break
        
        return num
        

        