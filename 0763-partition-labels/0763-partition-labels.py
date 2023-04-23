class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        df = defaultdict(list)
        n = len(s)
        for i in range(n):
            df[s[i]].append(i+1)
        parts = []
        for item in df.values():
            if len(item)>=2:
                parts.append([item[0],item[-1]])
            else:
                parts.append([item[0],item[0]])

        parts.sort(key=lambda item: item[0])
        memory = parts[0]
        partition = []
        for i in range(1,len(parts)):
            if memory[1] > parts[i][0]:
                memory[1] = max(parts[i][1],memory[1])
            else:
                partition.append(memory)
                memory = parts[i]
        result = []
        ss = 0
        for p in partition:
            result.append(p[1] - ss)
            ss = p[1]
        result.append(n - ss)
        return result