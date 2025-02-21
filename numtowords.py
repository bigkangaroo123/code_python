def numtowords(n):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    tens = ["", "", "twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    powers = ["", "million", "billion" "trillion"]
    listnum = list(map(int, n))
    strnum = []
    #max: 2147483648
    def p1(chunk):
        strchunk = []
        strchunk.append(ones[(chunk[0])])
        if len(chunk) == 3:
            if chunk[0] != 0:
                strchunk.append(ones[chunk[0]] + "hundred")
            if chunk[1] != 0 or chunk[2] != 0:
                strchunk.append("and")
            
            chunk = chunk[1:]
        
        if len(chunk) == 2:
            if chunk [0] == 0 and chunk[1] == 0:
                strchunk.append("thousand")

            elif chunk[0] == 1:
                if chunk[1] == 0:
                    strchunk.append("ten")
                else:
                    strchunk.append(teens[chunk[1]])
                
            else:
                strchunk.append(tens[chunk[0]])
                if chunk[1] != 0:
                    strchunk.append(ones[chunk[1]])


        elif len(chunk) == 1:
            if chunk[0] != 0:
                strchunk.append(ones[chunk[0]])

        return " ".join(strchunk)
    
    if len(n) >= 9:
        