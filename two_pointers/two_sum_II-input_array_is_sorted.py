class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        """
        Input: 
        - numbers; an array of integers
        - target: an integer

        Output: return the 1-indexed positions of the two numbers whose sum equals target

        Examople: 
        numbers = [2, 7, 11, 5], target = 9

        We return [1, 2] because 2 + 7 = 9

        Goal: find two elements whose sum equals target

        The array is already sorted in non decreasing oreder which is the key propoerty that we'll take advantage of.

        Edge cases:
        1. When array is of the minumm array size
            e.g numbers = [-1, 0], target = -1
            retyrn [1, 2]

        2. When array is of the minimum array size and has duplicate elements
            e.g numbers = [2, 2], target = 4
            retuen [1, 2]

        3. When array has negative numbers
            e.g numbers = [-5, -2, 3, 7], target = 7
            return [2, 4]

        4. When two numbers are far apart
            e.g numbers = [1, 2, 3, 4, 9], target = 10
            return [1, 5]

        - - -

        Brute Force Approach(Basic Array Traversal/Nested Loop)
        Intuition: The straightforward approach here is to compare every possible pair of numbers and return the indices of the numbers that sum up to target

        Example 1:
        numbers = [2, 7, 11, 15], target = 9

        [2, 7, 11, 15]
         ↑  ↑
         i
            j

        Remember, our array is 1-indexed.

        At index 1: 2
        At index 2: 7
        is 2 + 7 = 9? Yes

        We return [1, 2]

        Example 2:
        numbers = [1, 3, 4, 5] target = 7

        [1, 3, 4, 5]
         ↑  ↑
         i
            j

        At index 1: 1
        At index 2: 3
        Is 1 + 3 == 7? No

        We still stay at index 1, and compare with the rest of the numbers after it

        At index 1: 1
        At index 3: 4
        is 1 + 4 == 7? No

        At index 1: 1
        At indec 4: 5
        is 1 + 5 == 7? No

        Then we move to the next index 2, and compare the element at index 2, with every other element after it

        At index 2: 3
        At index 3: 4
        is 3 + 4 == 7? es

        We return [2, 3]

        Algorithm:
        1. Loop through each number in nums using index i
        2. For every i, loop through each number after it using index j
        3. check if index i and index j equals target
            - if they are equal, return their 1-indexed positions
        4. Becaus ethe problem guran tees an exactly one solution, we will eventually find a pair

        Pseudocode:
        for i, from 0 to len(nums) - 1
            for j, from i + 1 to len(nums) - 1
                if nums[i] + nums[j] == target:
                    return [i + 1, j + 1]

        Time complexity: O(n) because we pass through each number in nums at least twice
        Space complexity: O(1) because we created no extra data structure

        - - -

        Optimized Approach 1 (Two pointers)
        - Because the array is. sorted, we can use two pointers to adjust the sum eficiently.
        - If the current sum is too big, moving the pointer left makes the sum smaller
        - If the sum is too small, moving the left pointer right, makes  the sum larget
        - This lets us quickly close in on the target without checking every pair

        So, we put a pounter at each end

        numbers = [ 2, 7, 11, 15], target = 9
                    ↑          ↑
                  left
                               right

        We calucate: numbers[left] + numbers[right]

        if the sum is too small: sum < target
            we move left rightward

        if the sum is too big: sum > target
            we move right leftward

        When sum equals target, we returned their 1-indexed indices

        Like in the xample above:

        Step 1:
        2 + 15 > 9
        we move right pointer leeftward

        Step 2:
        2 + 11 > 9
        we move right pointer leftward

        Step 3:
        2 + 7 == 9

        We return [1, 2]

        Algorithm:
        1. Initiate left pointer = 0
        2. Initiate right pointer = len(numbers) - 1
        3. While left < right
            - calculate total = numbers[left] + numbers[right]
            - if sum == target, return their 1-indexed indices
            - if sum < target, move left rightward
            - if sum > target, move right leftward
        4. Return the answer

        Pseudocode
        left = 0
        right = len(numbers) - 1

        while left < right:

            total = numbers[left] + numbers[right]

            if total == target:
                return [left + 1, right + 1]
        
            if total < target:
                left += 1
            else:
                right -= 1

        Time complexity : O(n) because each pointer only moves in one direction, so together they make at most n moves.
        Space complexity: O(1) because we only used two pointers and a few variables

        - - -

        Optimized Approach 1 (Binary Search) 



        """
        # # Brite force Approach (Basic Array Traversal/Nested Loop)
        # for i in range(len(numbers)):
        #     for j in range(i + 1, len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i + 1, j + 1]

        # Optimized Approach (Two pointers)
        left = 0
        right = len(numbers) - 1

        while left < right:

            total = numbers[left] + numbers[right]

            if total == target:
                return [left + 1, right + 1]
        
            if total < target:
                left += 1
            else:
                right -= 1

        # Optimized Approach 1 (Binary Search) 
        """
        We also could solve this using binary search approach since the array is sorted.
        We just need to :
        - find the complement that when added to numbers[i] equals target
        - we find the middle number in the array, and 
            - if mid == coplement, we return their 1-indexed indice
            - if mid < complement, we serach right
            - if mid > complement, we serach left
        """
