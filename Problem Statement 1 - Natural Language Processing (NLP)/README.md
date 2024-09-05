# Text Preprocessing and Tokenization with spaCy

This project demonstrates how to preprocess and tokenize text using **spaCy** within a **Streamlit** web app. It provides a user-friendly interface where you can input text, and the app will process it, filtering out stop words and non-alphabetic tokens.

## Features
- **Text Preprocessing**: The app converts the input text to lowercase and processes it using spaCy's language model.
- **Tokenization**: It tokenizes the input text and filters out stop words and non-alphabetic tokens.
- **Interactive UI**: A simple Streamlit web interface allows users to input text and view the results in real-time.

## Example
**If you input:**
Hi, Everyone! This is an example phrase.

**The output will be:**
[hi, example, phrase]

## Requirements

To run this project, you will need the following Python packages:
- **streamlit**: For building the web app.
- **spacy**: For natural language processing.
- **en_core_web_sm**: The spaCy English model.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/iampraveens/SNS-iHub-Assignment.git
    ```

2. Navigate to the project directory:
    ```bash
    cd your-repository
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Download the spaCy English language model:
    ```bash
    python -m spacy download en_core_web_sm
    ```

## Running the App

To run the Streamlit app, execute the following command:
```bash
streamlit run app.py
```

This will start the Streamlit server and open the app in your default web browser.

## Usage
1. Enter the text you want to preprocess and tokenize in the text input area.
2. Click the Process Text button to view the filtered tokens.

## File Structure
- **tokenizer.py:** Main script containing the Streamlit app and tokenization function.
- **requirements.txt:** Lists the dependencies required to run the app.
- **README.md:** Project documentation (this file).

## License
This project is licensed under the MIT License - see the LICENSE file for details.
