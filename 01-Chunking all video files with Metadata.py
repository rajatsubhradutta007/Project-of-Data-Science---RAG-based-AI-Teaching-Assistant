import whisper
import json
import os

model = whisper.load_model("large-v2")

Audios = os.listdir("Audios")

for audio in Audios:
    if("-" in audio):
        number = audio.split("-")[0]
        title = audio.split("-")[1][:-4]
        print(number , title)
        result = model.transcribe(audio = f"Audios/{audio}",
        # result = model.transcribe(audio = f"audios/sample.mp3",
                              language = "en",
                              task = "translate",
                              word_timestamps = False)
        
        chunks = []
        for segment in result["segments"]:
            chunks.append({"number" : number , "title" : title , "start" : segment["start"] , "end" : segment["end"] , "text" : segment["text"]})

        chunks_with_metadata = {"chunks" : chunks , "text" : result["text"]}
        with open(f"jsons/{audio}.json" , "w") as f:
            json.dump(chunks_with_metadata , f)