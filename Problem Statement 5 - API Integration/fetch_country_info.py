import requests
import streamlit as st

# Function to fetch country data from the REST Countries API
def fetch_country_info(country_name):
    base_url = f"https://restcountries.com/v3.1/name/{country_name}"
    
    try:
        # Make a GET request to the API
        response = requests.get(base_url)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()  # Parse JSON response

            # Extract the first result (in case of multiple matches)
            country = data[0]

            # Extract relevant information
            name = country.get('name', {}).get('common', 'N/A')
            capital = country.get('capital', ['N/A'])[0]
            population = country.get('population', 'N/A')
            area = country.get('area', 'N/A')
            region = country.get('region', 'N/A')
            languages = country.get('languages', {}).values()
            currency_info = country.get('currencies', {}).values()

            # Prepare a user-friendly currency string
            currencies = ', '.join([f"{currency['name']} ({currency['symbol']})" for currency in currency_info])

            # Create a dictionary of the extracted information
            country_data = {
                'Name': name,
                'Capital': capital,
                'Population': population,
                'Area': f"{area} sq. km",
                'Region': region,
                'Languages': ', '.join(languages) if languages else 'N/A',
                'Currencies': currencies if currencies else 'N/A'
            }

            return country_data
        else:
            # Handle different HTTP status codes
            if response.status_code == 404:
                return {"Error": "Country not found. Please check the country name."}
            else:
                return {"Error": f"API returned an error: {response.status_code}"}

    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        return {"Error": f"Unable to make the API request. {str(e)}"}

# Streamlit app setup
st.title("Country Information Fetcher")

# Input field to get the country name from the user
country_name = st.text_input("Enter the country name:")

# Fetch and display country data when the user submits the input
if st.button("Get Country Info"):
    if country_name:
        with st.spinner('Fetching data...'):
            country_info = fetch_country_info(country_name)
        
        # Check if an error was returned
        if "Error" in country_info:
            st.error(country_info["Error"])
        else:
            # Display the country information in a readable format
            st.subheader(f"Information about {country_info['Name']}")
            st.write(f"**Capital**: {country_info['Capital']}")
            st.write(f"**Population**: {country_info['Population']}")
            st.write(f"**Area**: {country_info['Area']}")
            st.write(f"**Region**: {country_info['Region']}")
            st.write(f"**Languages**: {country_info['Languages']}")
            st.write(f"**Currencies**: {country_info['Currencies']}")
    else:
        st.error("Please enter a country name.")
