#!/usr/bin/env python3

#########
#
# Author: Michael E. OConnor
#
#   •	The Responses API is a more generic API for generating text completions based on prompts. 
#       It is typically used for simpler tasks, such as completing a text prompt or generating creative 
#       writing, summaries, translations, etc.
#   •	It’s mainly used for single-turn interactions.
#
#########

import os
from openai import OpenAI

def main():
    # Load the API key from an environment variable
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError('The OPENAI_API_KEY environment variable is not set')

    # Expects api_key to be previously set
    client = OpenAI()

    # The prompt to send to GPT-3
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

    response = client.responses.create(
        model="gpt-4o-mini",
        instructions="You are a helpful python coding assistant.",
        input=prompt,
    )

    print(response.output_text)

if __name__ == '__main__':
    main()
