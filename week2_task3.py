def printNumber(n):
    if n > 99:
            return "ERROR"

    ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", 
                "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", 
                "sixty", "seventy", "eighty", "ninety"]

    if 0 <= n < 10:
            return ones[n]
    elif 10 <= n < 20:
            return teens[n - 10]
    else:
            t = n // 10
            o = n % 10
            return tens[t] + (" " + ones[o] if o > 0 else "")
print("Word form:", printNumber(58))  
print("Word form:", printNumber(102)) 