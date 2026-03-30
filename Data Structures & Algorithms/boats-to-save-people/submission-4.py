class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # greedy approach
        # sort from lightest to heaviest
        people.sort()
        left, right = 0, len(people) - 1
        boats = 0
        
        while left <= right:
            # Heaviest person always needs a boat
            # Check if lightest can join them
            if people[left] + people[right] <= limit:
                left += 1  # lightest person boards
            right -= 1     # heaviest person boards
            boats += 1
        
        return boats


