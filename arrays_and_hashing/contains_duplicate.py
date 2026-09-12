## Question 217.Contains Duplicate
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Input: nums - an array of integers

        Output: return a boolean
            - True if nums contains a duplicate
            - False if efrey elemenet is distinct

        Goal: return a boolean; True if the array contains a duplicate and False otherwise

        Edge cases:
        1. Empty array -> return False
            e.g nums = []

        2. Array containing one element -> return False
            e.g nums = [5]

        3. Array containing distinct numbers -> return False
            e.g nums = [1, 2, 3, 4]

        4. Array containing duplicates - return True 
            e.g nums = [1, 2, 3, 1]

        Walkthrough:

        nums = [1, 2, 3, 1]
                0  1  2  3
                   ↑

        At index 0: have I seen 1 before? No
        At index 1: have I seen 2 before? No
        At index 2: have I seen 3 before? No
        At index 3: have I seen 1 before? Yes

        We return True

        - - -

        Brute Force Approach (Basic Array Traversal)
        intuition:
        - We copare every number with the other number and check wether any of them are equal
        - Compare nums[i] with nums[i + 1], nums[i + 2], nums[i +3]... and so on

        For example:
        nums = [1, 2, 3, 3]
                0  1  2  3
                ↑
                i
                   ↑
                   j

        At index 0:
        Compare 1 with 2
        Compare 1 with 3
        Compare 1 with 3

        At index 1:
        Compare 2 with 3
        Compare 2 with 3

        At index 2:
        Compare 3 with 3

        And 3 -> 3 is a duplicate!

        We return True

        Algorithm:
        1. Iterate through the array using two nested loops, and compare all possible pairs of distinct indices
        2. if any pair of elements has the same value, return True
        3. If all the pairs of elements has distinct value, return False

        Pseudocode:
        for i, from 0 to length of nums -1
            for j, from 1 + 1 to length of nums - 1

                if i equals j
                    return True
        return False

        Time complexity: O(n^2) because we potentially compare every pair of elements
        Space complexity: O(1) because no extra data structure was created

        - - -

        Optimized Approach (Using a Hash Set)
        Intuition:
        - Can we save time and avoid comparing every number against every number?
        - We need to avoid repeatedly visiting numbers we have visited before.
        - We need a data structure to store every number we have visited before

        Set is the perfect data structure

        Say we have nums = [1, 2, 3, 3]

        set = {}

        nums = [1, 2, 3, 3]
                0  1  2  3
                ↑
             pointer

        At index 0: have I seen 1 before? No
            set = {1}
        At index 1: have I seen 2 before? No
            set = {1, 2}
        At index 2: have I seen 3 before? No
            set = {1, 2, 3}
        At index 3: have I seen 3 before? Yes

        Return True

        Algorithm:
        1. Initialize an empty hash set to store seen values
        2. Iterate through each number in the array
        3. For each number:
            - If it already exists in the set, return True because a duplicate has been found
            - Otherwise, add it to the set
        4. If the loop finishes without finding a duplicate, return False

        Pseudocode:
        Create an empty hash set

        for i, from 0 to length of nums - 1
            if i in seen
                return True
            
            add i to seen

        return False

        Time complexity: O(n) because we iterate through the array exactly once
        Space complexity: O(n) because we created an extra data structure; seen.
        """
        # # Brute Force Approach (Basic Array Traversal)
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        # Optmized Approach
        seen = set()

        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen.add(nums[i])

        return False
