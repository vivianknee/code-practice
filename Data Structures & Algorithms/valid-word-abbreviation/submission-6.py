class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # two things to consider
        # are we evaluating a digit or a char
        # if char: just check that they are equal
        # if digit we need to update a pointer to point in the right place

        def parseNumber(s, i):
            res = []
            while i < len(s) and s[i].isdigit():
                res.append(s[i])
                i+=1
            return int("".join(res)), i

        wordIndex = 0
        abbrIndex = 0
        while abbrIndex < len(abbr):
            # if the char is a letter, compare to pos in word for validity
            if abbr[abbrIndex].isalpha():
                if wordIndex >= len(word):
                    return False
                if word[wordIndex] != abbr[abbrIndex]:
                    return False
                abbrIndex += 1
                wordIndex += 1
            else: # we are working with digits at this point
                if abbr[abbrIndex] == '0':
                    return False
                # get the number and get the index in abbr
                num, new_index = parseNumber(abbr, abbrIndex)
                # check if the num is too big for the remaining char
                if num > ((len(word)-1) - wordIndex) + 1:
                    return False
                # it fits, update indexes
                else:
                    abbrIndex = new_index
                    wordIndex += num
        return True

        # word="apple"
                  
        # abbr="a4"
        # compare a and a --> match indexes icnrease to 1 and 1
        # 4 - 1 = 3






                