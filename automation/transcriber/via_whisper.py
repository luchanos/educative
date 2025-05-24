import whisper
from moviepy.editor import VideoFileClip


def extract_audio_from_video(video_path: str, audio_path: str) -> None:
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)  # Whisper сам справится с форматом


def transcribe_audio(audio_path: str, model_size: str = "medium") -> str:
    model = whisper.load_model(model_size)
    result = model.transcribe(audio_path, language="ru")  # укажем явно русский
    return result["text"]


def save_transcription_to_file(transcription: str, txt_path: str) -> None:
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(transcription)


video_path = ""
audio_path = ""  # можно mp3 или wav, Whisper неважно
txt_path = ""

if __name__ == "__main__":
    extract_audio_from_video(video_path, audio_path)
    transcription = transcribe_audio(audio_path)
    save_transcription_to_file(transcription, txt_path)
