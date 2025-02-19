#Problem Requirements
"""
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".

Example 1:

Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2"

"""


#Design
"""
Dictionary (key, time) = value
List (Key) index time

"""

#Implementation Problems and Solutions
"""
Didn't think get could be lower than the time, but easy fix
"""

#Code Start
from typing import Dict, List, Tuple

class TimeMap:

    def __init__(self):

        self.time_dict: Dict[Tuple[str, int], str] = {}

        self.key_times: Dict[str, List[int]] = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        pair = (key, timestamp)

        self.time_dict[pair] = value

        if key in self.key_times:
            self.key_times[key].append(timestamp)
        else:
            self.key_times[key] = []
            self.key_times[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:

        pair = (key, timestamp)

        if pair in self.time_dict:
            return self.time_dict[pair]
        
        if key in self.key_times: #Key does exist

            left = 0
            right = len(self.key_times[key]) - 1
            prev = self.key_times[key][left]

            #Time is most recent timestamp
            if self.key_times[key][right] < timestamp:
                prev = self.key_times[key][right]
                pair = (key, prev)
                return self.time_dict[pair]

            #Key never happend before timestamp
            if prev > timestamp:
                return ""

            #Binary search
            while left <= right:

                mid = left + (right - left) // 2
                
                if self.key_times[key][mid] < timestamp:
                    prev = self.key_times[key][mid]
                    left = mid + 1
                else: #Time too big move right towards left
                    right = mid - 1
            
            pair = (key, prev)
            return self.time_dict[pair]

        return "" #Key does not exist
    

        


#Test Code - sometimes needs to change depending on the data type or constraints of output and answer
def Test(id, output, answer):
    try:
        assert output == answer
        print(f"Test {id} passed")
    except:
        print(f"Test {id} failed got {output} expected {answer}")

timemap = TimeMap()

timemap.set("love", "high", 10)
timemap.set("love", "low", 20)

