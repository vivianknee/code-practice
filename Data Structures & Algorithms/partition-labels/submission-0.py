class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # if we encounter a char, all instances of that char need to be in the same substring
        # res = [] contains len of all possible substrings
        # create an adj list mapping char to freq
        # iterate over the string. when we encounter the first char
        # we need to keep iterating over the string while deincremenitg the freq of the char
        # only when that freq reaches 0 do we start a new subarray
        # at the end of each operation, append the pointer len to the res array

        adjList = {}
        for char in s:
            if char in adjList:
                adjList[char] += 1
            else:
                adjList[char] = 1
        
        # iterate over the string
        l = 0
        res = []
        seen = set()
        for r in range(len(s)):
            curChar = s[r]
            adjList[curChar] -= 1
            seen.add(curChar)

            if all(adjList[c] == 0 for c in seen): # ALL char need to have freq 0
                res.append(r - l + 1)  # correct interval length
                l = r + 1              # move l to start of next partition
                seen.clear()           # reset for next partition
        
        return res






