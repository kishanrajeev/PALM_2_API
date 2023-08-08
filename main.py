import k2key
import google.generativeai as palm

palm.configure(api_key=k2key.API_KEY)

# Create a new conversation
response = palm.chat(messages='Hello')

# Last contains the model's response:
response.last

print(response.last)