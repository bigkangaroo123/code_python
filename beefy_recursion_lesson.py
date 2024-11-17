def pow(base, exponent, tail=1):
    if exponent == 0:
        return 1
    elif exponent == 1:
        return base
    else:
        return base * pow(base, exponent - 1, tail*base)

def palindrome(word) -> bool:
    if len(word) <= 1:
        return True
    elif len(word) <= 3:
        return word[0] == word[-1]
    elif word[0] == word[-1]:
        return palindrome(word[1:-1])
    else:
        return False


def twentyqs(start=1, end=100, q_count=0):
    if start > end:
        return "i admit defeat"
    elif q_count == 20:
        return "i admint defeat"
    else:
        mid = (start + end) // 2
        q_count += 1
        user_input = input(f"is {mid} ur value? (ye/nay)")
        if user_input == "ye":
            return f"ez dub with only {q_count} questions asked"
        else:
            q_count += 1
            input2 = input(f"is ur number lower than {mid}?: (yes or no) ")
            if input2 == "yes":
                return twentyqs(start=1, end=mid, q_count=q_count)
            else:
                return twentyqs(start=mid, end=100, q_count=q_count)

print(twentyqs())
