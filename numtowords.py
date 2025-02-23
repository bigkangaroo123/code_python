def numtowords(n):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    tens = ["", "", "twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    powers = ["", "million", "billion", "trillion"]
    #max: 2147483648
    def p1(chunk):
        strchunk = []
        if len(chunk) == 3:
            if chunk[0] != 0:
                strchunk.append(ones[chunk[0]] + " " + "hundred")
            
            chunk = chunk[1:]
        
        if len(chunk) == 2:
            if chunk[0] == 1:
                strchunk.append(teens[chunk[1]])
            else:
                if chunk[0] != 0:
                    strchunk.append(tens[chunk[0]])
                if chunk[1] != 0:
                    strchunk.append(ones[chunk[1]])


        elif len(chunk) == 1:
            if chunk[0] != 0:
                strchunk.append(ones[chunk[0]])

        return " ".join(strchunk)
    
    def split(n):
        chunks = []
        while n>0:
            chunks.append(n%1000)
            n//=1000

        return chunks
    
    if n == 0:
        return "zero"
    
    chunks = split(n)
    words = []
    
    for i, chunk in enumerate(chunks):
        if chunk > 0:
            words.append(p1(list(map(int, str(chunk).zfill(3)))) + (" " + powers[i] if powers[i] else ""))
    
    return " ".join(reversed(words)).strip()

n = int(input())
print(numtowords(n))
#not working proerpyl