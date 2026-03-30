class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)

        for n in nums:
            count[n] += 1

            if len(count) <= 2:
                continue
            new_count = defaultdict(int)
            for n, c in count.items():
                if c > 1:
                    new_count[n] = c - 1
            count = new_count

        res = []
        for n in count:
            if nums.count(n) > len(nums) // 3:
                res.append(n)
        
        return res






        # find all alements that appear more than n/3 times
        # nums = [5,2,3,2,2,2,2,5,5,5] len(nums) / 3 = 10/3 = 3
        # return elements that appear more than 3 times in this case 5 and 2

        # initial thoughts
        # first create a dictionary of number and frequencies
        # if the freq > n/3, append it to a result

        # res = []
        # times = len(nums) // 3

        # freqTable = {}
        # for num in nums:
        #     if num in freqTable: # saw it again
        #         freqTable[num] += 1
        #     else:
        #         freqTable[num] = 1 # just saw it
        
        # for key in freqTable:
        #     if freqTable[key] > times:
        #         res.append(key)
        
        # return res