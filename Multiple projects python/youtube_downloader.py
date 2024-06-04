from pytube import YouTube

link = "https://www.youtube.com/live/qvq_eLhgxDg?si=w_JSPvTw0Wp1QU44"

youtube_1 = YouTube(link)

# print(youtube_1.title)
# print(youtube_1.thumbnail_url)

videos = youtube_1.streams.all() # for all format

# videos = youtube_1.streams.filter(only_audio=True)
vid = list(enumerate(videos))

for i in vid:
    print(i)

strm = int(input("enter :"))    
videos[strm].download()    
print("Successfully downloaded")

# *********** Playlist download ****************

# from pytube import Playlist

# py = "https://www.youtube.com/playlist?list=PLKnIA16_RmvbAlyx4_rdtR66B7EHX5k3z"

# print(f"Downloading : {py.title}")

# for video in py.videos:
#     video.streams.first().download()