# Write a function to convert numbers to text numerals
NUM_WORD = {1: "one",
           2: "two",
           3: "three",
           4: "four",
           5: "five",
           6: "six",
           7: "seven",
           8: "eight",
           9: "nine",
           10: "ten",
           11: "eleven",
           12: "twelve",
           13: "thirteen",
           14: "fourteen",
           15: "fifteen",
           16: "sixteen",
           17: "seventeen",
           18: "eighteen",
           19: "nineteen",
           20: "twenty",
           30: "thirty",
           40: "forty",
           50: "fifty",
           60: "sixty",
           70: "seventy",
           80: "eighty",
           90: "ninety"}
def text_numeral(num):
    """
    This function takes in an integer, and converts it into the English version of the integer

    Parameter
    ----------
    num:
        An integer

    Returns
    -------
    str:
        A string that is the English version of the parameter "num"

    Examples
    --------
    >>> text_numeral(15)
    'fifteen'
    >>> text_numeral(29)
    'twenty nine'
    
    """
    ans = []
    key_list = [key for key in NUM_WORD]
    for keys in key_list[::-1]:
        if keys <= num:
            ans.append(NUM_WORD[keys])
            num -= keys
    return " ".join(ans)


