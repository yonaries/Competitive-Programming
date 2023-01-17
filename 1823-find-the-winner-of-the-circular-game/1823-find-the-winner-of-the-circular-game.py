class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = list(range(1, n+1))
        l = k
        
        while n != 1:
            turn = (l % n) - 1
            players.pop(turn)
            
            l = turn + k if turn != -1 else k
            n -= 1
        
        return players[0]       