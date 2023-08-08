#importing other python files
import k2key #Contails API key

#Importing libraries
import google.generativeai as palm

palm.configure(api_key=k2key.API_KEY)

# Create a new conversation
response = input("Star a new conversation: ")

# Last contains the model's response:
response.last

print(response.last)


# Add to the existing conversation by sending a reply
response = response.reply(input("Respond to Palm: "))
# See the model's latest response in the `last` field:
response.last
print(response.last)
