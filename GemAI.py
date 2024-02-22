import requests

#Gemini AI API key (according to 22.02.2024)
API_KEY = "AIzaSyBS1VrouiC3h6hO1a167SNVUaJVcd_1ijU"

def summarize_video(video_url):
    url = "https://api.gemini.ai/v1/summarize/video"

    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    
    payload = {
        "video_url": video_url
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  
        summary = response.json()["summary"]

        return summary

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


    if summary:
        print("Video Summary:")
        print(summary)
