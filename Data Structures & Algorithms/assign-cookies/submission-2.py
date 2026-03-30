class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # g hold each childs greed aka how big of a cookie they want
        # can only give each child one cookie
        # s holds the cookie sizes
        # child is satisfied if the size of cookie is >= to their greed
        # return maximized content number of children

        # two pointers
        # one for arr g and one for arr s
        # i want to be greedy so give the smallest cookie to the least greedy child
        # good way to do this is sorting the two arrays first
        # comparing the first item in each arr to each other
        # if s[i] >= g[i], we increment both pointers and icnrease cookie count
        # if this condition not satisfied, we need to see move onto the next child. 
        g.sort()
        s.sort()
        cookies = 0

        p1 = len(g) - 1
        p2 = len(s) - 1
        while p1 >= 0: # iterate till we reach the first child
            if p2 >= 0 and s[p2] >= g[p1]:
                cookies += 1
                p2 -= 1
            p1 -= 1
        
        return cookies

        # g=[10,9,8,7] -> 7 8 9 10
        # s=[5,6,7,8] -> 5 6 7 8



