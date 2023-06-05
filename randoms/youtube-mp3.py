from pytube import YouTube

link = input("Link: ")
yt = YouTube(link)

print("wait for it...")

descarga = yt.streams.filter(only_audio=True).get_audio_only()
print("aguanta..")

descarga.download()
print("ya ta")
