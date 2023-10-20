class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = sum(cardPoints)
        
        cards_size = len(cardPoints)
        win_size = cards_size - k
        
        answer = sum(cardPoints[cards_size-k:])
        
        win_sum = sum(cardPoints[:win_size])
        # print(answer, cardPoints[:k])
        
        for i in range(win_size, cards_size):
            win_sum += cardPoints[i] - cardPoints[i-win_size]

            answer = max(answer, total - win_sum)

        return answer