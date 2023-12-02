def replace_multiple_question_marks_and_exclamations(input_str):
    input_str = input_str.rstrip()
    last_non_whitespace_index = len(input_str) - 1
    while last_non_whitespace_index >= 0 and input_str[last_non_whitespace_index].isspace():
        last_non_whitespace_index -= 1
    if last_non_whitespace_index >= 0:
        last_char = input_str[last_non_whitespace_index]
        if last_char == '?' or last_char == '!':
            count = 1
            for i in range(last_non_whitespace_index - 1, -1, -1):
                if input_str[i] == last_char:
                    count += 1
                else:
                    break
            input_str = input_str[:last_non_whitespace_index - count + 1] + last_char
    return input_str
input_string = "Это вопрос???"
output_string = replace_multiple_question_marks_and_exclamations(input_string)
print(output_string)