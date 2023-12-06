import requests, json



payload = {
    "recipient_type": "individual",
    "to" : "27625693562",#Number here
    "type": "interactive",
"interactive":
    {
    "type": "product_list",
    "header":{
        "image": {
            "id": "your-media-id"              #We Will put business Logo here
        }
     },
     "body":{
        "text": "Heyy Welcome Please take a Look at Our catalogue"
      },
     # "footer":{                   may not use this
     #    "text":"text-footer-content"
     # },
     "action":{
        "catalog_id":"catalog-id",
        "sections": [
             {
             "title": "the-section-title",
             "product_items": [
                  { "product_retailer_id": "product-SKU-in-catalog" },
                  { "product_retailer_id": "product-SKU-in-catalog" },

              ]}
              # {
              # "title": "the-section-title",
              # "product_items": [
              #    { "product_retailer_id": "product-SKU-in-catalog" }
              # ]},
       ]
     },
    }
}


payload = json.dumps(payload)
response = requests.post("https://waba.360dialog.io/v1/messages", data=payload,headers= {
    'D360-Api-Key': 'EPidTiaDt7bl0sy5rNEHv6mBAK',
    'Content-Type': "application/json",
})
print(response.text)


