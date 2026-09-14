### Two Sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Input : 
        - nums: an array of integers
        - target: an integer

        Output: an array that contains the indices of the two numbers whose sum equals target

        Goal: Find the two different indices i and j where nums[i] + nums[j] == target and return those indices. 

        We have assured that every input has exactly one pair of indices that satisfy the condition. So, we don't need to worry about inputs having more than one valid pair.

        Edge cases:
        - When we have a minimum array size: 
        e. g if nums = [5, 5] and target = 10
        
        return [0, 1]
        
        This also proves the i != j constraint (which means that the values can be same but indices must be different)

        - When we have negative numbers
        e.g nums = [-3, 4, 2] and target = -1

        return [0, 2]

        our solution therefore must work with negative numbers

        - When pairs isn't adjacent
        e.g nums = [4, 5, 6] and target = 10

        return [0, 2]

        The two numbers don't have to be close to each other, so we can't just look at neighboring elements.


        Walkthrough:
        Example 1:

        nums = [3, 4, 5, 6]
        target = 7

        nums = [3, 4, 5, 6]
                0  1  2  3
                ↑  ↑
                i  j

        at index[0] -> 3

        7 - 3 = 4

        Now, let's look for 4: 
        4 is at index[1]

        so we return [0, 1]


        What if the first number didn't work:

        Example 2:
        
        nums = [3, 4, 5, 6]
        target = 9

        nums = [3, 4, 5, 6]
                ↑        ↑
                i        j

        Start at index[0] -> 3

        9 - 3 = 6

        Let's find 6, and we see 6 at index[3]

        3 + 6 = 9

        return [0, 3]

        - - -

        Brute Force Approach
        Intuition:
        We try every posiible pair, for each i, we look at the next index after it:

        nums = [3, 4, 5, 6]

        We'll do:

        3 + 4
        3 + 5
        3 + 6
        
        4 + 5
        4 + 6

        5 + 6

        as soon as one equals target, we return the indices.

        Algorithm:
        1. Start with index i = 0
        2. Start next at index i + 1
        3. Compare nums[i] + nums[j] with target
        4. if they eqaual target, return [i, j]
        5. Otherwise, move j forward
        6. Once j finishes, move i forward
        7. Continue until we find the pair

        Pseudocode:
        for i from 0 to length of nums - 1
            for j from i + 1 to length of nums - 1

            if nums[i] + nums[j] = target
                return [i, j]

        Time complexity: O(n * n) = O(n^2) because we are using a nested for loop
        Space complexity: O(1) because no extra data structures created

        - - -

        Optimized Approach (Using a hash map)

        Intuition:

        nums = [3, 4, 5, 6]
        target = 9

        When we start at index[0] -> 3

        9 - 3 = 6

        instead checking the numbers after it, we can ask, have i see this number 6 before?

        So, we use a hash map or dictionary to help us remember.

        For example:

        {
            3: 0,
            4: 1,
            5: 2,
            6: 3
        }


        Let's say:
        nums = [3, 4, 5, 6]
        target = 7

        seen = {}

        nums = [3, 4, 5, 6]
                0  1  2  3
                ↑

        At index[0]: 3

        target - current -> 7 - 3 = 4

        Is 4 in seen? No
        So, we store 3 in seen:
        seen =
                {
                    3:0
                }

        At index[1]: 4

        target - current -> 7 - 4 = 3
        Is 3 in seen? Yes

        We return [0, 1]

        Algorithm:
        1. Create an empty hash map called seen
        2. Iterate through nums using its index and value
        3. Calculate the complement
            complement = target - current number
        4. Check whether the complement is in seen
        5. if it exists, return the stored index and the current index
        5. If not, add current number to seen
        6. continue

        Pseudocode:
        create an empty hash map called seen

        for each index i and number num in nums

            complement = target - num

            if complement in seen
                return [seen[complement, i]]

            add num and its index i to seen

        Time
        Space
        """
        # Brute Force Implementation
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # Python Implementation
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i
