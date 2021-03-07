# Youtube_Crawl

- 安裝套件

```
python -m pip install pytube
python -m pip install ffmpeg-python
apt -y install ffmpeg
```

## How to use pytube

```
from pytube import Youtube
yt = Youtube(<Youtube_url>)
```
- 影片標題
```
youtube_title = yt.title
```
- 串流資訊
```
yt_streams = yt.streams
```
>> yt_streams = 
[<Stream: itag="18" mime_type="video/mp4" res="360p" fps="30fps" vcodec="avc1.42001E" acodec="mp4a.40.2" progressive="True" type="video">, <Stream: itag="137" mime_type="video/mp4" res="1080p" fps="30fps" vcodec="avc1.640028" progressive="False" type="video">, <Stream: itag="248" mime_type="video/webm" res="1080p" fps="30fps" vcodec="vp9" progressive="False" type="video">, <Stream: itag="136" mime_type="video/mp4" res="720p" fps="30fps" vcodec="avc1.4d401f" progressive="False" type="video">, <Stream: itag="247" mime_type="video/webm" res="720p" fps="30fps" vcodec="vp9" progressive="False" type="video">, <Stream: itag="135" mime_type="video/mp4" res="480p" fps="30fps" vcodec="avc1.4d401e" progressive="False" type="video">, <Stream: itag="244" mime_type="video/webm" res="480p" fps="30fps" vcodec="vp9" progressive="False" type="video">, <Stream: itag="134" mime_type="video/mp4" res="360p" fps="30fps" vcodec="avc1.4d401e" progressive="False" type="video">, <Stream: itag="243" mime_type="video/webm" res="360p" fps="30fps" vcodec="vp9" progressive="False" type="video">, <Stream: itag="133" mime_type="video/mp4" res="240p" fps="30fps" vcodec="avc1.4d4015" progressive="False" type="video">, <Stream: itag="242" mime_type="video/webm" res="240p" fps="30fps" vcodec="vp9" progressive="False" type="video">, <Stream: itag="160" mime_type="video/mp4" res="144p" fps="30fps" vcodec="avc1.4d400c" progressive="False" type="video">, <Stream: itag="278" mime_type="video/webm" res="144p" fps="30fps" vcodec="vp9" progressive="False" type="video">, <Stream: itag="140" mime_type="audio/mp4" abr="128kbps" acodec="mp4a.40.2" progressive="False" type="audio">, <Stream: itag="249" mime_type="audio/webm" abr="50kbps" acodec="opus" progressive="False" type="audio">, <Stream: itag="250" mime_type="audio/webm" abr="70kbps" acodec="opus" progressive="False" type="audio">, <Stream: itag="251" mime_type="audio/webm" abr="160kbps" acodec="opus" progressive="False" type="audio">]

- ex:720p mp4 video
```
yt_streams.filter(res="720p", mime_type="video/mp4")
```
- ex:audio
```
yt_streams.filter(mime_type="audio/mp4")
```
- download video
```
yt_streams.filter(res="720p", mime_type="video/mp4")[0].download()
```
#### Youtube play list

```
from pytube import Playlist
pl = Playlist(<Youtube_playlist_url>)
for video in pl.videos:
    video.streams.filter()[0].download()
```



## How to use ffmpeg

- 結合影片及音樂
```
audio_stream = ffmpeg.input(<audio_path>)
video_stream = ffmpeg.input(<video_path>)
video_name = <output_name>
ffmpeg.output(audio_stream, video_stream, video_name).run() 
```