import streamlit as st
from dotenv import load_dotenv

load_dotenv()
import os
import google.generativeai as genai

from youtube_transcript_api import YouTubeTranscriptApi

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt = """This is a youtube transcript summarizer, which will provide a brief summary of 250 words depending on the transcript shared  """


def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("/")[3].split("?")[0].strip()

        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)

        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]
        print(transcript)
        return transcript

    except Exception as e:
        raise e


def generate_gemini_content(transcript_text, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt + transcript_text)
    return response.text


st.title("YouTube Transcript to Summary Converter")
youtube_link = st.text_input("Enter YouTube Video Link:")

if youtube_link:
    video_id = youtube_link.split("=")[1]
    print(video_id)
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

if st.button("Get Detailed Notes"):
    transcript_text = extract_transcript_details(youtube_link)

    if transcript_text:
        summary = generate_gemini_content(transcript_text, prompt)
        st.markdown("## Summary is as given below:")
        st.write(summary)
