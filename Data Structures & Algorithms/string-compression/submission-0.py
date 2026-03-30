class Solution:
    def compress(self, chars: List[str]) -> int:
        # modify in place in order to use constant space
        # we will have pointers to modify things in place
        # both pointers start at the beginning
        # pointer 1 is to know where to update things in the arr
        # pointer 2 is to check for new char and their amounts
        # return pointer1 + 1

        p1 = p2 = 0
        curChar = chars[0]
        curCount = 0
        while p2 < len(chars):
            # keep track of curr char
            # keep track of curr count as well
            if chars[p2] == curChar:
                curCount += 1
            else:
                # apend the char 
                chars[p1] = curChar
                p1 += 1
                # append the count
                if curCount > 1:  # only write count if > 1
                    for digit in str(curCount):
                        chars[p1] = digit
                        p1 += 1
                
                curChar = chars[p2] # reset curChar to current one we are at
                curCount = 1 # reset the count
            p2 += 1
        
        chars[p1] = curChar
        p1 += 1
        if curCount > 1:
            for digit in str(curCount):
                chars[p1] = digit
                p1 += 1
        # atp, p2 has reached the end and p1 is at the end of compression
        return p1
                

            
