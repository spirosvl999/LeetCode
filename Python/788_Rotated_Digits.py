class Solution:
    def rotatedDigits(self, n: int) -> int:
        # Mapping for digits after rotation
        rotate = {
            '0': '0', '1': '1', '8': '8',
            '2': '5', '5': '2', 
            '6': '9', '9': '6'
        }
        
        def is_good(num: int) -> bool:
            s = str(num)
            rotated = []
            changed = False
            for c in s:
                if c not in rotate:
                    return False
                rotated_digit = rotate[c]
                rotated.append(rotated_digit)
                if rotated_digit != c:
                    changed = True
            
            return changed
        
        count = 0
        for x in range(1, n + 1):
            if is_good(x):
                count += 1
        
        return count
