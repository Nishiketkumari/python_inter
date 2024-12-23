import openai

# Set your OpenAI API key
#openai.api_key = "d59bf463e83c486d9511dec64343f207.ff0db0124bef016b"



openai.api_key = "78c6d3a593mshd48603e96868485p1db938jsn1a80a5e12873"

def chat_with_gpt(prompt, model="gpt-3.5-turbo", temperature=0.7, max_tokens=150):
    """
    Interacts with ChatGPT using the provided prompt.

    Parameters:
        prompt (str): The input prompt for ChatGPT.
        model (str): The model to use (default is "gpt-3.5-turbo").
        temperature (float): The creativity level (0.0-1.0).
        max_tokens (int): The maximum number of tokens to generate.

    Returns:
        str: The response from ChatGPT.
    """
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "system", "content": "You are a helpful assistant."},
                      {"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage
if __name__ == "__main__":
    user_input = input("Enter your prompt: ")
    response = chat_with_gpt(user_input)
    print("\nChatGPT response:")
    print(response)
