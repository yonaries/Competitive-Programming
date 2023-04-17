class Solution:
    def findTheWinner(self, n, k):
        n = list(range(1, n+1))
        return self.josephus(n, k)
        
    def josephus(self, players, skip):
        skip -= 1
        idx = skip
        
        while len(players) > 1:
            players.pop(idx)
            idx = (idx + skip) % len(players)
        
        return players[0]