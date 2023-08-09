# PALM-A-API

This project is a Python script that utilizes the PaLM API from Google's Generative AI library to create a chatbot. The script enables the user to initiate a new conversation with the chatbot, reset the conversation, or exit the program. The chatbot employs the PaLM API to generate responses to the user's messages.

## Getting Started

To utilize this project, you will need to have an API key for the PaLM API. The API key should be stored in a Python file named `k2key.py` in the same directory as the script. The API key can be obtained from the Google Cloud Console.

## Prerequisites

- Python 3.x
- PaLM API key

## Installation

1. Clone the repository to your local machine.
2. Create a Python file named `k2key.py` in the same directory as the script.
3. Add your PaLM API key to the `k2key.py` file in the following format: `API_KEY = 'your_api_key_here'`.

## Usage

To run the script, simply execute the script in a Python environment. The script will prompt the user to enter a message to start the conversation. The `new_palm()` function prompts the user to enter a message to start the conversation. The function then uses the PaLM API to generate a response to the user's message. The function continues to prompt the user for responses and generate responses using the PaLM API until the user enters "n" to reset the conversation or "exit" to exit the program. The function limits the number of prompts to 90 per minute.

## Built With

- Python
- PaLM API from Google's Generative AI library

## Acknowledgments

- The Google Generative AI Python Client was used to interact with the PaLM API.

## Contact

* [Kishan Rajeev](https://kishan.jeevsol.com/)

## License

Licensed under the MIT License.
