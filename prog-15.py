def even_level_substring(input_string):
    even_level_string = input_string[::2]
    return even_level_string
input_string = "Sunrises in the east"
result = even_level_substring(input_string)
print("The substring with characters at even levels is:", result)
