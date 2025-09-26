class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            l = i + 1
            r = len(numbers) - 1
            temp = target - numbers[i]
            while l <= r:
                mid = l + (r - l)//2
                if numbers[mid] == temp:
                    return [i+1 , mid+1]
                elif numbers[mid] < temp:
                    l = mid + 1
                else:
                    r = mid - 1                                              # Runtime: 50 ms // Beats 5.02%
        return []                                                            # Memory: 18.47 // Beats 90.20%
