def int_to_roman_numeral(num):
    """
    Converts a positive integer into a roman numeral as a list.
    M (1000) is the largest roman numeral it will output.
    """
    result = ""
    
    #dict of values and their associated numeral, in descending order
    roman_numerals = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C',
    90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

    #for each key in roman_numerals, append corresponding value to result as many times as the key fits in num, update num
    for element in roman_numerals: 
        for i in range(num // element): 
            result += roman_numerals[element]
        num %= element

    return(result)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(prog="Int_to_roman_numeral", 
description= "Converts a positive integer into a roman numeral, M (1000) is the largest roman numeral it will output.",
epilog="Created by yours truly, Dominic")
    parser.add_argument("number", type=int)
    args = parser.parse_args()

    print(int_to_roman_numeral(args.number))

# option for use without parser would be:
# from int_to_roman_numeral import int_to_roman_numeral
# print("".join(int_to_roman_numeral(int(input("Number: ")))))

# meaty bit of the code w/out comments:
# result = ""
# roman_numerals = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C',
#     90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
# for element in roman_numerals.keys():
#     for i in range(num // element):
#         result += roman_numerals[element]
#     num %= element
# return(result)
