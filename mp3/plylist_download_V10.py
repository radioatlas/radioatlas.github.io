from pytube import Playlist
from datetime import datetime

URL_PLAYLIST = "https://www.youtube.com/watch?v=80PfZmAAxWY&list=PL7umzjS_ns5wMMPAyCXvzIvvr7NUaDq9T"




import youtube_dl
youtube_dl_options = {
        'skip_download': True,
        'ignoreerrors': True
    }
with youtube_dl.YoutubeDL(youtube_dl_options) as ydl:
    videos = ydl.extract_info(f'https://www.youtube.com/@levendeurdecassettes')

sdhsdhshd











with open('log.txt', 'w') as f:
    f.close()

# Retrieve URLs of videos from playlist
playlist = Playlist(URL_PLAYLIST)
print('Number Of Videos In playlist: %s' % len(playlist.video_urls))
print('Number Of Videos In playlist: %s' % len(playlist.video_urls), file=open('log.txt', 'a'))



# importing packages 
from pytube import YouTube 
import os 

for x in playlist:
    try:
        
        yt = YouTube( x)
        # extract only audio 
        video = yt.streams.filter(only_audio=True).first() 
          
 
        out_file = video.download()
        #out_file=out_file.split('\\')[-1]

        try:
            # save the file 
            base, ext = os.path.splitext(out_file) 
            new_file = datetime.today().strftime('%Y_%m_%d_%H_%M_%S') + '.mp4'
            os.rename(out_file, new_file) 
              
            # result of success 
            print(out_file + '<;>'+new_file+'<;>>>>'+ "OK ")
            print(out_file + '<;>'+new_file+'<;>>>>'+ "OK ", file=open('log.txt', 'a', encoding='utf-8'))
        except:
            print(x+ " >>> OK RENAME NOK")
            print(x+ " >>> OK RENAME NOK", file=open('log.txt', 'a', encoding='utf-8'))
        

    except Exception as e:
        print(e)
        print(x+ " >>> ERROOOOOOOOOR")
        print(x+ " >>> ERROOOOOOOOOR", file=open('log.txt', 'a', encoding='utf-8'))
        
