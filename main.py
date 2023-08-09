#importing other python files
import k2key #Contails API key

#Importing libraries
import google.generativeai as palm

def new_palm():

    Og_response = input("Start a new conversation: ")
    if Og_response == 'n':
       new_palm()
    else:
        palm.configure(api_key=k2key.API_KEY)

        response = palm.chat(messages=(Og_response), temperature = 1)
        response.last
        print(response.last)

        response = response.reply(input('Respond to Palm: '))
        response.last
        print(response.last)


if __name__ == '__main__':
    while True:
        new_palm()