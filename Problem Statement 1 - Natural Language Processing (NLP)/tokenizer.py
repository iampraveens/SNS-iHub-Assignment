import streamlit as st
import spacy

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

# Define the function to preprocess and tokenize text
def preprocess_and_tokenize(text):
    """
    Preprocesses and tokenizes the given text.
    Args:
        text (str): The input text to be preprocessed and tokenized.
    Returns:
        List[str]: A list of filtered tokens from the preprocessed text.
    Description:
        This function takes in a text string as input and preprocesses it by converting it to lowercase and processing it with spaCy. It then filters out stop words and non-alphabetic tokens from the processed text and stores them in a list called `filtered_tokens`. Finally, it returns the `filtered_tokens` list.
    Example:
        >>> preprocess_and_tokenize("Hi, Everyone! This is an example phrase.")
        [hi, example, phrase]
    """
    # Convert text to lowercase and process it with spaCy
    doc = nlp(text.lower())

    # List to store filtered tokens
    filtered_tokens = []

    # Filter out stop words and non-alphabetic tokens
    for word in doc:
        if word.is_alpha and not word.is_stop:
            filtered_tokens.append(word)  # Use word to append the string version of the token

    return filtered_tokens

# Streamlit UI
st.title("Text Preprocessing and Tokenization")

# Text area for input
text_input = st.text_area("Enter text here", "Hi, Everyone! This is an example phrase.")

# Process text when the button is clicked
if st.button("Process Text"):
    if text_input:
        # Call the tokenization function
        tokens = preprocess_and_tokenize(text_input)
        
        # Display the tokens
        st.write("Filtered Tokens:")
        st.write(tokens)
    else:
        st.write("Please enter some text to process.")
