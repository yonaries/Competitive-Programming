class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = sum(cardPoints[len(cardPoints)-k:])
        left, right = 0, len(cardPoints)-k
        answer = total
        
        while right < len(cardPoints):
            total += cardPoints[left] - cardPoints[right]
            answer = max(answer, total)
            
            left += 1
            right += 1
            
        return answer