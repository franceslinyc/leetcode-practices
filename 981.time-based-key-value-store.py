#
# @lc app=leetcode id=981 lang=python3
#
# [981] Time Based Key-Value Store
#

# @lc code=start
class TimeMap:

    # method 1: brute force
    
    def __init__(self):

        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        self.store[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.store:            # Careful! Don't forget self.

            return ""
        
        res = ""
        
        best_time = -1 # 0 works too; -1 is safer

        for time, value in self.store[key]: # Careful! Don't forget self.

            if time <= timestamp and time >= best_time: 

                best_time = time

                res = value

        return res    # Don't need return "" if best_time == -1 else res because res is already initialized as ""


    # # method 2: binary search
    
    # def __init__(self):

    # def set(self, key: str, value: str, timestamp: int) -> None:

    # def get(self, key: str, timestamp: int) -> str:


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end

