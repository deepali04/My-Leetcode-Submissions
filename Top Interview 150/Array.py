#problem 88 - Merge Sorted Arrays

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums1[0:m+n] = sorted(nums1[:m]+nums2[:n])
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            
            p -= 1

        nums1[:p2 + 1] = nums2[:p2 + 1]
        
#problem 27 - Remove Element
    def removeElement(self, nums: List[int], val: int) -> int:
        nums[:] = [x for x in nums if x != val]


# problem 26 - Remove duplicates form sorted array
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums))
        print(nums)
        return len(nums)
    

# problem 80 - Remove duplicates form sorted array-II
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

    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0
        first = chars[0]
        count, length  = 0, len(chars)
        chars.append(" ") 
        for i in range(length+1): 
            char = chars.pop(0)
            if char == first: 
                count += 1
            else:
                if count == 1: 
                    chars.append(first) 
                elif count > 1:
                    chars.append(first)
                    chars += (list(str(count))) 
                first = char 
                count = 1 
        return len(chars)
