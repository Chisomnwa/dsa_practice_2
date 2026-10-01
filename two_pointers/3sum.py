class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        Input: nums which is an array of integers that contains at least 3 elements, and are not necessarily sorted.

        Output: to return all unique triplets of values that add up to 0.
            - The order of the triplets doens't matter
            - the order of values within a triplet also doesn't matter mathematically, although we usually sort them to make the duplicate detection easier

        Goal: find three different array elements such that 
        nums[i] + nums[j] + nums[k] == 0

        with:

        i != j
        i != k
        j != k

        And importantly, do not return the same value combination more than once

        For example, if an array contains two -1s, we can use both:
        [-1, -1, 2]

        but, we should return that triplet once.

        Edge Cases:
        1. Can we have less than 3 elements?
            - The constraint guarantees at least 3 elelemnets i.e 3 <= nums.length

        2. What happens when we don't have valid triplet?
            - If there's no combination thst suums to 0
            - We return an empty set []

        3. When we have all zeros, what hapens?
            - e.g nums = [0, 0, 0]
            - 0 + 0 + 0 is valid
            - So, we return it only once = [[0, 0, 0]]
        
        4. What happens when you have duplicate values producing the same teriple?
            e.g nums = [-1, 0, 1, 0, 1, -1]
            - There can be multiple ways to select: [-1, 0, 1]
            - But the result should contain that triplet only once

        5. Can we have negative numbers in the valid triplets?
            - Yes, the constraints assures tat so our algorithm should also recognize negative numbers 
            -e.g we have such valid triplets
            [-2, -1, 2]
            [-2, 0, 2]
            [-1, 0, 1]

        6. What if we have multiple different valid triplets?
            - We shoulldn't stop after finding one solution
            - The algorithm needs to continue seraching after finding a valid triplet
            - e.g nums = [-1, 0, 1, 2, -1, -4]

            - There are two valid triplets:
            - [-1, -1, 2]
            - [-1, 0, 1]

        Our MentaL Model for this 3Sum is: For every combination of 3 diferet elements that sums to zero, don't miss any valid triplets, and don't return duplicate triplets.

        - - -
        Brute Force Approach
        Intuition: The simplest way to solve this is to literally try every possible combination of three elements.

        For eg.
        nums = [-1, 0, 1, 2, -1, 4]

        We use three loops:
        i - choose the first number
        j - choose the second number
        k - chooose the third number

        For example:
        At index i:0 -> -1
        At index j:1 -> 0
        At index k:2 -> 1

        So check:
        -1 + 0 + 1 = 0

        So, we found:
        [-1, 0, 1]

        Then, we continue trying other combinations

        The diplicate problem:
        A simple way for the brute-force aproach to handle this is to sort each original array and store them in a set. The set can. recognize that we've alllready seen that combination.

        For e.g: nums = [-1, 0, -1, 2, 1]

        After we have: [-1, 0, 1, 2]

        Algorithm:
        1. Create an empty set called result
        2. Use three nested loops to choose three different indexes
        3. Check whether their values sum to 0
        4. If they do, sort the three values
        5. Convert the triplets to a tuple and add it to a set
        6. After choosing every possible combination, convert the set back to a list

        Pseudocode:
        result = empty set

        For i, from 0 to len of nums -1
            For j, from i + 1 to len of nums -1
                For k, from j + 1 to len of nums - 1

                    if nums[i] + nums[j] + nums[k] == 0
                        triplet = tuple(sorted(nums[i], nums[j], nums[k]))
                        addd result to triplet

        return result as a list

        - - -
        I converted the triplet to tuple because tuples are immutable and hashable, so they can be stored in a set to automatically eliminate duplicate triplets, whereas lists are mutable and unhashable.

        hashable means = Python can give the object a fixed hash value so it can efficiently store and look it up in a set. 

        Time complexity: O(n^3) because we have three nested for loops.

        Space complexity: O(n^2) beacuse the result can hold 0(n^2) unique elements.

        What do we mean? 
        - The importamt question for space complexity is: How many different different triplets could we potentially have to store?
        - As the input geets larger, the number of valid triplets we might have to keep in memory can grow proportional to n^2

        Know this:
        - A triplet has exactly three elements, so storing one triplet takes exactly O(1) space.
        - The O(^2) comes from the maximum number of triplets we could store.

        A simple way to see it:
        - We have n numbers
        - for every choice of the first number, there can be roughly n choices for the second number
        - Once those two are chosen, the third number is determined by the condition: a + b + c = 0

        So roughly:
        n choices * n choices = n^2 possible triplet candidates

        Therefore:
        - 1 triplet -> O(1) space
        - n^2 triplets -> On^2 spaces
            
        - - -

        Optimized Approach (Two pointers and Two sum II technique under the hood)
        Why Optimize?
        The brute force solution checks every combination of three numbers:
        O(n^3)

        With up to 3000 numbers, that's too much work.

        We can reduce this to O(n^2) by:
        1. Soring the array
        2. Fixing one number
        3. Using two pointers to find the other two numbers

        Intuiton:
        We want: a + b + c = 0

        After sorting, if we fix one number 'a', the problem becomes:
        b + c = -a

        And we've already learned how to solve Two Sum on a sorted array using two pointers

        So, the big idea is:
        sort the array, fix one number, then use two pointers to find the other two numbers

        This will change our approach from:
        Three loops -> O(n^3) 
        
        to 
        
        One loop + two-pointer scan -> O(n^2)

        E.g nums = [-1, 0, 1, 2, -1, -4]

        After sorting: [-4, -1, -1, 0, 1, 2]

        If we fix -4, we need:
        b + c = 4

        So, we use two pointers 

        [-4, -1, -1, 0, 1, 2]
              ↑            ↑
            left          right

        if a = -4, we ned two numbers that sum to 4
        - if b + c is too small move left right
        - if b + c is too big, move right left
        - it it equals to zero togethr with a, we found a triplet

        Sorting also makees it possible to skip duplicates

        Algorithm:
        1. Sort nums
        2. Create an empty result list
        3. Loop through each index i
        4. Treat nums[i] as the first number of the triplet
        5. Set:
            - left = i + 1
            - right = len(nums) - 1
        6. While left < right:
            - Calculate total = nums[i] + nums[j] + nums[k]
            - if total == 0:
                - Add the triplet
                - Move both pointers
                - Skip duplicate values
            - If total < 0:
                - Move left forward
            - If total > 0:
                - Move right backward
        7. Skip duplicate values for i as well
        8. Return the result

        Pseudocode:
        sort nums

        result = []

        for i from 0 to n - 1

            if nums[i] is same as previous value:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:

                total = nums[i] + nums[j] + nums[k]

                if total == 0:
                    append [nums[i], nums[j], nums[k]] to result

                    move left forward
                    move right backward

                    skip duplicate values at the left
                    skip duplicate values at the right

                elif if total < 0:
                    move left forward

                else:
                    move right backard

        return result

        Time complexity:
            - Sorting takes O(n log n)
            - Outer loop + two-pointer O(n^2)

            Overall = O(n^2)

        Space complexity: The result storage is output space; excluding the output, the algorithm uses O(1) auxilliary space apart from the sorting implementation's internal space.
        """
        # Brute Force Approach (Used three nested loops)
        result = set()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j +1, len(nums)):

                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                        result.add(triplet)
        
        return [list(triplet) for triplet in result]

        # Optimized Approach (Using a for loop and two pointers)
        nums.sort()
        result = []

        for i in range(len(nums)):
            
            # Skip duplicate first values
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:

                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # Skip duplicate values on the left
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate values on the right
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1

                else:
                    right -= 1

        return result
