import streamlit as st
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Define the text generation function
def generate_text(prompt, model_name='gpt2', max_length=150):
    """
    Generate text using a pre-trained GPT-2 model.

    Args:
        prompt (str): The input prompt to generate text from.
        model_name (str, optional): The name of the pre-trained GPT-2 model to use. Defaults to 'gpt2'.
        max_length (int, optional): The maximum length of the generated text. Defaults to 150.

    Returns:
        str: The generated text.
    """
    # Load the tokenizer for the given model
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    
    # Load the pre-trained GPT-2 model, using eos_token_id as the pad token
    model = GPT2LMHeadModel.from_pretrained(model_name, pad_token_id=tokenizer.eos_token_id)

    # Encode the input prompt into token IDs
    numeric_ids = tokenizer.encode(prompt, return_tensors='pt')

    # Generate text using beam search with no repeating n-grams
    result = model.generate(
        numeric_ids,
        max_length=max_length,  # Limit the length of the generated text
        num_beams=5,            # Use beam search for better results
        no_repeat_ngram_size=2,  # Prevent repetition of n-grams
        early_stopping=True      # Stop early if all beams reach the EOS token
    )
    
    # Decode the generated token IDs back into text
    generated_text = tokenizer.decode(result[0], skip_special_tokens=True)
    
    return generated_text  # Return the generated text

# Streamlit app setup
st.title("Text Generation")

# User input
user_input = st.chat_input(placeholder="Enter any text to generate")

# Generate response when the user submits a message
if user_input:
        response = generate_text(prompt=user_input)
        st.write(response)