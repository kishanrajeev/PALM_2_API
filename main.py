#importing other python files
import k2key #Contails API key

#Importing libraries
import google.generativeai as palm

palm.configure(api_key=k2key.API_KEY)

response = palm.chat(messages=(input('Start a new conversation: ')), temperature = 1)
response.last
print(response.last)

response = response.reply(input("Respond to Palm: "))
response.last
print(response.last)