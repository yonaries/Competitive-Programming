class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        # rules
        
        # player[i] <= trainer[i] to have a match
        # and both players and trainers can only have one or none matches
        
        # if min(trainers) < min(players): min(trainers) can't have any match
        # if max(trainers) < max(players): max(players) can't have any match
        
#         if len(players) == 1 and len(trainers) == 1:
#             if players[0] <= trainers[0]:
#                 return 1
#             else:
#                 return 0
        
#         while (min(trainers) < min(players)): 
#                 trainers.remove(min(trainers))
   
#         while (max(trainers) < max(players)):
#                 players.remove(max(players))
        
#         return min(len(players),len(trainers))

        count = 0
        trainers.sort()
        players.sort()
        left = 0
        for i , player in enumerate(players):
            while(left < len(trainers)):
                if player <= trainers[left]:
                    count += 1
                    left += 1
                    break
                left += 1
        return count
        