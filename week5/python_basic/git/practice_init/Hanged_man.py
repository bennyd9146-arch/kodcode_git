import random
def choose_word(list_words):
    return random.choice(list_words).lower()

def print_game_status(number_of_attempts,hidden_word,selected_letters):
    print("========================================")
    print("         welcome to hanged man          ")
    print("========================================")
    print(f"the number_of_attempts is {number_of_attempts}, the selected_letters {selected_letters}, the hidden_word {hidden_word}")

def get_user_input():
    user_input = input("please enter your letter for the word: ")
    return user_input.lower()

def update_hidden_word(word,hidden_word,user):
    for i , char in enumerate(word) :
        if char == user:
            tmp = list(hidden_word)
            tmp[i] = user
            hidden_word = "".join(tmp)
    return hidden_word

def play_game():

    number_of_attempts = 20
    list_words =[
"Book",
"Tree",
"Blue",
"Good",
"Time",
"Love",
"Star",
"Home",
"Fire",
"Wind",]
    
    word = choose_word(list_words)
    hidden_word = "#" * len(word)
    selected_letters = []

    while number_of_attempts > 0 :
        print_game_status(number_of_attempts,hidden_word,selected_letters)

        user = get_user_input()
        selected_letters.append(user)
        
        if user in  word:
            hidden_word = update_hidden_word(word,hidden_word,user)

        
        if hidden_word == word:
            print("you won")
            break
            
        else:
            number_of_attempts -= 1
            if number_of_attempts == 0:
                print("The attempts are over")
    
play_game()






