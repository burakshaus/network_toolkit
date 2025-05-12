import requests

def fetch_wikipedia_summary(query):
    try:
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{query}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data.get("extract", "No summary available")
        else:
            return f"Error: Could not find page for '{query}'."
    except Exception as e:
        return f"Exception occured: {e}"
