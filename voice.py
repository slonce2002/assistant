import os
import wave
import pyaudio
import openai
from config import OPENAI_API_KEY
import pyttsx3

# Initialize TTS
engine = pyttsx3.init()
engine.setProperty("rate", 150)

# Configure OpenAI
openai.api_key = OPENAI_API_KEY

def speak(text: str):
    engine.say(text)
    engine.runAndWait()

def record_audio(filename="input.wav", record_seconds=5, mic_index=None):
    """Record `record_seconds` of audio to a WAV file."""
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000

    p = pyaudio.PyAudio()
    params = {
        "format": FORMAT,
        "channels": CHANNELS,
        "rate": RATE,
        "input": True,
        "frames_per_buffer": CHUNK,
    }
    if mic_index is not None:
        params["input_device_index"] = mic_index

    stream = p.open(**params)
    print(f"Recording {record_seconds}s of audio…")
    frames = [stream.read(CHUNK) for _ in range(int(RATE / CHUNK * record_seconds))]
    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    return filename

def listen(record_seconds: int = 5, mic_index: int = None) -> str:
    """
    Records audio, sends it to Whisper via the OpenAI API, and returns the transcript.
    Falls back to empty string on error.
    """
    try:
        wav_path = record_audio(record_seconds=record_seconds, mic_index=mic_index)
        with open(wav_path, "rb") as audio_file:
            # New interface for openai-python >=1.0.0
            resp = openai.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file
            )
        text = resp["text"].strip().lower()
        print(f"You said: {text}")
        return text
    except Exception as e:
        print(f"Whisper transcription failed: {e}")
        return ""

