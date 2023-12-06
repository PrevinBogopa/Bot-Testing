import requests, json


payload = {
    "recipient_type": "individual",
    "to" : "27727969902",
    "type": "interactive",
    "interactive": {
            "type": "location_request_message",
            "body": {
                "type": "text",
                "text": "Kindly Share Your Location"
            },
            "action": {
                "name": "send_location"
            }
        }
        }





payload = json.dumps(payload)
response = requests.post("https://waba.360dialog.io/v1/messages", data=payload,headers= {
    'D360-Api-Key': 'EPidTiaDt7bl0sy5rNEHv6mBAK',
    'Content-Type': "application/json",
})
print(response.text)


