from pytube import YouTube

link = input("Link: ")
yt = YouTube(link)

descarga = yt.streams.filter(only_audio=True).get_audio_only()
print("wait for it...")

descarga.download()
print("oke")
