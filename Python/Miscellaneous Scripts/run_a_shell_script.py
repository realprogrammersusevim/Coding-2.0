from asyncio import wait_for
from multiprocessing.connection import wait
import os
from time import sleep

youtube_video_url = input("Please provide a youtu.be link (from the 'Share' button). ")

if youtube_video_url.startswith("https://youtu.be"):
    os.system("yt-dlp " + youtube_video_url)
    print("Great! This Python script ran the shell script using yt-dlp to download your video. Your YouTube video has finished downloading now.")
    print("If you didn't change the location of the Terminal, the default location it boots up in is the folder /User/jonathanmilligan/")
else:
    print("Why don't you read the directions again.")
    print("Please provide a youtu.be link (from the 'Share' button)")
    sleep(3)
    print("Alright, got that?")
    youtube_video_url = input("Now try putting in the correct link this time. ")