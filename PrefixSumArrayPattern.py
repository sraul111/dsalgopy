from typing import List


class NumArray:

    def __init__(self):
        # self.arr = nums
        # self.prefix_sum = [0] * len(self.arr)
        # self.prefix_sum[0] = self.arr[0]
        # for i in range(1, len(self.arr)):
        #     self.prefix_sum[i] = self.prefix_sum[i-1] + self.arr[i]

        self.prefix_sum = [0]
        
        # Precompute the prefix sums
        # for num in nums:
        #     print(self.prefix_sum[-1])
        #     self.prefix_sum.append(self.prefix_sum[-1] + num)

        # print(self.prefix_sum)    
        
    def createPrefixSumOfArray(self,nums: List[int]) -> List[int]:
        #prefix_sum = [0]
        for num in nums:
            self.prefix_sum.append(self.prefix_sum[-1]+num)
        return self.prefix_sum    

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right+1] -self.prefix_sum[left]

    def subarray_sum(self,nums: List[int], target):
        prefix_sum_map = {0: 1}  # Initialize with 0 sum having one count
        current_sum = 0
        count = 0

        for num in nums:
            current_sum += num
            if (current_sum - target) in prefix_sum_map:
                count += prefix_sum_map[current_sum - target]
            if current_sum in prefix_sum_map:
                prefix_sum_map[current_sum] += 1
            else:
                prefix_sum_map[current_sum] = 1

        return count    
    
    def subarray_sum1(self,nums: List[int], target):
        #not implemented correctly/completely
        hashMap = {0:1} # initialize with 0 sum having one count
        countOfSubArraysWithTargetAsSum =0
        sumOfNums = 0

        for num in nums:
            if(num == target):
                if(num in hashMap):
                    hashMap[num] += 1

            
            sumOfNums += num
            if(sumOfNums == target):
                if(sumOfNums in hashMap):
                    hashMap[sumOfNums] +=1

        if(target in hashMap):
            return hashMap.get(target)
        return 0

    def findMaxLengthOfContigousBinary(self, nums: List[int]) -> int:
        # Initialize the hashmap with prefix sum 0 at index -1
        prefix_sum_map = {0: -1}
        max_length = 0
        prefix_sum = 0
        
        for i, num in enumerate(nums):
            # Replace 0 with -1
            if num == 0:
                prefix_sum -= 1
            else:
                prefix_sum += 1
            
            # Check if the prefix sum has been seen before
            if prefix_sum in prefix_sum_map:
                # Calculate the length of the subarray
                max_length = max(max_length, i - prefix_sum_map[prefix_sum])
            else:
                # Store the first occurrence of the prefix sum
                prefix_sum_map[prefix_sum] = i
        
        return max_length



#obj = NumArray([1,-1,-1,1,1,-1,-1,1])
numArray = NumArray()
#print(numArray.createPrefixSumOfArray([1,2,3,4,5]))
print(numArray.subarray_sum1([1,2,3,4,5],3))
#print(numArray.findMaxLengthOfContigousBinary([0,0,0,1,1,1,0,0]))