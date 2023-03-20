import whisper
# Modelo a utilizar, desde el menos eficaz pero mas veloz hasta el mas eficaz pero lento, medium es el promedio
model = whisper.load_model("medium") 
result = model.transcribe("PearlJam_EvenFlow.mp3")
print(result["text"])