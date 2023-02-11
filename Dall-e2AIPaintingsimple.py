import requests

print("""
           .d88888b.             
         .8P"     "9bd888b.      
        .8P     .d8P"   `"988.   
     .8888   .d8P"    ,     98.  
   .8P" 88   8"    .d98b.    88  
  .8P   88   8 .d8P"   "98b. 88  
  88    88   8P"  `"8b.    "98.  
  88.   88   8       8"8b.    88 
   88    "98.8       8   88   "88
    `8b.    "98.,  .d8   88    88
    88 "98b.   .d8P" 8   88   d8"
    88    "98bP"    .8   88 .d8" 
    "8b     `    .d8P"   8888"   
     "88b.,   .d8P"     d8"      
       "9888P98b.     .d8"       
               "988888P"         
""")

# Your OpenAI API key
apikey = input("Please enter your OpenAI APIkey")
api_key = apikey

# The description of the image you want to generate
prompt1 = input("Please enter your requirements:")
prompt = prompt1
#Select size
sizep = input("Please select the size you need,The size of the generated images. Must be one of ,  or .[256x256][512x512][1024x1024]:")
# The endpoint URL for the DALL·E 2 API
url = "https://api.openai.com/v1/images/generations"

# The headers for the API request
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# The payload for the API request
data = {
    "model": "image-alpha-001",
    "prompt": prompt,
    "num_images":1,
    "size":sizep,
    "response_format":"url"
}

# Send the API request
response = requests.post(url, headers=headers, json=data)

# Check if the request was successful
if response.status_code == 200:
    # Get the URL of the generated image
    image_url = response.json()["data"][0]["url"]
    print(f"Image URL: {image_url}")
else:
    print("Request failed")
