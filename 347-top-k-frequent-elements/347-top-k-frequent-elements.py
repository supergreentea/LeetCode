class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        frequencies = Counter(nums)
        output = []
        
        for num, count in frequencies.items():
            buckets[count].append(num)
        
        print(buckets)
            
        for i in range(len(nums), -1, -1):
            for n in buckets[i]:
                output.append(n)
                print(len(output))
                if len(output) == k:
                    return output
        
        return output