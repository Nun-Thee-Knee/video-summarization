from youtube_transcript_api import YouTubeTranscriptApi


class Data:
    def __init__(self,link):
        self.link = link
        self.text = None
        self.transcript = None
        self.video_id = None
        self.message = []
        self.data = None

    def video_link_check(self):
        try:
            self.video_id = self.link.split("/")[3].split("?")[0].strip()
            self.transcript_fetcher()
        except Exception as e:
            error = type(e).__name__
            self.message.append({error: "You have provided a wrong youtube link"})
            return self.message


    def transcript_fetcher(self):
        try:
            self.transcript = YouTubeTranscriptApi.get_transcript(self.video_id)
        except Exception as e:
            error = type(e).__name__
            if error == "TranscriptsDisabled":
                self.message.append({error: "Subtitles for this link are disabled"})
            elif error == "NoTranscriptFound":
                self.message.append({error: "Language is not supported of this video"})
            else:
                self.message.append({error: "Error faced while fetching the transcript"})
        self.summarization()


    def summarization(self):
        if not self.message:
            self.text = " ".join([entry['text'] for entry in self.transcript])
            self.data = {
                "transcript": self.transcript,
                "summarized_text": self.text
            }
            return self.data
        else:
            self.message.append({"TranscriptUnavailable": "Summarization is Impossible for unavailable transcripts"})
            return self.message