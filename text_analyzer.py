# pythonic_analyzer.py
from collections import Counter

def read_file(file_path):
    """
    Reads a text file and returns its content as a single string.
    
    Args:
        file_path (str): The path to the text file.
        
    Returns:
        str: The content of the file.
    """
    with open(file_path, 'r') as f:
        return f.read()

def count_words(text):
    """
    Counts the frequency of each word in a given text.
    
    Args:
        text (str): The input text.
        
    Returns:
        collections.Counter: A Counter object with word frequencies.
    """
    words = text.lower().split()
    return Counter(words)

def find_long_words(word_list, min_length=3):
    """
    Finds all words in a list that are longer than a specified minimum length.
    
    Args:
        word_list (list): A list of words.
        min_length (int): The minimum length for a word to be considered "long".
        
    Returns:
        list: A list of words that meet the length criteria.
    """
    return [word for word in word_list if len(word) > min_length]

def analyze_text(file_path):
    """
    Analyzes a text file for word count, unique words, and frequent words.
    
    Args:
        file_path (str): The path to the text file to analyze.
    """
    file_content = read_file(file_path)
    words_list = file_content.lower().split()
    word_counts = count_words(file_content)
    
    print(f"The total number of words is: {len(words_list)}")
    print(f"The unique words count is: {len(word_counts)}")
    
    print("The most frequent words are:")
    for word, count in word_counts.most_common(5):
        print(f"'{word}': {count}")
    
    long_words = find_long_words(words_list)
    print(f"Long words (more than 3 characters): {len(long_words)}")
    
if __name__ == "__main__":
    # Create a text file for testing.
    with open("sample.txt", "w") as f:
        f.write("The fluffy cat naps on the windowsill, purring. The other cat stretches and yawns, ready for a playful chase with a toy mouse.")
    
    analyze_text("sample.txt")