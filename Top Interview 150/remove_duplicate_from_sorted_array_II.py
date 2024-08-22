class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index, occurence = 1, 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                occurence += 1
            else:
                occurence = 1
            
            if occurence <= 2:
                nums[index] = nums[i]
                index += 1
            print(nums)
        return index
