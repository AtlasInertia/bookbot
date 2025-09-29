def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def get_num_words(filepath):
    num_words = len(get_book_text(filepath).split())
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

def get_character_count(filepath):
    count = {}                                  #empty dictionary to begin
    text = get_book_text(filepath).lower()      #convert all text to lowercase
    for char in text:                           #count all characters including spaces and symbols return as dictionary
        count[char] = count.get(char, 0) + 1    #default value of zero is set. For each occurance, 1 is added
    return count

def sort_dictionary(dictionary):
    new_list = []
    for char in dictionary:                 #convert key value pairs into list items (such as {"char": <e>, "num": <125>})
        simple_dictionary = {"char": 0 , "num": 0} #new dictionary for each set of pairs
        num = dictionary[char]              #fetch num value
        simple_dictionary["char"] = char    #modify dictionary value with iterator
        simple_dictionary["num"] = num      #modify dictionary value with iterator value pair
        new_list.append(simple_dictionary)  #add dictionary to list
    
    def sort_on(list_item):
        return list_item["num"]
    new_list.sort(reverse=True, key=sort_on)
    return new_list

def alpha_only(list):
    for item in list:
        if item["char"].isalpha() == True :
            print(f"{item["char"]}: {item["num"]}")
