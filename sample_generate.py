import soundfile as sf
from EasyTTS.inference.TTS import TTS

tts = TTS(lang="fr") # Instantiate the model for your language
audio = tts.predict(text="Bonjour à tous") # Make a prediction

sf.write('./audio_pip.wav', audio, 22050, "PCM_16") # Save output in .WAV file
