import time
import random

def generate_random_text():
    # List of sample texts for typing practice
    sample_texts = [
        "The quick brown fox jumps over the lazy dog.",
        "Python is a high-level programming language.",
        "Coding is fun and challenging.",
        "Practice makes perfect.",
        "Type as fast as you can!",
    ]
    return random.choice(sample_texts)

def calculate_typing_speed(start_time, end_time, typed_text):
    # Calculate typing speed in words per minute (WPM)
    words_typed = len(typed_text.split())
    elapsed_time_seconds = end_time - start_time
    wpm = (words_typed / elapsed_time_seconds) * 60
    return wpm

def main():
    input("Press Enter to start typing test...")
    
    random_text = generate_random_text()
    print("Type the following text:\n")
    print(random_text)
    
    input("\nPress Enter when ready to start typing...")
    
    start_time = time.time()
    typed_text = input("Start typing: ")
    end_time = time.time()
    
    wpm = calculate_typing_speed(start_time, end_time, typed_text)
    
    print("\nTyping Speed:", wpm, "WPM")
    
    # Calculate accuracy
    correct_words = sum(1 for a, b in zip(random_text.split(), typed_text.split()) if a == b)
    accuracy = (correct_words / len(random_text.split())) * 100
    print("Accuracy:", accuracy, "%")
    
if __name__ == "__main__":
    main()
