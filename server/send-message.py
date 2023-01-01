# Import the required libraries
import requests

# Set the API endpoint and your API key
api_endpoint = '/server/v1/message'
api_key = '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'

# Send a POST request to the API
def send_message(message):
  data = { 'message': message }
  headers = { 'Content-Type': 'application/json', 'X-API-Key': api_key }
  response = requests.post(api_endpoint, json=data, headers=headers)

  # Return the chatbot's message
  return response.json()['message']
