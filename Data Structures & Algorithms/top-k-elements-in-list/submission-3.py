class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
    # brute force solution
    # element nums
    # iterate over nums and keep count of the freq of each element

    # for i in range k
    # we want to pop k items w max freq from the hash table 
    # append these to a res

    # 1 2 2 3 3 3 k = 2
    # hash = {1: 1, 2:2, 3: 3}
    # for i in range(k), get the max based on the freq
    # append to res = [2,3]

    # sets up a hash table of numbers : frequencies
        hashTable = {} # number : frequency
        for num in nums:
            if num in hashTable: # increment if alr seen
                hashTable[num] += 1
            else:   
                hashTable[num] = 1 # set to one otherwise
        
        print(hashTable)

        res = []
        for i in range(k):
            maxFreq = max(hashTable, key=hashTable.get) # gets the num for which has max freq
            res.append(maxFreq)
            del hashTable[maxFreq]
        
        return res




        

        
