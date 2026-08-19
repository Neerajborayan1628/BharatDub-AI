<div align="center"> <img src="images/bharatdub_ai_logo.png" width="900" alt="BharatDub AI">
BharatDub AI
AI-Powered Video Dubbing — Voice Cloning, Multilingual Translation & Lip-Sync

Dub • Translate • Sync — Powered by AI Bringing global content to India


</div>
What is BharatDub AI?

BharatDub AI is an end-to-end AI video dubbing pipeline. Give it a video — a local file or a YouTube link — pick a source and target language, and it automatically:

Transcribes the spoken dialogue
Splits it into clean sentences
Translates it into the target language
Clones the original speaker's voice and emotion for the new audio
Re-syncs the dubbed audio to the video
(Optional) Matches lip movement to the new audio, frame-by-frame

Indian-language dubbing — Hindi first — is the primary focus, but the pipeline supports a wide range of languages out of the box.

✨ Features
Feature	Description
🎬 YouTube Direct Input	Paste a YouTube URL and skip manual downloading — yt-dlp handles it.
🌐 Multi-Language Dubbing	Dub across 15 languages, with Hindi supported and set as the default target language.
🗣️ AI Voice Cloning	Uses XTTS to synthesize the translated speech in the original speaker's own voice.
🎭 Emotion-Aware Synthesis	Detects emotion (anger, happiness, sadness, neutral) per segment via SpeechBrain and carries it into the dubbed audio.
👄 Dynamic Lip-Sync (optional)	Frame-level lip-sync powered by Wav2Lip, including multi-speaker scenes.
🔊 Background Sound Preservation	Keeps original ambient audio/music intact alongside the new dialogue track.
🧑‍🤝‍🧑 Speaker Diarization	Automatically detects and tracks who is speaking when, using pyannote.audio.
✂️ Sentence Tokenization	Breaks transcripts into clean, well-timed segments using NLTK for accurate translation and sync.
🧠 Context-Aware Translation (optional)	Direct translation via MarianMT, with an optional LLM pass (llama3-70b) for more natural, context-aware phrasing.
🖥️ Gradio Web App	A browser-based UI to upload a video, configure options, and run a dubbing job with no command line needed.
⚡ CPU & GPU Compatible	Runs on CPU; GPU (CUDA) strongly recommended for practical speed.
🇮🇳 Hindi Language Support

Hindi is fully supported and set as the default target language. The Gradio selector maps Hindi → hi, which is passed straight to the XTTS voice-cloning model. Full language table and verification notes live in LANGUAGE_SUPPORT.md.

<details> <summary>Full language list</summary>
Display name	Code
English	en
Spanish	es
French	fr
German	de
Italian	it
Turkish	tr
Russian	ru
Dutch	nl
Czech	cs
Arabic	ar
Chinese (Simplified)	zh-cn
Japanese	ja
Korean	ko
Hindi	hi
Hungarian	hu
</details>
🛠️ How It Works
Stage	Tech Used	What it does
Speaker Diarization	pyannote.audio	Segments audio by who's speaking, and when.
Transcription	Whisper	Converts spoken audio into text.
Sentence Segmentation	NLTK	Splits transcripts into clean, timed sentences.
Translation	MarianMT (+ optional llama3-70b)	Translates each sentence into the target language.
Emotion Analysis (optional)	SpeechBrain	Classifies emotion per audio segment.
Voice Synthesis	XTTS	Generates translated speech, cloning the original speaker's voice + emotion.
Lip-Sync (optional)	OpenCV + Wav2Lip	Detects faces and generates matching lip movement for the new audio.
Audio/Video Sync	FFmpeg	Aligns the new audio track with original video timing.
Final Mixing	PyDub	Merges the new audio with the video into the finished dubbed output.
🚀 Installation & Usage
0) Install Anaconda

Install Anaconda to manage the Python environment.

1) Create the Conda Environment
bash
conda remove -n bharatdub --all          # remove any existing env, if needed
conda create -n "bharatdub" python=3.10.14 ipython
conda activate bharatdub
2) Get the Project
bash
git clone <your-repository-url> BharatDub-AI
cd BharatDub-AI
3) Configure the .env File
bash
HF_TOKEN="your_huggingface_token"
Groq_TOKEN="your_groq_token"

[!NOTE] HF_TOKEN — from Hugging Face; required for speaker diarization. You'll also need access to pyannote/speaker-diarization-3.1.

Groq_TOKEN — from GroqCloud; optional, enables llama3-70b context-aware translation.

[!TIP] llama3-70b works best for Latin-family languages and is weaker on languages like Arabic or Mandarin. Leave the Groq field empty to skip it.

4) Install Dependencies
bash
sudo apt-get install ffmpeg
pip install -r requirements.txt
5) Enable GPU Acceleration (optional)
bash
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

Verify:

python
import torch
print(torch.cuda.is_available())
6) Download Wav2Lip Models

Needed only for lip-sync:

7) Run via Command Line
bash
python inference.py --yt_url "https://www.youtube.com/shorts/ULptP9egQ6Q" --source_language "en" --target_language "hi" --LipSync True --Bg_sound True
usage: inference.py [-h] (--yt_url YT_URL | --video_url VIDEO_URL)
                    --source_language SOURCE_LANGUAGE --target_language
                    TARGET_LANGUAGE [--whisper_model WHISPER_MODEL]
                    [--LipSync LIPSYNC] [--Bg_sound BG_SOUND]

options:
  -h, --help            show this help message and exit
  --yt_url YT_URL       YouTube single video URL
  --video_url VIDEO_URL
                        Single video URL
  --source_language SOURCE_LANGUAGE
                        Video source language
  --target_language TARGET_LANGUAGE
                        Video target language
  --whisper_model WHISPER_MODEL
                        Choose the whisper model based on your device requirements
  --LipSync LIPSYNC     Lip synchronization of the result audio to the synthesized video
  --Bg_sound BG_SOUND   Keep the background sound of the original video, though it might be slightly noisy

Output is saved to results/.

8) Launch the Gradio Web App
bash
python app.py

Then open http://localhost:7860/



BharatDub AI builds on the work of the open-source dubbing and speech AI community:

Wav2Lip — lip-sync model
Linly Dubbing
freeCodeCamp
HuggingFace video-dubbing
All the open-source model authors this project depends on
License

[!Caution] When using this tool, comply with relevant laws, including copyright, data protection, and privacy laws. Do not dub or clone the voice/likeness of any individual without their permission.

