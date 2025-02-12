class Solution:

    def anagrams(self, arr):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''

        #code here
        d = {}
        output = []
        n = len(arr)
        for i in range(n):
            key = tuple(sorted(arr[i]))
            if key not in d:
                d[key] = []
            d[key].append(arr[i])
        for key, value in d.items():
            output.append(value)
        return output
obj = Solution()
print(obj.anagrams(['act', 'god', 'cat', 'dog', 'tac']))