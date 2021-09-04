from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api import _errors

try:
    videoUrl = input("Please enter the video url: \n")
    videoId = videoUrl[videoUrl.index("v=") + 2 : ]
    srt = YouTubeTranscriptApi.get_transcript(f"{videoId}")
    word = input("Please enter the word you are looking for: \n")
    print("Link(s): ")
    for index in range(len(srt)):
        if word in srt[index]["text"]:
            print(f"https://www.youtube.com/watch?v=zxYjTTXc-J8&t={srt[index]['start']}s")
    
except _errors.TranscriptsDisabled :  
    print("This video has no subtitles")

