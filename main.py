from stats import get_num_words, get_character_count, sort_dictionary, alpha_only
import sys

def main(): #use relative path to book
    if len(sys.argv) < 2 :
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    get_num_words(path)
    print("--------- Character Count -------")
    count = get_character_count(path)
    sorted_num = sort_dictionary(count)
    alpha_only(sorted_num)

    print("============= END ===============")

    

main()