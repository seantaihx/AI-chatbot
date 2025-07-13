from grammar_correction import correct_grammar
from translator import translate
from quiz_generator import generate_quiz

def main():
    print("Welcome to AI Language Teacher!")
    while True:
        print("\nOptions:\n1. Grammar Correction\n2. Translate\n3. Quiz\n4. Exit")
        choice = input("Choose (1-4): ")

        if choice == "1":
            text = input("Enter the sentence: ")
            lang = input("Language (Spanish/German): ").strip().capitalize()
            print("Corrected:", correct_grammar(text, lang))
        elif choice == "2":
            text = input("Text to translate: ")
            src = input("From (e.g., es, de, en): ").lower()
            tgt = input("To (e.g., en, es, de): ").lower()
            print("Translation:", translate(text, src, tgt))
        elif choice == "3":
            lang = input("Quiz language (Spanish/German): ").capitalize()
            level = input("Level (beginner/intermediate/advanced): ").lower()
            print(generate_quiz(lang, level))
        elif choice == "4":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()