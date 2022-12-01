
import random

class random_number:
    
    def generate(amount: int, minRange: int, maxRange: int):
        ans = []
        
        if amount < 0:
            return "Amount must be over 0"
        elif minRange > maxRange:
            return "minRange must be smaller than maxRange"
        
        for i in range(amount):
            ans.append(random.randint(minRange, maxRange))

        for i in ans:
            if type(i) != int:
                return

        if len(ans) < 1:
            return

        return ans


print(random_number.generate(5, 1, 100))