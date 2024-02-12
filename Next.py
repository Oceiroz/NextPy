
def menu():
    user_number = get_input("Please input any whole number", int)
    format_number(user_number)
    
def get_input(input_message, input_type):
    while(True):
        raw_input = input(f"{input_message}\n")
        
        try:
            user_input = input_type(raw_input)
            break
        except ValueError:
            print("invalid input, please try again")
    
    return user_input

def format_number(user_number):
    
    user_list = []
    for char in str(user_number):
        user_list.append(int(char))    
    user_list.sort(reverse=True)
    final_value = ""
    for char in user_list:
        final_value += str(char)
    if int(final_value) == user_number:
        print(-1)
    else:
        print(final_value)
    
menu()