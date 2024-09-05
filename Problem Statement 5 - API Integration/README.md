# Country Information Fetcher

This project is a **Streamlit** app that fetches and displays information about a country using the **REST Countries API**. Users can input the name of a country, and the app will retrieve relevant details such as the capital, population, area, region, languages, and currencies.

## Features
- **Country Information Retrieval**: Fetches and displays country data like name, capital, population, area, region, languages, and currencies.
- **Error Handling**: Handles cases where the country is not found or if there is a network or API error.
- **Streamlit Interface**: Provides an intuitive and user-friendly web interface for input and data display.

## Example

**If you enter:**
Canada

**The output will display:**
- Name: Canada
- Capital: Ottawa
- Population: 38,005,238
- Area: 9,984,670 sq. km
- Region: Americas
- Languages: English, French
- Currencies: Canadian dollar (C$)

## Requirements

To run this project, you will need the following Python packages:
- **streamlit**: For building the web app interface.
- **requests**: For making API calls to the REST Countries API.

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
streamlit run fetch_country_info.py
```
This will start the Streamlit server and open the app in your default web browser.

## Usage
1. Enter a country name in the input field.
2. Click on the Get Country Info button.
3. The app will fetch and display relevant information about the country.

## File Structure
- **fetch_country_info.py:** Main script containing the Streamlit app and country information fetching logic.
- **requirements.txt:** Lists the dependencies required to run the app.
- **README.md:** Project documentation (this file).

## License
This project is licensed under the MIT License - see the LICENSE file for details.