#User function Template for python3

class Solution:
    def convertToWords(self, n):
        # code here
        if n == 0:
            return "Zero"
        ones = {
            0: "",
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine"
        }
        
        tens = {
            0: "",
            2: "Twenty",
            3: "Thirty",
            4: "Forty",
            5: "Fifty",
            6: "Sixty",
            7: "Seventy",
            8: "Eighty",
            9: "Ninety"
        }
        
        ten_plus = {
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen"
        }
        
        hundreds = {
            0: "",
            1: "One Hundred",
            2: "Two Hundred",
            3: "Three Hundred",
            4: "Four Hundred",
            5: "Five Hundred",
            6: "Six Hundred",
            7: "Seven Hundred",
            8: "Eight Hundred",
            9: "Nine Hundred"
        }
        
        s = str(n)
        len_s = len(s)
        
        count = 0
        result = ''
        while count < len_s:
            word = ''
            if count < 3:
                flag = ''
            elif count < 6:
                flag = 'Thousand'
            elif count < 9:
                flag = "Million"
            else:
                flag = "Billion"
            cur_3 = s[-3:]
            s = s[:-3]
            count += len(cur_3)
            if int(cur_3) == 0:
                continue
            # print(cur_3, count)
            word = []
            if len(cur_3) == 3:
                word.append(hundreds[int(cur_3[0])])
                if cur_3[1] == '1':
                    word.append(ten_plus[int(cur_3[1:])])
                else:
                    word.append(tens[int(cur_3[1])])
                    word.append(ones[int(cur_3[2])])
            elif len(cur_3) == 2:
                if cur_3[0] == '1':
                    word.append(ten_plus[int(cur_3)])
                else:
                    word.append(tens[int(cur_3[0])])
                    word.append(ones[int(cur_3[1])])
            else:
                word.append(ones[int(cur_3)])
            words = " ".join(word)
            words += ' ' + flag
            result = words + ' ' + result
        return " ".join(result.split())
        
sol = Solution()
print(sol.convertToWords(123456789))