class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        count = 0 

        while l <= r: 
            total = people[l] + people[r]
            count += 1 

            if total <= limit: 
                l += 1
                r -= 1 
            elif total > limit: 
                r -= 1 
            else: 
                l += 1 
                r -= 1 

        return count  

        