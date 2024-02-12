from mutagen.mp4 import MP4
import glob
import numpy as np

def get_audio_duration(filename):
    audio = MP4(filename)
    return audio.info.length

# duration = get_audio_duration('2024_02_11_15_13_16.mp4')
# print(int(duration//60),'min',int(duration%60),'seconde')

list_=glob.glob("*.mp4")
N=len(list_)
name=[]
time=[]
for i,f_name in enumerate(list_):
    try:
        duration = get_audio_duration(f_name)
        if duration > 2*60: # 2 minutes
            print('OK',i,'/',N,f_name, int(duration//60),'min',int(duration%60),'seconde')
            name.append(f_name)
            time.append(duration)
        else:
            print('NOK',f_name,"Audio is very short < 2min")
    except:
        print('NOK',f_name,'ERROR')
        pass

    
string= '''
function names() {
return ''' +str(name) + ''';
}

function times() {
return ''' +str(time) + ''';
}

function tot_times() {
return ''' +str(np.sum(time))+''';
}

'''


with open ('names.js','w') as f:
    f.write(string)
    f.close()
input('close?')
