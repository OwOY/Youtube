from pytube import YouTube
import ssl
import os
import sys
import ffmpeg 

ssl._create_default_https_context = ssl._create_unverified_context

class Youtube:

    def __init__(self, url):

        self.url = url
        self.main()


    def main(self):
        
        self.choose_res()
    

    def choose_res(self):

        yt = YouTube(self.url)
        stream_yt_list = yt.streams
        print(yt.title)
        res = int(input('請選擇您要的影片清晰度(預設mp4)\n(1)1080p\n(2)720p\n(3)360p\n(4)240p\n(5)離開 :  '))
        stream_yt_audio = stream_yt_list.filter(mime_type="audio/mp4")[0]

        if res == 1:
            stream_yt = stream_yt_list.filter(res="1080p", mime_type="video/mp4")[0]
            try:
                self.download_video_audio(stream_yt, stream_yt_audio)
            except Exception as err:
                print(err)

        elif res == 2:
            stream_yt = stream_yt_list.filter(res="720p", mime_type="video/mp4")[0]
            try:
                stream_yt.download()
                stream_yt_audio.download()
                print('OK')
            except Exception as err:
                print(err)

        elif res == 3:
            stream_yt = stream_yt_list.filter(res="360p", mime_type="video/mp4")[0]
            try:
                stream_yt.download()
                stream_yt_audio.download()
                print('OK')
            except Exception as err:
                print(err)

        elif res == 4:
            stream_yt = stream_yt_list.filter(res="240p", mime_type="video/mp4")[0]
            try:
                stream_yt.download()
                stream_yt_audio.download()
                print('OK')
            except Exception as err:
                print(err)

        elif res == 5:
            os._exit(0)


    def download_video_audio(self, stream_yt, stream_yt_audio):
        
        video = stream_yt.download()
        path = os.path.dirname(video)
        video_name = os.path.basename(video)
        os.rename(video, path + '/video.mp4')
        
        audio = stream_yt_audio.download()
        audio_type = os.path.basename(audio).split('.')[-1]
        audio_name = f'{path}/audio.{audio_type}'
        os.rename(audio, audio_name)

        self.merge_audio_video(path, video_name, audio_name)


    def merge_audio_video(self, path, video_name, audio_name):

        video_stream = ffmpeg.input(f'{path}/video.mp4') 
        audio_stream = ffmpeg.input(audio_name) 
        ffmpeg.output(audio_stream, video_stream, video_name).run() 
        os.remove(f'{path}/video.mp4')
        os.remove(audio_name)


if __name__ == '__main__':
    
    url = sys.argv[1]
    Youtube(url)