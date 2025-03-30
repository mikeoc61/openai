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

    response = client.responses.create(
        model="gpt-4o",
        instructions="You are a helpful python coding assistant.",
        input=prompt,
    )

    print(response.output_text)

if __name__ == '__main__':
    main()
