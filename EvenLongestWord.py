# Take a string from user, Search in the string longest even number and return the number using function
# If no longest even word then return '00'

def longest_even(string):
    longest_word = '00'
    for word in string.split():
        if len(word) % 2 == 0 and len(word) > len(longest_word):
            longest_word = word
    return longest_word


if __name__ == '__main__':
    print("Enter a string: ", end="")
    input_string = input()

    print(f"Longest Even word from the inputted string '{input_string}' is '{longest_even(input_string)}'")