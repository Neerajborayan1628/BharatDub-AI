<div align="center"> <img src="images/bharatdub_ai_logo.png" width="900" alt="BharatDub AI">
🇮🇳 BharatDub AI

BharatDub AI is an end-to-end AI video dubbing pipeline focused on multilingual dubbing, with Hindi as the primary Indian-language target.

Give it a local video or YouTube URL, choose the source and target languages, and BharatDub AI can transcribe, translate, clone the speaker's voice, preserve background sound, synchronize the dubbed audio, and optionally perform lip-sync.

✨ Features

Feature

Description

🎬 YouTube Input

Paste a YouTube URL and download the source using yt-dlp.

📁 Local Video Input

Process a local video through the Gradio interface.

🌐 Multilingual Dubbing

Supports multiple source and target languages.

🇮🇳 Hindi Support

Hindi (hi) is supported and configured as the default target language.

🗣️ Voice Cloning

XTTS generates translated speech using the original speaker's voice characteristics.

🎭 Emotion Analysis

SpeechBrain can classify emotions such as neutral, happiness, sadness, and anger.

👥 Speaker Diarization

pyannote.audio identifies who is speaking and when.

✂️ Sentence Segmentation

NLTK splits transcripts into clean sentence segments.

🧠 Context-Aware Translation

MarianMT provides translation, with optional Groq/LLM processing.

👄 Optional Lip-Sync

Wav2Lip synchronizes mouth movement with generated speech.

🔊 Background Sound

Original music and ambient audio can be retained.


⚡ GPU Acceleration

CUDA GPU acceleration is supported and recommended.

🇮🇳 Hindi Language Support

Hindi is a first-class target language in BharatDub AI.

Hindi → hi

See LANGUAGE_SUPPORT.md for additional language information and verification notes.

Supported Languages

Language

Code

English

en

Spanish

es

French

fr

German

de

Italian

it

Turkish

tr

Russian

ru

Dutch

nl

Czech

cs

Arabic

ar

Chinese (Simplified)

zh-cn

Japanese

ja

Korean

ko

Hindi

hi

Hungarian

hu

Model quality and availability can vary by language.

🧠 How It Works

Local Video / YouTube URL
          │
          ▼
   Audio Extraction
          │
          ▼
   Speaker Diarization
     pyannote.audio
          │
          ▼
      Whisper STT
          │
          ▼
 Sentence Segmentation
         NLTK
          │
          ▼
      Translation
  MarianMT / optional LLM
          │
          ▼
    Emotion Analysis
      SpeechBrain
          │
          ▼
    Voice Synthesis
        XTTS v2
          │
          ├───────────────┐
          ▼               ▼
 Background Sound     Optional Wav2Lip
   Preservation          Lip-Sync
          │               │
          └───────┬───────┘
                  ▼
          Final Dubbed Video

🛠️ Technology Stack

Stage

Technology

Purpose

Video Download

yt-dlp

Download YouTube videos

Speaker Diarization

pyannote.audio

Detect speakers and speaking intervals

Transcription

Whisper / Faster-Whisper

Speech-to-text

Sentence Segmentation

NLTK

Split transcripts into sentences

Translation

MarianMT

Machine translation

Optional LLM Translation

Groq / Llama

Context-aware translation

Emotion Analysis

SpeechBrain

Emotion classification

Voice Cloning

XTTS v2

Generate translated speech

Lip-Sync

Wav2Lip

Synchronize mouth movement

Video Processing

OpenCV

Frame and face processing

Audio Processing

PyDub

Audio manipulation and mixing

Media Processing

FFmpeg

Audio/video conversion and synchronization

Web Interface

Gradio

Browser-based UI

🚀 Installation

Requirements

Windows 10/11 or Linux

Python 3.10.x

Git

FFmpeg

NVIDIA GPU with CUDA recommended

Hugging Face account/token for speaker diarization

Optional Groq API key for LLM translation

1. Clone the Repository

git clone https://github.com/Neerajborayan1628/BharatDub-AI.git
cd BharatDub-AI

2. Create an Environment


 Python venv

