from moviepy.audio.AudioClip import CompositeAudioClip
from moviepy.audio.fx.volumex import volumex
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.VideoClip import ColorClip, TextClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.fx import loop, resize

from helpers import cat


def main():
    clip = ColorClip(size=(1080, 1920), color=[255, 255, 255], duration=10)

    audioClip = AudioFileClip("audio/Cat Circus - Doug Maxwell.mp3").set_duration(clip.duration)
    audioClip = volumex(audioClip, 0.1)

    #gif = cat.get_cat_gif()
    gif = 'temp/img.gif'
    gifClip = VideoFileClip(gif).set_position(('center', 350)).set_duration(clip.duration)
    loopGifClip = loop.loop(gifClip, duration=clip.duration)
    bigGifClip = resize.resize(loopGifClip, (gifClip.w * 2, gifClip.h * 2))

    textClip = TextClip(txt='Cat Facts #1', font="Amiri-Bold", fontsize=150, color="black").set_duration(clip.duration)
    textClip = textClip.set_position(('center', 100))

    fact = cat.get_cat_fact()
    factClip = TextClip(txt=fact, font="Amiri-Bold", size=(900, 800), fontsize=100, color="black",
                        method='caption').set_duration(clip.duration)

    voice = cat.get_fact_audio(fact)
    voiceClip = AudioFileClip(voice)
    voiceClip = volumex(voiceClip, 3)

    y = 350 + bigGifClip.h

    factClip = factClip.set_position(('center', y))

    video = CompositeVideoClip([clip, bigGifClip, textClip, factClip])
    new_audioclip = CompositeAudioClip([audioClip, voiceClip])
    video.audio = new_audioclip

    video.write_videofile("movie.mp4", codec='libx264',
                          audio_codec='aac')


if __name__ == '__main__':
    main()
