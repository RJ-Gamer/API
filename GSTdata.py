import requests

url = "https://gst-number-verify-or-search.p.rapidapi.comhttps//appyflow.in/api/verify-gst"

# payload = "gstIN=03ACDPM7062M1ZH&key_secret=OCM7ztf3i3QpJpBLljGseaWmaNV2"
headers = {
    'x-rapidapi-host': "gst-number-verify-or-search.p.rapidapi.com",
    'x-rapidapi-key': "31d3ea4a13msh754a97fffbcaae8p145ecejsnfbc6ac684819",
    'content-type': "application/json"
    }

response = requests.request("POST", url, headers=headers)

print(response.text)
