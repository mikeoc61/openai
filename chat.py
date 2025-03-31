#!/usr/bin/env python3

#########
#
# Author: Michael E. OConnor
#
#   •	The Chat Completions API is specifically designed for conversational AI, enabling more interactive, 
#       multi-turn conversations. It supports the exchange of messages, making it suitable for chatbots and 
#       other applications requiring back-and-forth dialogue.
#   •	This API allows you to track the history of the conversation and use it to generate more 
#       context-aware responses.
#   •	It retains the context of the entire conversation (or the conversation history you provide) and uses 
#       that to generate more coherent and context-aware responses. This makes it better suited for applications 
#       where context matters over multiple interactions.
#
#########

import os
from openai import OpenAI

# Load the API key from an environment variable
api_key = os.environ.get('OPENAI_API_KEY')
if not api_key:
    raise ValueError('The OPENAI_API_KEY environment variable is not set')

def main():

    # Expects api_key to be previously set
    client = OpenAI()

    # The prompt to send OpenAI
    prompt = input("Please enter a prompt: ")

    ### GPT-4o-Mini
    # - **Size**: Generally smaller in terms of model parameters.
    # - **Performance**: May be slower and less capable compared to larger models. Suitable for lightweight applications where performance is less critical.
    # - **Use Cases**: Often used for simpler tasks or in environments with limited computational resources.

    ### GPT-4o-Turbo
    # - **Size**: Larger and more powerful than Mini models.
    # - **Performance**: Faster response times and better at understanding and generating complex responses.
    # - **Use Cases**: Ideal for applications requiring higher accuracy, more nuanced understanding, and faster performance.

    ### Summary
    # - **Use GPT-4o-Mini** for lightweight tasks where resources are limited.
    # - **Use GPT-4o-Turbo** for applications that demand higher performance and better results.

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "developer", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )

    print(completion.choices[0].message.content)

if __name__ == '__main__':
    main()
