# Whisper Transcriptions

A Python utility designed to batch transcribe `.wav` audio files into formatted `.docx` documents using OpenAI's Whisper model.

## Features
* **Batch Processing:** Automatically finds all WAV files in a source directory.
* **Word Export:** Saves each transcription as a separate Word document.
* **CLI Support:** Run directly from your terminal as a command.
* **Library Support:** Import the core function into other Python scripts.

---

## Prerequisites

### 1. FFmpeg (Required)
OpenAI's Whisper requires `ffmpeg` to process audio files.
* **Windows:** Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add the `bin` folder to your **System PATH**.
* **macOS:** Run `brew install ffmpeg`

---

## Installation

Since this is a package, you can install it directly into any virtual environment via GitHub:

```powershell
pip install git+[https://github.com/benma/Whisper_Transcriptions.git](https://github.com/benma/Whisper_Transcriptions.git)

## Usage

#As a terminal command:
whisper-run "C:\path\to\your\wav_files" "C:\path\to\save\docx_files"

#As a python library:

from whisper_transcribe.transcriber import transcribe_wav

transcribe_wav("./audio_input", "./transcripts_output")

##Structure:

Whisper_Transcriptions/
├── pyproject.toml         # Build metadata and dependencies
├── src/
│   └── whisper_transcribe/
│       ├── __init__.py    # Makes the folder a package
│       └── transcriber.py # Main transcription logic
└── README.md              # You are here!
