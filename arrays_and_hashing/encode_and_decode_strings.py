class Solution:
    """
    Input: 
        For encode: a list of strings
        e.g strs = ["Hello", "World"]

        For decode: a string produced by encode
        e.g "some encoded string"

    Output:
        encode() should turn: ["Hello", "World"] into one string

        The important requirement is:
        decode(encode(strs)) == strs

        the original list must be constructed exactly.

    What makes this problem tricky?

    We need to somehow combine multiple strings into one string

    A first thought might be:

    "Hello" + "#" + "World" -> "Hello#World"

    Then, we split by "#" and we'll have: "Hello" + "World"

    But, it's possible that any of those words can contain any of the 256 ascii characters.

    Key idea:

    Instead of using a character as a seperator, we can store the length of each string before the string itself.

    E.g: "["Hello" + "World"]

    "Hello" has length of 5
    "World" has length of 5

    We could encode it as "5#Hello5#World" and decoding becomees simple.

    We read 5 and that tells us: The next 5 characters belong to the first string
    We read 5 again and that tells us the next 5 characters belong to the second string

    The result : ["Hello", "World"]

    And it doesn not matter what each word contains because we're using the length to determine exactly how many characters belong to each string.

    Edge cases:
    1. Empty string - > return [""]
        e.g [""] 
        encode as -> 0#
        decode as -> [""]

    2. Multiple empty strings, we need to preserve all strings, including their positiions
        e.g ["", "", "Hello"]
        encode as -> 0#0#Hello
        decode as -> ["", "", "Hello"]

    3. Strings containing our delimiter
        e.g ["Hello#World", "Test"]
        The # inside the first string should not confuse our decoder
        This is exactly why we are using length

    4. Strings containg numbers
        e.g ["123", "45"]
        The decoder can't simply assume numbers are seperators or lengths based on their appearance.
        It needs to know where the length metadata ends and where the actual string begins.

    5. Empty list
        e.g []
        encode as -> []
        decode as -> []

        This is important because there are no strings at all to encode

    - - -

    Brute Force Approach:
    Intuition:
    - To encode a list of strings into a single string, we need a way to store each string so that we can later seperate them correctly during decoding
    - A simple and reliable strategy is to record the length of each string first, followed by a special seperator, and then append all the strings together
    - During decoding, we can read the recorded lengths to know exactly how many characters to extract for each original string
    - This avoids any issues with special characters, commas, or symbols inside the strings because the lengths tell us precisely where each string starts and ends

    Algorithm:
    Encoding:
    1. Create an empty string to store encoded result
    2. Go through each string in strs
    3. For the current string, replace every # character with ##
    4. Add escaped string to the encoded result
    5. Add a single # after it to mark the end of that string
    6. Continue till every string has been processed
    7. Return the encoded string

    Decoding:
    1. create an empty list called result
    2. We start reading the encoded string from left to right
    3. Build the curremt decoded string one character at at time
    4. If the curent character is not #, add it too the current string
    5. If the current charactre is #, look at the next character
        - If the next charctaer is also #, this represents an original #, so add one # to the current string and skip both characters
        - Otherwise, the single # is our seperator, so finish the curremt string and add it to result
    6. Continue u till the entire encoded string has been processed
    7. Return result

    Pseudocode:
    Encode:

    create an empty encoded string

    for each string in strs:
        replace every '#' in the string with '##'
        add the escaped string to encoded
        add '#' as the seperator

    return encoded
    
    Decode:

    create an empty result
    create an empty current string

    set i = 0

    while i is less than the length of encoded string:

            if current character is '#':

                if the next character is also '#':
                    add '#' to the current string
                    move i forward by 2

                otherwise:
                    add the current string to result
                    reset current string
                    move i forward by 1

            otherwise:
                add current character to current string
                move i forward by 1

    return result

    Time complexity: O(n) where n is the total number of characters across all strings
    Space complexity: O(n) for the encoded string and the decoded result

    - - -

    Optimized Approach(Using the length of each string and a unique character as a seperator)

    Instead of choosing a seperator and worrying about wether that character appears inside the strings, we'll encode the length of each string + a seperator + the string itself

    For example:
    strs = ["Hello", "World"]

    encode: "5#Hello5#World"

    With this, the decoder doesn't need to search for where a string ends.
    It already knows that the next number says exactly how many characters belong to this string.

    Algorithm:
    Encode:
    1. Initialize an empty result builder (or list of string parts).
    2. For each string in the list
        - Compute its length
        - Append "length#string" to the builder
    3. Return the final encoded string

    Decode:
    1. Initialize an empty result list and set i = 0
    2. While i is less than the length of the encoded string:
        - Move a pointer j forward until it finds '#' - this segment represents the length
        - Convert the substring s[i:j] into an integer length
        - Move i to the character right after '#'
        - Extract the next length characters - this is the original string
        - Append the extracted string to the result list
        - Move i forward by lengt to continue decoding the next segment
    3. Return the result list

    Time complexity:O(m +n) for each encode() and decode() function calls
    Space complexity:O(m + n) for each encode and decode function calls
    """
    # # Brute force Approach (Straighforward Approach)
    # def encode(self, strs: List[str]) -> str:
    #     encoded = ""

    #     for s in strs:
    #         escaped = s.replace("#", "##")
    #         endoded += escaped + "#"
        
    #     return encoded
        

    # def decode(self, s: str) -> List[str]:
    #     result = []
    #     current = ""

    #     i = 0

    #     while i < len(s):
    #         if s[i] == "#":

    #             if 1 + 1 < len() and s[i + 1] == "#":
    #                 current += "#"
    #                 i += 2

    #             else:
    #                 result.append(current)
    #                 current = ""
    #                 1 += 1

    #         else:
    #             current += s[i]
    #             i += 1

    #     return result

    ####################################################

    # Optimized Appproach (Using the length of each string and a unique character as a seperator)
    def encode(self, strs: List[str]) -> str:
        result = []

        for s in strs:
            length = len(s)
            result.append(str(length) + "#" + s)

        return "".join(result)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            # Find the "#" seperator
            while s[j] != "#":
                j += 1

            # Get the length of the string
            length = int(s[i:j])

            # Move past "#"
            i = j + 1

            # Extracty the string using its length
            string = s[i:i + length]
            result.append(string)

            # Move to the beginning of the next encoded string
            i += length

        return result
