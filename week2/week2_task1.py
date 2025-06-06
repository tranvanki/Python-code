#1. Write python code to reverse the integer part and fractional part separately
#example, the input “123.456” must produce the output as “321.654”. 0.456 = 456/1000=> 0.456 *1000 % 10= 6
def reverse_number(number):
    # Separate integer and fractional parts
    integer_part = int(number)
    fractional_part = number - integer_part

    # Reverse integer part
    reverse_integer = 0
    temp = abs(integer_part)
    while temp > 0:
        reverse_integer = reverse_integer * 10 + temp % 10
        temp //= 10

    # Reverse fractional part (up to 4 digits)
    reverse_fractional = 0
    count = 0
    temp_frac = abs(fractional_part)
    while count < 4:
        temp_frac *= 10
        digit = int(temp_frac)
        reverse_fractional = reverse_fractional * 10 + digit
        temp_frac -= digit
        count +=1
        

    # Combine as string to keep the decimal
    fractional_str = str(reverse_fractional)    
    while len(fractional_str) < 4:
        fractional_str += '0'
    sign = ''
    if number < 0:
        sign = '-'
    result = sign + str(reverse_integer) + '.' + fractional_str
    return result
#test the function
print(reverse_number(123.456)) #expected output: 321.654
print(reverse_number(-123.456)) #expected output: -321.654

