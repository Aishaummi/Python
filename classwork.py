# def main():
#     sentence = ("This is a ball", "The ball is on the table", "This is my name")

# longest = 0

# for words in sentence.split():
#     if len(words)>longest:
#         longest = len(words)
#         longest = word = words
        
# # print("The longest word is", longest_word, "with lenght", len(longest_word))
# main()


sentences = ['This is a ball', 'The ball is on the table', 'This is my name']
def find_sentences_with_words(lst):
    longest = ''
    for word in lst:
        if len(word.split(' ')) > len(longest.split(' ')):
            
         longest = word
    return longest


random_stuffs = ['Hello', '23', '2.4', 'Night', 'welcome']

def get_on_string_with_characters(lst):
    return [value for value in lst if value.isalpha()]


print(get_on_string_with_characters(random_stuffs)) 