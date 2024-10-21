from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip
from termcolor import colored
from moviepy.video.fx.all import crop
from moviepy.config import change_settings
import sys
import os
import srt_equalizer

# Adiciona o diretório dois níveis acima ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))

from utils import *
from config import *

change_settings({"IMAGEMAGICK_BINARY": 'C:\\Program Files\\ImageMagick-7.1.1-Q16-HDRI\\magick.exe'})

def get_verbose():
    return True

class Test:
    def __init__(self):
        files = os.listdir(os.path.join(ROOT_DIR, "video-gen", "assets"))
        images = []

        for file in files:
            if file.endswith(".png"):
                images.append(file)

        self.images = images

        combined_image_path = os.path.join(ROOT_DIR, "video-gen", "output", "test.mp4")
        threads = 2
        tts_clip = AudioFileClip(os.path.join(ROOT_DIR, "video-gen", "assets", "51da195f-5d9a-40d8-9a3a-6785e031a047.wav"))
        max_duration = tts_clip.duration
        req_dur = max_duration / len(self.images)

        # Make a generator that returns a TextClip when called with consecutive
        generator = lambda txt: TextClip(
            txt,
            font=os.path.join(ROOT_DIR, "video-gen", "assets", "Roboto-Bold.ttf"),
            fontsize=100,
            color="#FFFF00",
            stroke_color="black",
            stroke_width=20,
            size=(1080, 1920),
            method="caption",
        )

        print(colored("[+] Combining images...", "blue"))

        clips = []
        tot_dur = 0
        # Add downloaded clips over and over until the duration of the audio (max_duration) has been reached
        while tot_dur < max_duration:
            for image_path in self.images:
                clip = ImageClip(os.path.join(ROOT_DIR, "video-gen", "assets", image_path))
                clip.duration = req_dur
                clip = clip.set_fps(30)

                # Not all images are same size,
                # so we need to resize them
                if round((clip.w/clip.h), 4) < 0.5625:
                    if get_verbose():
                        info(f" => Resizing Image: {image_path} to 1080x1920")
                    clip = crop(clip, width=clip.w, height=round(clip.w/0.5625), \
                                x_center=clip.w / 2, \
                                y_center=clip.h / 2)
                else:
                    if get_verbose():
                        info(f" => Resizing Image: {image_path} to 1920x1080")
                    clip = crop(clip, width=round(0.5625*clip.h), height=clip.h, \
                                x_center=clip.w / 2, \
                                y_center=clip.h / 2)
                clip = clip.resize((1080, 1920))

                # FX (Fade In)
                clip = clip.fadein(2).fadeout(2)

                clips.append(clip)
                tot_dur += clip.duration

        final_clip = concatenate_videoclips(clips)
        final_clip = final_clip.set_fps(30)
        random_song = os.path.join(ROOT_DIR, "video-gen", "assets", "1.mp3")

        subtitles_path = os.path.join(ROOT_DIR, "video-gen", "assets", "a13977a0-b72b-4e60-a07d-06f2d3e4658e.srt")

        # Equalize srt file
        srt_equalizer.equalize_srt_file(subtitles_path, subtitles_path, 10)

        # Burn the subtitles into the video
        subtitles = SubtitlesClip(subtitles_path, generator)
        subtitles.set_position(("center", "center"))

        random_song_clip = AudioFileClip(random_song).set_fps(44100)

        # Turn down volume
        random_song_clip = random_song_clip.fx(afx.volumex, 0.35)
        comp_audio = CompositeAudioClip([
            tts_clip.set_fps(44100),
            random_song_clip
        ])

        final_clip = final_clip.set_audio(comp_audio)
        final_clip = final_clip.set_duration(tts_clip.duration)

        # Add subtitles
        final_clip = CompositeVideoClip([
            final_clip,
            subtitles
        ])

        final_clip.write_videofile(combined_image_path, threads=threads)

        success(f"Wrote Video to \"{combined_image_path}\"")

Test()