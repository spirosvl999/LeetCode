class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for i in nums:                                          # Runtime: 6ms & Memory 31.52MB
            if i in hashset:                                    # Used hashmap instead of for loop
                return True                                     # to make this script faster.
            hashset.add(i)  
        return False                                            # Logic first said "Do it with for loop"
                                                                # But with this solution we beat 85.07% of times.
      
                                                                # Complexity = O(N) .
