#
# @lc app=leetcode id=271 lang=python3
#
# [271] Encode and Decode Strings
#

# @lc code=start
class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        
        res = ""

        for s in strs: 

            res += str(len(s)) + "#" + s 

        return res


    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """

        res = []

        i = 0                    # i points at start of the current block

        while i < len(s): 

            j = i                # Use j to search for the '#' separator

            while s[j] != "#":   # Can handle multi-digit length, i.e., 12#Hello...

                j += 1

            length = int(s[i:j]) # Read the string length 
            
            i = j + 1            # Move i to point at start of the actual string s 

            j = i + length       # Move j to the start of the next block 

            res.append(s[i:j])   # Extract characters

            i = j                # Move i to point at start of the next block
        
        return res
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
# @lc code=end

