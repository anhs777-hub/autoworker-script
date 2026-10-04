from pathlib import Path
import sys, subprocess, json
import numpy as np
from PIL import Image, ImageOps
sys.path.insert(0, str(Path('output/video-tools').resolve()))
import imageio_ffmpeg
out=Path('output/knowledge-university'); out.mkdir(parents=True,exist_ok=True)
banner=Image.open(r'C:/Users/user/Desktop/지식대학/ChatGPT 이미지 2026년 10월 4일 오전 01_55_42.png').convert('RGB')
logo=Image.open(r'C:/Users/user/Desktop/지식대학/지식대학 프로필 이미지.png').convert('RGBA')
ff=imageio_ffmpeg.get_ffmpeg_exe()
video=out/'knowledge-university-intro-720p.mp4'
cmd=[ff,'-y','-f','rawvideo','-vcodec','rawvideo','-pix_fmt','rgb24','-s','1280x720','-r','30','-i','-','-an','-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p','-movflags','+faststart',str(video)]
p=subprocess.Popen(cmd,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
thumbs=[]
def smooth(x):
    x=max(0,min(1,x)); return x*x*(3-2*x)
for i in range(180):
    t=i/30
    frame=Image.new('RGB',(1280,720),(255,252,235))
    size=round(530+20*smooth(t/2.5))
    lg=logo.resize((size,size),Image.Resampling.LANCZOS)
    frame.paste(lg,((1280-size)//2,(720-size)//2),lg)
    z=1+0.025*smooth((t-1.7)/4.3)
    bg=ImageOps.fit(banner,(round(1280*z),round(720*z)),method=Image.Resampling.LANCZOS)
    x=(bg.width-1280)//2; y=(bg.height-720)//2
    bg=bg.crop((x,y,x+1280,y+720))
    frame=Image.blend(frame,bg,smooth((t-1.7)/0.9))
    gain=smooth(t/0.8)*(1-smooth((t-5.1)/((179/30)-5.1)))
    arr=np.rint(np.asarray(frame,dtype=np.float32)*gain).astype(np.uint8)
    p.stdin.write(arr.tobytes())
    if i in [0,24,60,90,150,179]: thumbs.append(Image.fromarray(arr).resize((384,216)))
p.stdin.close(); err=p.stderr.read(); rc=p.wait()
if rc: raise RuntimeError(err.decode(errors='replace'))
sheet=Image.new('RGB',(1152,432))
for n,im in enumerate(thumbs): sheet.paste(im,((n%3)*384,(n//3)*216))
sheet.save(out/'intro-contact-sheet.jpg')
r=subprocess.run([ff,'-i',str(video),'-vf','signalstats,metadata=print:file='+str(out/'intro-frame-stats.txt').replace('\\','/'),'-f','null','-'],capture_output=True,text=True)
print(r.stderr[-1800:])
print(video.resolve())
