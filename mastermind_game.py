from random import randint

#generate random 4 digit code
def gen_code():
    rand_list = ["R", "B", "G", "Y", "O", "P"]
    return rand_list[randint(0,5)]

def red_check(red_num, j, win_con, rand_code_copy, user_input):
    if user_input[j] == rand_code_copy[j]:
        red_num += 1
        rand_code_copy[j] = "0"
        user_input[j] = "1"
    if red_num == 4:
        win_con = True
    return red_num, win_con, user_input, rand_code_copy

def white_check(white_num, j, rand_code_copy, user_input):
    if rand_code_copy.count(user_input[j]) >= 1:
        white_num += 1
        tmp_index = rand_code_copy.index(user_input[j])
        rand_code_copy[tmp_index] = "0"
    return white_num

def print_score(num_red, num_white):
        print("Number of Red Pins: " + str(num_red))
        print("Number of White Pins: " + str(num_white))
        num_red = 0
        num_white = 0
        return num_red, num_white

def make_user_code():
    j = 0
    for j in range(len(user_input)):
        user_input[j] = input("Guess Pin " + str(j + 1) + " (R, B, G, Y, O, P): ")
    return user_input
    

def check_guesses(num_red, num_white, win_con, user_input, rand_code_copy, j, h):
    for j in range(len(user_input)):
        num_red, win_con, user_input, rand_code_copy = red_check(num_red, j, win_con, rand_code_copy, user_input)
        j += 1
    for h in range(len(user_input)):    
        num_white = white_check(num_white, h, rand_code_copy, user_input)
        h += 1
    return num_red, num_white, win_con, user_input

def play_game(rand_code, user_input, i, win_con, num_red, num_white, num_guess):
    while i < num_guess and not win_con:
        #user input
        user_input = make_user_code()
        #check if user input matches random code
        j = 0
        h = 0
        rand_code_copy = rand_code.copy()
        #guessing game
        num_red, num_white, win_con, user_input = check_guesses(num_red, num_white, win_con, user_input, rand_code_copy, j, h)
        #prints number of red and white pins
        num_red, num_white = print_score(num_red, num_white)
        i += 1
    quit = True
    return quit, win_con


#variable declaration
quit = False
rand_code = ["0", "0", "0", "0"]
user_input = ["0", "0", "0", "0"]
num_guess = 8
win_con = False
num_red = 0
num_white = 0
#game starts
while not quit:
    #call random code generation function
    for index in range(len(rand_code)):
        rand_code[index] = gen_code()   
    i = 0
    #begin user guesses
    quit, win_con = play_game(rand_code, user_input, i, win_con, num_red, num_white, num_guess)

if win_con:
    print("you win!")
else:
    print("you lose!")
