from pytube import YouTube
link = input("Вставьте ссылку на видео  ")
video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download()
