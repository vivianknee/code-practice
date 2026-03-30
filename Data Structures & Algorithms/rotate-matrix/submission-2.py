class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # square matrix
        # rotate 90 degrees clockwise, right down left up starting from top left
        # need to rotate until the grid id 1 by 1

        # four pointers left right top bottom
        l = 0
        r = len(matrix) - 1

        while l < r:
            # gets num of iterations it should be doing which is len of outer matrix
            for i in range(r - l):
                top = l
                bott = r

                # save the top left
                topLeft = matrix[top][l + i]

                # move the bottom left into top left
                matrix[top][l + i] = matrix[bott - i][l]

                # move bottom right into bottom left
                matrix[bott - i][l] = matrix[bott][r - i]

                # move top right into bottom right
                matrix[bott][r - i] = matrix[top + i][r]

                # move top left into top right
                matrix[top + i][r] = topLeft

            r -= 1
            l += 1


        