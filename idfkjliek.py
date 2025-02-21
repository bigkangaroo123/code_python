def number_to_words(n):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    thousands = ["", "thousand", "million", "billion"]
    
    def two_digit_words(num):
        if num < 10:
            return ones[num]
        elif num < 20:
            return teens[num - 10]
        else:
            return tens[num // 10] + (" " + ones[num % 10] if num % 10 != 0 else "")
    
    def three_digit_words(num):
        if num < 100:
            return two_digit_words(num)
        return ones[num // 100] + " hundred" + (" " + two_digit_words(num % 100) if num % 100 != 0 else "")
    
    if n == 0:
        return "zero"
    
    words = []
    chunk_index = 0
    while n > 0:
        chunk = n % 1000
        if chunk > 0:
            words.append(three_digit_words(chunk) + (" " + thousands[chunk_index] if thousands[chunk_index] else ""))
        n //= 1000
        chunk_index += 1
    
    return " ".join(reversed(words)).strip()

# Example usage
num = int(input("Enter a number: "))
print(number_to_words(num))