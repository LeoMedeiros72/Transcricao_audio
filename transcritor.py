# Instalar bibliotecas necessárias
!pip install -q speechrecognition pydub

import os
import speech_recognition as sr
from google.colab import files
from pydub import AudioSegment
from pydub.utils import make_chunks

# 📤 Upload do arquivo de áudio (MP3)
def upload_audio():
    uploaded = files.upload()
    return list(uploaded.keys())[0]

# 🎚️ Normaliza o volume do áudio
def normalize_audio(file_path):
    sound = AudioSegment.from_mp3(file_path)  # Carregar como mp3
    normalized = sound.apply_gain(-sound.dBFS)
    normalized_file = "normalized_audio.wav"
    normalized.export(normalized_file, format="wav")  # Exportar como WAV
    return normalized_file

# ✂️ Divide o áudio em partes menores (30s por padrão)
def split_audio(file_path, chunk_length_ms=30000):
    sound = AudioSegment.from_wav(file_path)
    chunks = make_chunks(sound, chunk_length_ms)
    chunk_files = []

    for i, chunk in enumerate(chunks):
        chunk_name = f"chunk_{i}.wav"
        chunk.export(chunk_name, format="wav")
        chunk_files.append(chunk_name)

    return chunk_files

# 🧠 Função para transcrever um único arquivo de áudio
def transcribe_audio(file_path, language="pt-BR"):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio, language=language)
    except sr.UnknownValueError:
        return "(Não foi possível entender o áudio)"
    except sr.RequestError as e:
        return f"(Erro ao conectar com o serviço: {e})"

# 📝 Função principal para executar tudo
def process_audio(file_path):
    print("🎧 Normalizando áudio...")
    normalized_file = normalize_audio(file_path)

    print("⏱️ Dividindo áudio em partes...")
    chunk_files = split_audio(normalized_file)

    print("🔍 Transcrevendo...")
    full_text = ""
    for i, chunk_file in enumerate(chunk_files):
        text = transcribe_audio(chunk_file)
        full_text += f"[Trecho {i+1}]: {text}\n"
        os.remove(chunk_file)  # Limpa o arquivo temporário

    return full_text

# 🚀 Executando o processo completo
print("📥 Faça upload do seu arquivo .mp3...")
uploaded_file = upload_audio()
transcription = process_audio(uploaded_file)

print("\n📄 Transcrição final:\n")
print(transcription)
