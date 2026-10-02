class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        Input: an array of integers where each position represents a day and value is the stock price that day

        prices = [7, 1, 5, 3, 6, 4]
                  0  1  2  3  4  5

        Output: return the maximum profit from exactly one buy followed by one later sell

        For example:
        Buy: price 1
        Sell: price 6

        Profit = 6 - 1 = 5

        Goal: We want sell_price - buy_price to be as large as possible, with one crucial rule:
        The selling price day must come after the buying day.

        So, we cannot simply find the smallest and largest numbers without considering their positions

        Edge Cases:
        1. When prices only decrease -> return 0 (we can never return a negative profit)
            Every possible transaction loses money
            e.g [7, 6, 4, 3, 1]
        
        2. When there is only one day - > return 0
            There is no future day to sell
            e.g [5]

        3. When cheapest prices occurs after the highest price
            e.g [10, 8, 2]
            You cannot say: 10 - 2 = 8
            because that would mean buying at 2 after selling at 10

        4. When we have same prices -> maximum profit is 0
            e.g [5, 5, 5]

        Walkthrough:
        Say we have:
        prices = [7, 1, 5, 3, 6, 4]

        If we buy at 7, possible future sales are:

        7 -> 1 = -6
        7 -> 5 = -2
        7 -> 3 = -4
        7 -> 6 = -1
        7 -> 4 = -3

        Nothing is profitable

        Then co nsider bying at 1:

        1 -> 5 = 4
        1 -> 3 = 2
        1 -> 6 = 5 (best)
        1 -> 4 = 3

        Our maximum profuut becomes 5

        but we would continue checking other remmaining possibilities to make sure nothing beats 5

        - - -

        Brute Force Approach
        Intuition
        To every possible buy day, and for each buy day, try every possible future sell day
        This naturally guarantees that we buy before selling

        Algorithm:
        1. Initialize max_profit to 0
        2. Loop through each index i as the buying day
        3. For each i, loop through every index j after i as the selling day
        4. Calculate prices[j] - prices[i]
        5. Compare that profit with the max_profit, and keep the largger value
        6. After checking every valid pair, return the max_profit

        Pseudocode:
        max_profit = 0

        for i, from 0 to len(prices) - 1
            for j from i _ 1 to len(prices) - 1
                profit = prices[j] - prices[i]

                max_profit = max(max_profit, profit)

        return max_profit

        Time complexity: O(n^2) because for each buying day, we potentially examine every selling day
        Space complexity: O(1) because we did not create any extra data structures

        - - -

        Optimized Approach
        Intuition: 
        We will use two pointers where left represents the buying day and right represents a future selling day.
        Move right forward to find the best profit, and whenever we find a cheaper price, move left there because it gives us a better buying opportunty.

        prices = [7, 1, 5, 3, 6, 4]
                  0  1  2  3  4  5
                     ↑           ↑
                   left        right

        max_profit = 0

        First comparison:
        buy_price -> 7
        sell_price -> 1

        profit = 1 - 7 = -6

        Since 1 < 7, we've found a cheaper buying price

        Move left to right


        Next comparison:
        buy_price = 1
        sell_price = 5

        profit = 5 - 1 = 4

        We keep left at 1 and move right forward


        Next comparison:
        buy_price = 1
        sell_price = 3

        profit = 3 - 1 = 2

        max_profit statys at 4

        Move right forward


        Next comparison:
        buy_price = 1
        sell_price = 6

        profit = 6 - 1 = 5

        max_profit becomes 5

        Move right forward again


        Next comparison:
        buy_price = 1
        sell_price = 5

        profit = 5 - 1 = 4

        max_profit statys at 5


        So, now right moves beyond the array, so we stop

        We return 5

        Algorithm:
        1. set left to index 0 as the buying day
        2. Set right to index 1 as the selling day
        3. I itialize max_profit to 0
        4. While right is within array:
            - if prices[right] > prices[left]:
                - Calculate profiit
                - Update max_profit if the current profit is larger
            - Otherwise move left to right, because we have found a cheaper buying price
            - Move right one position forward
        5. Return max_profit

        Pseudocode:
        left = 0
        right = 1
        max_profit = 0

        while right < len(prices):

            if profit[right] > profit[left]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)

            else:
                left = right

            right += 1

        return max_profit

        Time complexity: O(n) we are iterating the array once while checking for a better profit
        Space complexity: O(1) because we did not create any extra data structure
        """
        # # Brute Force Approach (Nested For Loops)
        # max_profit = 0

        # for i in range(len(prices)):
        #     for j in range(i + 1, len(prices)):

        #         profit = prices[j] - prices[i]

        #         max_profit = max(max_profit, profit)

        # return max_profit

        # Optimized Approach
        left = 0
        right = 1

        max_profit = 0

        while right < len(prices):

            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]

                max_profit = max(max_profit, profit)

            else:
                left = right

            right += 1

        return max_profit
