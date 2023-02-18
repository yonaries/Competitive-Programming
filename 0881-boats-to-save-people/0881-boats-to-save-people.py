class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        high, least, boats = len(people)-1, 0, 0
        
        while(least <= high):
            if (people[least] + people[high] <= limit):
                least += 1
                high -=1
            else:
                high -=1
            boats += 1
            
        return boats
        