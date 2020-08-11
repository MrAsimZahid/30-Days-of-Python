import os
from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import VideoFileClip
from moviepy.editor import ImageSequenceClip
from moviepy.editor import ImageClip
from PIL import Image

thumbnail_dir = os.path.join(SAMPLE_OUTPUTS, "thumbnails")
thumbnail_per_frame_dir = os.path.join(SAMPLE_OUTPUTS, "thumbnails_per_frame")
thumbnail_per_half_second_dir = os.path.join(SAMPLE_OUTPUTS, "thumbnails_per_per_half_second")
output_videos = os.path.join(SAMPLE_OUTPUTS, 'thumbs.mp4')

this_dir = os.listdir(thumbnail_dir)
filepaths = [os.path.join(thumbnail_dir, fname) for fname in this_dir if fname.endswith("jpg")]

directory = {}

for root, dirs, files in os.walk(thumbnail_per_frame_dir):
    for fname in files:
        filepath = os.path.join(root, fname)
        try:
            key = float(fname.replace(".jpg", ""))
        except:
            key = None
        if key != None:
            directory[key] = filepath

new_paths = []
for k in sorted(directory.keys()):
    print(k)
    filepath = directory[k]
    new_paths.append(filepath)

#clip = ImageSequenceClip(new_paths, fps=10)
#clip.write_videofile(output_videos)

my_clips = []
for path in list(new_paths):
    frame = ImageClip(path)
    print(frame.img)
    my_clips.append(frame.img)
    print(dir(frame))

clip = ImageSequenceClip(my_clips, fps=22)
clip.write_videofile(output_videos)
