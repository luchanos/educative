import speech_recognition as sr
from moviepy.editor import VideoFileClip
from pydub import AudioSegment
from pydub.utils import make_chunks
import os
from tqdm import tqdm


def extract_audio_from_video(video_path: str, audio_path: str) -> None:
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path, codec='pcm_s16le')


def recognize_speech_from_audio(audio_path: str, chunk_length_ms: int = 60_000) -> str:
    audio = AudioSegment.from_wav(audio_path)
    chunks = make_chunks(audio, chunk_length_ms)

    recognizer = sr.Recognizer()
    transcription = []

    with tqdm(total=len(chunks), desc="Transcribing", unit="chunk", leave=False) as pbar:
        for i, chunk in enumerate(chunks):
            chunk_name = f"chunk{i}.wav"
            chunk.export(chunk_name, format="wav")

            with sr.AudioFile(chunk_name) as source:
                audio_listened = recognizer.record(source)
                try:
                    text = recognizer.recognize_google(audio_listened, language="ru-RU")
                    transcription.append(text)
                except sr.UnknownValueError:
                    pass
                except sr.RequestError as e:
                    tqdm.write(f"[Error] Could not request results: {e}")

            os.remove(chunk_name)
            pbar.update(1)
            pbar.set_postfix_str(f"{i + 1}/{len(chunks)} chunks")

    return " ".join(transcription)


def save_transcription_to_file(transcription: str, txt_path: str) -> None:
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(transcription)


video_path = "lection.mp4"
audio_path = "extracted_audio.wav"
txt_path = "transcription.txt"

if __name__ == "__main__":
    extract_audio_from_video(video_path, audio_path)
    transcription = recognize_speech_from_audio(audio_path)
    save_transcription_to_file(transcription, txt_path)
