
import requests

# Replace with your deployed URL or "http://127.0.0.1:5000/generate" if local
url = "http://127.0.0.1:5000/generate"

payload = {
    "prompt": "Generate a persuasive letter for protesting my property tax increase in Travis County, Texas. My home was valued at $435,000 this year, up from $360,000 last year, but similar homes on my street are selling for $390,000."
}

response = requests.post(url, json=payload)
print(response.json())
