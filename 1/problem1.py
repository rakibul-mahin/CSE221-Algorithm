'''
PROBLEM: 1
FILE I/O
'''

even_parity_count, odd_parity_count, float_parity_count, palindrome_count, not_palindrome_count = 0, 0, 0, 0, 0
line_count = 0


# This function will check whether the number is odd, even or float
def even_odd_checker(num):
    if '.' in num:
        result_type = "float"
        return "{} cannot have parity and ".format(float(num)), result_type
    if int(num) % 2 == 0:
        result_type = "even"
        return "{} has even parity and ".format(int(num)), result_type
    else:
        result_type = "odd"
        return "{} has odd parity and ".format(int(num)), result_type


# This will check whether the string or word is palindrome or not
def palindrome_checker(word):
    not_palindrome = True
    if word is None:
        return "{} is not a palindrome".format(word), not_palindrome

    n = len(word)

    for i in range(0, n // 2):
        if word[i] != word[n - 1 - i]:
            return "{} is not a palindrome".format(word), not_palindrome

    not_palindrome = False
    return "{} is a palindrome".format(word), not_palindrome


# This is the main part, it will read, append and write data in different text files
with open('input.txt', 'r') as input_file:
    with open('output.txt', 'w') as output_file:

        for each_line in input_file:
            line_count += 1
            pair_list = each_line.split(" ")

            output_result, r_type = even_odd_checker(pair_list[0])
            if r_type == "float":
                float_parity_count += 1
            elif r_type == "even":
                even_parity_count += 1
            else:
                odd_parity_count += 1

            palindrome_test, not_palindrome = palindrome_checker(pair_list[1].replace("\n", ""))
            if not_palindrome:
                not_palindrome_count += 1
            else:
                palindrome_count += 1

            output_file.writelines(output_result + palindrome_test + "\n")

    with open("record.txt", "w") as record_file:
        record_file.write("Percentage of odd parity: " + str(((odd_parity_count / line_count) * 100)) + "%\n")
        record_file.write("Percentage of even parity: " + str(((even_parity_count / line_count) * 100)) + "%\n")
        record_file.write("Percentage of no parity: " + str(((float_parity_count / line_count) * 100)) + "%\n")
        record_file.write("Percentage of palindrome: " + str(((palindrome_count / line_count) * 100)) + "%\n")
        record_file.write("Percentage of non-palindrome: " + str(((not_palindrome_count / line_count) * 100)) + "%\n")