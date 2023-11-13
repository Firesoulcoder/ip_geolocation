import requests

# API endpoint URL
url = "https://api.apilayer.com/ip_to_location/"

# API key for authentication
api_key = "ENTER YOUR API KEY (GET IT FROM APILAYER)"

# Get user input for the IP address
ip_address = input("Enter the IP address: ")

# Construct the complete URL with the provided IP address
full_url = f"{url}{ip_address}"

# Set up headers with the API key
headers = {
    "apikey": api_key
}

# Make the API request
response = requests.get(full_url, headers=headers)

# Check the status code of the response
status_code = response.status_code

# If the request was successful (status code 200), display the result
if status_code == 200:
    result = response.json()

    # Display relevant details
    print("IP Address:", result.get("ip"))
    print("Latitude:", result.get("latitude"))
    print("Longitude:", result.get("longitude"))
    print("City:", result.get("city"))
    print("Region:", result.get("region"))
    print("Country:", result.get("country"))
else:
    print(f"Error: {status_code}. Unable to retrieve information.")
