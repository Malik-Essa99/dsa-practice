def most_common_word(input_string):
    input_string = input_string.replace('.','')
    words = input_string.split()
    word_count = {}

    for word in words:
        word = word.lower()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # Find the word with the highest count
    most_common = ""
    max = 0
    
    for word in word_count:
        if word_count[word] > max:
            max = word_count[word]
            most_common = word
            
    return most_common

# Example usage
input_string = "In a galaxy far far away"
# input_string = "Taco cat ate a taco"
# input_string = "No. Try not. Do or do not. There is no try."
result = most_common_word(input_string)
print(result)




