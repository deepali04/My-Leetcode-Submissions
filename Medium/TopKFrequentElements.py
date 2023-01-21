class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #iterated the nums list using list comprehension from 0 index to length of the nums
    #and then made a counter in the nums and returned the value of the element repeated atleast k times.

    print(Counter(nums))
    return [x[0] for x in Counter(nums).most_common(k)]