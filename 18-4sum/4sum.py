from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Sort the array to use the two-pointer technique and handle duplicates.
        nums.sort()
        n = len(nums)
        result = []

        if n < 4:
            return []

        # Outer loop for the first number
        for i in range(n - 3):
            # Skip duplicates for the first number
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # Second loop for the second number
            for j in range(i + 1, n - 2):
                # Skip duplicates for the second number
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue

                # Two-pointer approach for the last two numbers
                left, right = j + 1, n - 1
                
                # Note: We need to use 64-bit integers for sums to avoid overflow
                # if the numbers are large. Python handles large integers automatically.
                # In C++ or Java, care must be taken.
                remaining_target = target - nums[i] - nums[j]

                while left < right:
                    current_sum = nums[left] + nums[right]

                    if current_sum == remaining_target:
                        # Found a quadruplet
                        result.append([nums[i], nums[j], nums[left], nums[right]])

                        # Move pointers and skip duplicates for the third number
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        
                        # Skip duplicates for the fourth number
                        right -= 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    elif current_sum < remaining_target:
                        left += 1
                    else: # current_sum > remaining_target
                        right -= 1
        
        return result