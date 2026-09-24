class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Input: nums - an array of integers

        Output: answer - an array of integers where answer[i] is the product of every element except nums[i]
        e.g 
        nums = [1, 2, 3, 4]
        answer = [24, 12, 8, 6]

        at index 1:
        nums[1] = 1 * 3 * 4 = 12

        Goal: For every position, calculate the product of everything to its left and everything to its right

        And we have two importatnt restrictions:
        - No division
        - Must be in O(n) time

        Edge cases:
        - When is no zero in the nums array
            - The product is straightforward
            e.g nums = [1, 2, 3, 4]
                answer = [24, 12, 8, 6]

        - When there is a zero in the nums array 
            - The zero in the array gets the product of every other element
            - All other elements gets the product of zero since they include zero in the products
            e.g nums = [-1, 1, 0, -3, 3]
                answer = [0, 0, 9, 0, 0]

        - When an array have negative elements
            e.g nums = [-1, 1, 0, -3, 3]
            - so we need to find a way to handle negative products

        
        Wakthrough:
        nums = [1, 2, 3, 4]
                0  1  2  3
                         ↑

        At index 0:
            left = 1
            right = 2 * 3 * 4 = 24
            answer[0] = 1 * 2 * 3 * 4 =24

        At index 1:
            left = 1
            right = 3 * 4
            answer[1] = 1 * 3 * 4 = 12

        At index 2:
            left = 1 * 2
            right = 4
            answer[2] = 1 * 2 * 4 = 8

        At index 3:
            left = 1 * 2 * 3
            right = 1
            answer[3] = 1 * 2 * 3 * 1 = 6

        Brute Force Approach:
        Intuition:
        To get the product of all the elements except the particular position that I am pointing at starting from left to right.
        i.e For every i, loop through the entire array and multiply everything except nums[i]

        Algorithm:
        1. Create an empty answer array
        2. Loop through each index i in nums
        3. For each element, start a product value at 1
        4. Go through each index j in nums
        5. If i and j are different, multiply nums[j] and product
        6. After going through everything, append product to answer
        7. Return answer

        Pseudocode:
        answer = []

        for i, from 0 to length of nums - 1
            product = 1

            for j, from 0 to length of nums - 1
                if i and j are not equal
                    product = nums[j] * product

            append product to answer

        return answer

        Time complexity: O(n^2) because we are looping and iterating through the elements in nums exatly twice
        Space complexity: O(n) becuase of the extra data structure created; answer

        - - - 

        Optimized Approach (Prefix and Suffix)
        Intuition:

        The key insight here, for every index:

        annswer[i] = product of everything LEFT of i * product of everything RIGHT of i

        For example:

        nums = [1, 2, 3, 4]

        at index 2:

        [1, 2, 3, 4]
               ↑
               i

        Everything to the left: 1 * 2 = 2
        Everything to the rigght: 4

        Therefore answer[2] = 1 * 2 * 4 = 8


        LET'S VISUALIZE THE WHOLE THING

        PREFIX PRODUCTS:
        For each position, calculate the product before it:

        nums = [1, 2, 3, 4]

        prefix = [1, 1, 2, 6]

        How come?

        at index[0]:
        nothing to the left -> 1

        at index[1]:
        we have 1 to the left -> 1

        at index[2]:
        we have 1 * 2 to the left -> 2

        at index[3]:
        we have 1 * 2 * 3 to the left -> 6


        Suffix products:

        For each position, calculate the product after it
        nums = [1, 2, 3, 4]

        suffix = [24, 12, 4, 1]

        How is that?

        at index[3]:
        we have nothing after it -> 1

        at index[2]:
        we have 4 after it -> 4

        at index[1]:
        we have 3 * 4 after it -> 12

        at index[0]:
        we have 2 * 3 * 4 after it -> 24

        Then, multiiply prefix * suffix:
        prefix: [1,  1,  2, 6]
        suffix: [24, 12, 4, 1]
                 ↓   ↓   ↓  ↓
        answer: [24, 12, 8, 6]

        Algorithm:
        1. Get the length of nums
        2. Create an empty answer array filled with 1s
        3. Create an empty prefix arrray filled with 1s
        4. Create an empty suffix array filled with 1s
        5. Traverse nums from left to right and calculate the product of every element before each index. Store these products in prefix
        6. Traverse nums from right to left and calculate the products of every element after each index. Store those products in suffix
        7. For every index, multiply the corresponding prefix and suffix values to get the product of everything except nums[i]
        8. Return answer

        Pseudocode:
        n = len(nums) 

        answer = [1] * n
        prefix = [1] * n
        suffix = [1] * n

        forr i, from 1 to n - 1
            prefix[i] =  prefix[i - 1] * nums[i - 1]

        for i, from n - 2 down to 0
            suffix[i] = suffix[1 + 1] * nums[i + 1]

        for i from 0 to n - 1:
            anwer[i] = prefix[i] * suffix[i]

        Return answer

        Time  complexity = O(n) because we make two passes through the array i.e O(n) + O9n = O(n)
        Space complexity = O(n) because the sum of the extra data structures is O(n) + O(n) + O(n) = O(n)
     
         - - -

        Follow Up O(1) space

        We actually don't need a seperate prefix array or a seperate suffix array 
        The output array itself can store the prefix products

        answer = prefix products

        then we make a second pass from right, and multiply prefix into answer

        Example:
        nums = [1, 2, 3, 4]

        First pass:

        answer: [1, 1, 2, 6] <- prefix information

        Second pass:
        We walk from right to left while maintaining one variable
        suffix = 1

        At index[3]:
        answer[3] = answer[3] * suffix
        answer[3] = 6 * 1

        suffix = suffix * nums[3]
            = 1 * 4 = 4

        At index[2]:
        answer[2] = answer[2] * suffix
        answer[2] = 2 * 4 = 8

        suffix = suffix * nums[2]
            = 4 * 3 = 12

        At index[1]:
        answer[1] = answer[1] * suffix
        answer[1] = 1 * 12 = 12

        suffix = suffix * nums[1]
            = 12 * 2 = 24

        at index[0]:
        answer[0] = answer[0] * suffix
        answer[0] = 1 * 24 = 24

        suffix = suffix * nums[0]
            = 24 * 1 = 24

        Final answer = [24, 12, 8, 6]

        Algorithm:
        1. Create an output array filled with 1
        2. Traverse the array from left to right
        3. For each position, store the product of all elements that appear before that position in the output arrray
        4. Traverse the array from right to left
        5. Keep track of the product of all elements to the right using a suffix variable
        6. Multiply the current output value by the suffix product
        7. Update the suffix product using the current number
        8. Return the output array

        Pseudocode:
        Create answer array filled with 
        
        prefix = 1

        For each index from left to right:
            answer[index] = prefix

        suffix = 1

        For each index from right to left:
            answer[index] = answer[index] * suffix
            
            suffix = suffix * nums[index]

        Return answer

        Time complexity: O(n) because we are making two passes through the array, therefore O(n) + O(n) = O(n)
        Space complexity: O(1) since we aren't considering the returned output which is answer
       
        """
                  
        #. Brute Force Approach (Usinh nested loops)
        answer = []

        for i in range(len(nums)):
            product = 1

            for j in range(len(nums)):
                if i != j:
                    product *= nums[j]

            answer.append(product)

        return answer


        # Optimized approach (prefix and suffix)
        n = len(nums)

        answer = [1] * n
        prefix = [1] * n
        suffix = [1] * n

        for i in range (1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        for i in range(n):
            answer[i] = prefix[i] * suffix[i]

        return answer

        # Optmized Approach B - Using O(1) space
        answer = [1] * len(nums)

        prefix = 1

        for i in range(len(nums)):
            answer[i] = prefix
            prefix = prefix * nums[i]

        suffix = 1

        for i in range(len(nums) - 1, -1, -1):
            answer[i] = answer[i] * suffix
            suffix = suffix * nums[i]

        return answer

        """
        The big picture:
        - The first pass puts the left-side products into answer:
        answer = [1, 1, 2, 6]

        - The second pass multiples each of those by the right-side product:
                    prefix     suffix
        index 0:       1    *    24   =  24
        index 1:       1    *    12   =  12
        index 2:       2    *     4   =   8
        index 3:       6    *     1   =   6
        """
