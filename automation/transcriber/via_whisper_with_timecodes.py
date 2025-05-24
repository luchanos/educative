from datetime import timedelta
import whisper
from moviepy.editor import VideoFileClip


def format_time(seconds: float) -> str:
    """Форматирует секунды в вид 00:00:00"""
    return str(timedelta(seconds=int(seconds)))

def transcribe_audio(audio_path: str, model_size: str = "large", step_seconds: int = 15) -> list:
    model = whisper.load_model(model_size)
    result = model.transcribe(audio_path, language="ru", verbose=False)
    segments = result["segments"]

    grouped = []
    current_start = 0
    current_text = []

    for segment in segments:
        if segment["start"] >= current_start + step_seconds:
            # Сохраняем блок
            grouped.append((format_time(current_start), " ".join(current_text)))
            # Обновляем старт
            current_start += step_seconds
            current_text = []

        current_text.append(segment["text"])

    # Добавляем последний блок, если есть
    if current_text:
        grouped.append((format_time(current_start), " ".join(current_text)))

    return grouped

def save_transcription_to_file(transcription: list, txt_path: str) -> None:
    with open(txt_path, "w", encoding="utf-8") as f:
        for timestamp, text in transcription:
            f.write(f"[{timestamp}] {text}\n\n")

def extract_audio_from_video(video_path: str, audio_path: str) -> None:
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)  # Whisper сам справится с форматом


video_path = "Transcription.mov"
audio_path = "extracted_audio_from_interview.wav"  # можно mp3 или wav, Whisper неважно
txt_path = "transcription_from_interview_via_whisper_with_timecodes.txt"


if __name__ == "__main__":
    extract_audio_from_video(video_path, audio_path)
    transcription = transcribe_audio(audio_path)
    save_transcription_to_file(transcription, txt_path)
