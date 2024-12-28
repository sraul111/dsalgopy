from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        # Initialize currSum and maxSum to the sum of the initial k elements
        currSum = maxSum = sum(nums[:k])

        # Start the loop from the kth element 
        # Iterate until you reach the end
        for i in range(k, len(nums)):

            # Subtract the left element of the window
            # Add the right element of the window
            currSum += nums[i] - nums[i - k]
            
            # Update the max
            maxSum = max(maxSum, currSum)

        # Since the problem requires average, we return the average
        return maxSum / k

    def findDuplicate(self, nums: List[int]) -> int:
            nums.sort()
            left = 0
            right = len(nums) -1
            #print(right)
            mySet = UniqueSet()

            for i in range(len(nums)):

                try:
                    mySet.add(nums[left])
                    mySet.add(nums[right])
                    left+=1
                    right-=1
                    if left==right:
                        return -1

                except Exception as e:
                    return e
                    # print(f"{e}")
                    # return nums[left]  


class UniqueSet:
    def __init__(self):
        self.elements = set()

    def add(self, value):
        if value in self.elements:
            raise ValueError(value)
        self.elements.add(value) 


solution = Solution()   
print(solution.findDuplicate([1,3,4,2,2]))
# print(solution.findMaxAverage([1, 2, 3, 4, 5],3))
   