python -m venv .venv

Windows:

.\.venv\Scripts\Activate.ps1

Linux/macOS:

source .venv/bin/activate

3. Install FFmpeg

Windows with Winget:

winget install --id Gyan.FFmpeg.Shared -e

Verify:

ffmpeg -version

Ubuntu/Debian:

sudo apt update
sudo apt install ffmpeg

4. Install Python Dependencies

pip install -r requirements.txt

5. Configure .env

Create .env in the project root:

HF_TOKEN=your_huggingface_token
Groq_TOKEN=your_groq_token

HF_TOKEN is required for the Hugging Face speaker-diarization models.

Groq_TOKEN is optional and enables the optional LLM/context-aware translation path.


6. GPU Setup

For a CUDA 12.1 environment:

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

Verify:

import torch

print("PyTorch:", torch.__version__)
print("CUDA:", torch.cuda.is_available())

if torch.cuda.is_available():
    print("GPU:", torch.cuda.get_device_name(0))

👄 Wav2Lip

Wav2Lip is required only when lip-sync is enabled.


▶️ Usage

Gradio Web App

python app.py

Open:

http://127.0.0.1:7860

The web interface lets you configure the video, source language, target language, Whisper model, lip-sync, and background-sound options.



🎭 Emotion-Aware Voice Generation

Speech segments can be analyzed for emotions such as:

Neutral

Happiness

Sadness

Anger

The detected emotion can be used during voice synthesis to make the dubbed speech more expressive.

👄 Lip Synchronization

Lip-sync is optional and uses Wav2Lip.

For better results:

Use clear, front-facing speakers.

Prefer good-quality video.

Avoid heavily obstructed faces.

Use clean speech.

Avoid extreme camera angles.

📁 Project Structure

BharatDub-AI/
│
├── app.py
├── inference.py
├── requirements.txt
├── LANGUAGE_SUPPORT.md
├── verify_hindi_support.py
├── README.md
├── LICENSE
│
├── tools/
│   └── utils.py
│
├── Wav2Lip/
│   ├── inference.py
│   ├── face_detection/
│   ├── evaluation/
│   └── ...
│
└── images/
    └── bharatdub_ai_logo.png

Large generated media, model weights, virtual environments, and secrets should not be committed to Git.

🧪 Verify Hindi Support

python verify_hindi_support.py

⚠️ Troubleshooting

FFmpeg not found

ffmpeg -version

If the command is not found, install FFmpeg and add it to your PATH.

CUDA unavailable

import torch
print(torch.cuda.is_available())

Check your NVIDIA driver and PyTorch CUDA installation if this returns False.

Hugging Face authentication errors

Make sure:

HF_TOKEN is correct.

Required model terms have been accepted.

Your account has access to the required pyannote models.

Lip-sync errors

Make sure the required Wav2Lip model weights are configured before enabling lip-sync.

Slow processing

Use an NVIDIA CUDA GPU and an appropriate Whisper model. CPU processing can be significantly slower.

🔐 Responsible Use

BharatDub AI can clone a speaker's voice and modify video lip movement.

Please use these capabilities responsibly:

Obtain permission before cloning someone's voice or likeness.

Do not use the system for impersonation, fraud, or deception.

Respect copyright when downloading or modifying videos.

Do not process private recordings without appropriate authorization.

Comply with applicable copyright, privacy, and data-protection laws.

Clearly disclose AI-generated or AI-dubbed content where appropriate.

📚 Acknowledgements

BharatDub AI builds on open-source technologies and research from the speech, translation, and video communities, including:

Wav2Lip

pyannote.audio

Whisper / Faster-Whisper

SpeechBrain

XTTS

MarianMT

OpenCV

FFmpeg

PyDub

NLTK

Gradio

yt-dlp

Please respect the individual licenses and terms of the models and third-party projects used by BharatDub AI.

📄 License

See LICENSE for the applicable project license.

Third-party models and components may have separate licenses and terms.

🇮🇳 BharatDub AI

AI-powered multilingual video dubbing with a focus on Indian-language accessibility — starting with Hindi.