class Solution:
    def compress(self, chars: List[str]) -> int:  
        i = result = 0
        comperessed = []
        while i < len(chars):
            current = 1
            while i < len(chars) - 1 and chars[i] == chars[i + 1]:
                i += 1
                current += 1

            comperessed.append(chars[i])
            result += 1
            if current != 1:
                comperessed.extend(str(current))
                result += len(str(current))
            i += 1

        # append to the comperessed list
        for i in range(len(comperessed) - 1, -1, -1):
            chars.insert(0, comperessed[i])
            
        return result