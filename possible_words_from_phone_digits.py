class Solution:
    def possibleWords(self, arr):
        # code here
        keypad = {
            0: '',
            1: '',
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz'
        }
        
        result = []
        def backtrack(index, current):
            if index == len(arr):
                result.append(current)
                return
            letters = keypad[arr[index]]
            for ch in letters:
                backtrack(index + 1, current + ch)
            if letters == '':
                backtrack(index + 1, current)
                
                
        backtrack(0, '')
        return result

sol = Solution()
print(sol.possibleWords([2, 3, 4]))