class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        """
        Input: nums - An unsorted list of integers

        Output: int - the length of the longest element consecutive sequence

        Goal: Given an array of integers, look at how many numbers that consecutively follow each other and return their length

        Edge Cases:
        1. An empty array e.g [] -> return 0
        2. An array that contains one element e.g [5] -> return 1
        3. No consecutive numbers eg. [10, 20, 30] - > return 1
        4. nums[i] can either be zero, negative or opositive. We should be able to handle that.
        5. Duplicates shouldn't increase the length e.g [1, 0, 1, 2] ->  We only need to consider unique appearances.
       
        Walkthrough:
        Example 1: 
        nums = [100, 4, 200, 1, 3, 2]
        long_cons_seq = [1, 2, 3, 4]
        len(long_cons_seq) = 4

        return 4

        Example 2:
        nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
        long_cons_seq = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        len(long_cons_seq) = 9

        return 9

        Example 3:
        nums = [1, 0, 1, 2]
        long_cons_seq = [0, 1, 2]
        len(long_cons_seq) = 3

        return 3

        Example 4:
        nums = []
        long_cons_seq = []
        len(long_cons_seq) = 0

        return 0

        Example 5:
        nums = [-1, -2, -7, 5, 2, 1, 3, 4, 0, 12, 2, 5]
        long_cons_seq = [-2, -1, 0, 1, 2, 3, 4, 5]
        len(long_cons_seq) = 8

        return 8

        - - -

        Brute Force Approach (Basic Array Traversal)
        Intution: The straightforward idea here is for every number, to to build a consecutive sequence rom that number.

        For example: nums = [100, 4, 200, 1, 3, 2]

        longest = 0

        Start with 100
        Does 101 exist in the array -> No

        length = 1

        Move to 4
        Does 5 exist in the array -> No
        
        length = 1
        
        Move to 200
        Does 201 exist in the array? No
        length = 1

        Move to 1
            Des 2 exist in the array? Yes
            So, we have now: [1, 2]
            length = 2

            Does 3 exist in the array? Yes
            So, we have: [1, 2, 3]
            length = 3

            Does 4 exists in the array? Yes
            So, we have: [1, 2, 3, 4]
            length = 4

            Does 5 exist in the array? No

            We find the max(longest, length)
                        max(0, 4)
                        
        We return longest = 4

        Move to 3 and so on...

        The problem here is that we keep revisting numbers that we have vsited before and we kepp building consecutive sequences that overlap.

        Algorithm:
        1. Initialize longest = 0
        2. Loop through every number in the array
        3. Treat the current number as the beginning of a possible consecutive sequence
        4. Set the current seqy=uence length to 1
        5. Look for the longest consecutive number which is current + 1 by scanning the array
        6. If the next number exists, increase the current sequence length by 1, and continue looking for the next number
        7. If the number does not exists, stop building the curret sequence
        8. Update longest if the current sequence is longer
        9. Repeat this process for every number in the array, 
        10. Return longest

        Pseudocode:
        longest = 0

        for each num in nums:

            current = num
            length = 1

            while num + 1 in nums:
                current +=  1
                length += 1

            longest = max(longest, lenth)

        return longest

        Time complexity: O(n^2) because we loop through all n numbers, and for each n number, we may search oll n numbers again to find its consecutive sequence.
        Space complexity: O(1) because we only created a few variables and no extra data structure.

        - - -

        Optimized Approach
        Intution: The main problem is this current + i ums line in the brute force approach.
        Because nums is a list, Python may scan the entire array to determine wheher a number exists

        We want to make the checking faster?  

        So, we store the numbers in a set which has an O(1) lookup time.

        Now, instead of starting a sequence for every numnber, we only build a sequence when we find the beginning of one.
        
        Let's visualize this aproach with these numbers on the number line:

        1, 2, 3, 4           100             200
        <---------------------------------------->
                  ⬆

        Let's say we want to build a consecutive sequence from the numbers on the number line:
        
        Starting at 1 : Can we build  assequence from it? Yes, because it has no left neighbor which is 0
        So we have = [1, 2, 3, 4]

        We move to 2: Can we build a sequence from it? No
        Because the left neighbor 1 exists. So, 2 is not the start of a sequence.

        Same with 3

        Same with 4

        At 100: Can we build  assequence from it? Yes, becuase 99; the left neghbor does not exist.
        So, we have:  [100]

        At 200: Can we build  assequence from it? Yes, becuase 199; the left neghbor does not exist.
        So, we have:  [200]

        So, that same idea is what we apply in our optimized approach.

        We only build a squence if current - 1 exists in the set that we have build from nums.

        - - -
        
        nums = [100, 4, 200, 1, 3, 2]

         nums_set = {100, 4, 200, 1, 3, 2}

        We start building a sequence:

        Step 1:
        100 -> 1
        
        Step 2:
        We jump 4 because 4 - 1 = 3 exists in the set

        Step 3:
        200 -> 1

        Step 4:
        1 -> 2 -> 3 -> 4

        Step 5:
        We jump 3 because 3 - 1 exists in the set

        Step 6:
        We jump two because 2 - 1 exists in the set

        And we return 4 which is the longest consecutive sequence

        Algorithm:
        1. Initialize longest = 0
        2. Create a set of nums
        3. Loop throgh each number in the array
        4. If nums - 1 exists in the set, continue
        5. Start building a sequence from that number
        6. initialize the length of the current sequence to be 1
        7. While current + 1 exists in the set
            - Increase current by 1
            - Increase length of the consecutive sequence by 1
        8. Repeat this till no more next number 
        9. Update longest by finding the maximum between longest and latest consecutive sequence length
        10. Retuen longest

        Pseudocode:
        nums_set = set(nums)

        longest = 0

        for num in nums:

            if nums - 1 in nums_set:
                continue

            current = num
            length = 1

            while current + 1 in nums_set:
                current +=1 
                length += 1

            longest = max(longest, length)

        return longest

        Time complexity: O(n) because 
            - We only build a sequence when we find its starting number
            - Across the whole algporithm, the sequence building work is bounded by the number of elements
        Space complexity: O(n) because we created a set which we used to store the numbers

        """
        # # Brute Force Approach (Basic Array Traversal)
        # longest = 0

        # for num in nums:

        #     current = num
        #     length = 1

        #     while current + 1 in nums:

        #         current += 1
        #         length += 1

        #     longest = max(longest, length)

        # return longest

        # Optmized approach (Hash Set)
        nums_set = set(nums)

        longest = 0

        for num in nums:

            if num - 1 in nums_set:
                continue

            current = num
            length = 1

            while current + 1 in nums_set:
                current += 1
                length += 1

            longest = max(longest, length)

        return longest
 