#importing other python files
import k2key #Contails API key

#Importing libraries
import google.generativeai as palm
import os

os.environ['TERM'] = 'xterm-256color'

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def new_palm():
    print("Enter 'n' to reset the conversation. Limit 90 prompts per minute.")
    Og_response = input("Start a new conversation: ")
    if Og_response == 'n':
        clear_console()
        new_palm()
    else:
        palm.configure(api_key=k2key.API_KEY)

        response = palm.chat(messages=(Og_response), temperature = 1)
        print(response.last)
        while True:
            Og2_response = input('Respond to Palm: ')
            if Og2_response == 'n':
                clear_console()
                new_palm()
            else:
                response = response.reply(Og2_response)
                print(response.last)


if __name__ == '__main__':
    while True:
        new_palm()