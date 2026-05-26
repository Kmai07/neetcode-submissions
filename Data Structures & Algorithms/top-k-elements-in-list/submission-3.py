class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        freq = {}
        for i in nums:
            freq[i] = 1 + freq.get(i,0)
        
        # Sort the dictionary items by value (frequency) in descending order
        sorted_items = sorted(freq.items(), key=lambda item: item[1], reverse=True)
        
        # Take the first k elements from the sorted list and append the keys to ans
        for i in range(k):
            ans.append(sorted_items[i][0])
            
        return ans