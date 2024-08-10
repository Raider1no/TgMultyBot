from faster_whisper import WhisperModel
import ffmpeg
import numpy as np

model_size = "medium"
model = WhisperModel(model_size, device="cpu", compute_type="int8", cpu_threads=8)

def speechtotext(audio_data: [float]):
    output = ""
    segments, info = model.transcribe(audio=audio_data, beam_size=2, vad_filter=True)

    for segment in segments:
        output += segment.text

    return output


def load_audio(binary_file, sr: int = 16000):
    try:
        # This launches a subprocess to decode audio while down-mixing and
        # resampling as necessary.
        # Requires the ffmpeg CLI and `ffmpeg-python` package to be installed.
        out, _ = (
            ffmpeg.input("pipe:", threads=0)
            .output("-", format="s16le", acodec="pcm_s16le", ac=1, ar=sr)
            .run(cmd="ffmpeg", capture_stdout=True, capture_stderr=True, input=binary_file)
        )
    except ffmpeg.Error as e:
        raise RuntimeError(f"Failed to load audio: {e.stderr.decode()}") from e

    return np.frombuffer(out, np.int16).flatten().astype(np.float32) / 32768.0