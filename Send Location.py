
import requests, json


payload = {
    "recipient_type": "individual",
    "to" : "27727969902",
    "type": "location",
    "location": {

        "longitude": 18.4240655,
        "latitude": -33.924870,
        "name": "Botlhale AI ",#Can write anything
        "address": "17 Darling Street,Cape Town"#Address of the business
    }

}




payload = json.dumps(payload)
response = requests.post("https://waba.360dialog.io/v1/messages", data=payload,headers= {
    'D360-Api-Key': 'EPidTiaDt7bl0sy5rNEHv6mBAK',
    'Content-Type': "application/json",
})
print(response.text)


