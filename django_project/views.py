import requests
from django.shortcuts import render

def home(request):
    try:
        # Example 1: Fetching repo name from GitHub API
        response1 = requests.get('https://api.github.com/events')
        response1.raise_for_status()  
        data1 = response1.json()
        result1 = data1[0]["repo"]

        # Example 2: Fetching a random dog image from Dog CEO API
        response2 = requests.get('https://dog.ceo/api/breeds/image/random')
        data2 = response2.json()
        result2 = data2["message"]  # Access the "message" key to get the dog image URL

        # Example 3: Fetching a random cat image from cat API
        response3 = requests.get('https://api.thecatapi.com/v1/images/search')
        data3 = response3.json()
        result3 = data3[0]["url"]  # Access the "url" key to get the cat image URL

    except requests.RequestException as e:
        # Handle request exceptions, like network errors or bad responses
        result1 = "Error fetching data: " + str(e)
        result2 = "Error fetching data: " + str(e)
        result3 = "Error fetching data: " + str(e)

    return render(request, 'templates/index.html', {'result1': result1, 'result2': result2, 'result3': result3})
