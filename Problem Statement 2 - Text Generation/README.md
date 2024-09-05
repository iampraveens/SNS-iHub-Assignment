# Text Generation with Tranformers and GPT-2

This project demonstrates text generation using a **pre-trained GPT-2 model** from the Hugging Face `transformers` library, combined with a **Streamlit** interface for a simple and interactive experience. The app allows users to input a text prompt and generates a continuation using GPT-2.

## Features
- **Text Generation**: Generate text based on user-provided prompts using GPT-2.
- **Beam Search**: Enhances text generation quality with beam search, preventing repetitive outputs.
- **Streamlit Interface**: A user-friendly chat interface allows for easy interaction with the model.

## Example

- **If you input:**
Once upon a time,

- **The GPT-2 model will generate a continuation based on this prompt, such as:**
Once upon a time, there was a small village nestled in the mountains. The villagers lived in peace, tending to their farms and caring for their families. One day, however, a strange traveler arrived at the village gates, bringing with him tales of distant lands and ancient magic.

## Requirements

To run this project, you will need the following Python packages:
- **streamlit**: For building the web app interface.
- **transformers**: For loading and interacting with the GPT-2 model.

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

## Running the App

To run the Streamlit app, execute the following command:
```bash
streamlit run text_generation.py
```

This will start the Streamlit server and open the app in your default web browser.

## Usage
1. Enter a text prompt in the chat input.
2. The GPT-2 model will generate a continuation of the prompt.
3. The generated text will be displayed in the app.

## Customization
- You can modify the max_length parameter in the generate_text function to change the length of the generated text.
- You can change the num_beams parameter to adjust the beam search settings for text generation.

## File Structure
- **text_generation.py:** Main script containing the Streamlit app and GPT-2 text generation logic.
- **requirements.txt:** Lists the dependencies required to run the app.
- **README.md:** Project documentation (this file).

## License
This project is licensed under the MIT License - see the LICENSE file for details..