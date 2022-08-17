import csv
import os
from pathlib import Path
from pytube import YouTube

current_dir = Path(__file__).resolve().parents[0]

f = open(str(current_dir /"fs-videos.csv"))
rdr = csv.reader(f)
next(rdr)

yt_address = "https://www.youtube.com/watch?v="
yt_id = ""

for line in rdr:
  
    name = line[0]
    resolution = line[1][5:]
    fps = int(line[2][:2])
    yt_id = line[3]

    url = yt_address + yt_id
    yt = YouTube(url)
    yt.streams.filter(fps=int(fps),
                      res=resolution+"p",
                      file_extension='mkv').first().download(output_path=str(current_dir / "data" / "sports" / "fs" / "videos"),
                                                             filename=name+".mkv")
f.close()

    
