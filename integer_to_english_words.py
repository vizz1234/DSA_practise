class Solution:
    def numberToWords(self, num: int) -> str:

        if num == 0:
            return 'Zero'

        d = {
            0: '',
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine',
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen',
            20: 'Twenty',
            30: 'Thirty',
            40: 'Forty',
            50: 'Fifty',
            60: 'Sixty',
            70: 'Seventy',
            80: 'Eighty',
            90: 'Ninety',
            100: 'One Hundred',
            200: 'Two Hundred',
            300: 'Three Hundred',
            400: 'Four Hundred',
            500: 'Five Hundred',
            600: 'Six Hundred',
            700: 'Seven Hundred',
            800: 'Eight Hundred',
            900: 'Nine Hundred'
        }
    
        s_num = str(num)
        n = len(s_num)
        s_num = s_num[::-1]
        s_list = [s_num[i:i+3] for i in range(0, n, 3)]
        s_chunks = [text[::-1] for text in s_list]

        num_placements_order = {0: '', 1: ' Thousand ', 2: ' Million ', 3: ' Billion '}

        final_word = ''

        for idx, chunk in enumerate(s_chunks):

            chunk_num = int(chunk)
            chunk_word = ''

            if chunk_num == 0:
                continue

            if chunk_num in d:
                chunk_word = d[chunk_num]

            else:
                hundreds = (chunk_num // 100) * 100

                if chunk_num % 100 in d:
                    tens = chunk_num % 100
                    ones = 0
                
                else:
                    tens = ((chunk_num % 100) // 10) * 10
                    ones = chunk_num % 10

                chunk_word = d[hundreds] + ' ' + d[tens] + ' ' + d[ones]
            
            chunk_word += num_placements_order[idx]
            final_word = chunk_word + final_word

        return ' '.join(final_word.split())

sol = Solution()
print(sol.numberToWords(12345))