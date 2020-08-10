import os
from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import VideoFileClip
from PIL import Image


source_path = os.path.join(SAMPLE_INPUTS, 'sample.mp4')
thumbnail_dir = os.path.join(SAMPLE_OUTPUTS, "thumbnails")
thumbnail_per_frame_dir = os.path.join(SAMPLE_OUTPUTS, "thumbnails_per_frame")
thumbnail_per_half_second_dir = os.path.join(SAMPLE_OUTPUTS, "thumbnails_per_per_half_second")
os.makedirs(thumbnail_per_frame_dir, exist_ok=True)
os.makedirs(thumbnail_dir, exist_ok=True)
os.makedirs(thumbnail_per_half_second_dir, exist_ok=True)

clip = VideoFileClip(source_path)
print(clip.reader.fps) #frames per seconds
print(clip.reader.nframes)
print(clip.duration)
duration = clip.duration
max_duration = int(duration) + 1
for i in range(0, max_duration):
    frame = clip.get_frame(int(i))
    new_img_filepath = os.path.join(thumbnail_dir, f"{i}.jpg")
    #print(f"frame at {i} seconds saved at {new_img_filepath}")
    #print(frame)
    new_image = Image.fromarray(frame)
    new_image.save(new_img_filepath)

fps = clip.reader.fps
nframes = clip.reader.nframes
seconds = nframes / (fps * 1.0)


for i, frame in enumerate(clip.iter_frames()): #i = frame_index
    if i % fps == 0:
        current_milli_seconds = int((i / fps) * 1000)
        new_img_filepath = os.path.join(thumbnail_per_frame_dir, f"{current_milli_seconds}.jpg")
        #print(f"frame at {i} seconds saved at {new_img_filepath}")
        #print(frame)
        new_image = Image.fromarray(frame)
        new_image.save(new_img_filepath)
        i += 1

for i, frame in enumerate(clip.iter_frames()): #i = frame_index
    fphs = int(fps/2.0) # fphs =frames_per_half_second
    if i % fphs == 0:
        current_milli_seconds = int((i / fps) * 1000)
        new_img_filepath = os.path.join(thumbnail_per_half_second_dir, f"{current_milli_seconds}.jpg")
        #print(f"frame at {i} seconds saved at {new_img_filepath}")
        #print(frame)
        new_image = Image.fromarray(frame)
        new_image.save(new_img_filepath)
        i += 1