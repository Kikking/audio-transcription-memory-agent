import google.generativeai as genai

# Initialize the client
genai.configure(api_key="AIzaSyCpzAmARWnkqMc9Fn_3Tz5P54wC0LVVUCYMCA")

model = genai.GenerativeModel("gemini-3-flash-preview")

# Upload a single test file
audio_file = genai.upload_file("audiofiles/Recording.m4a")

print(f"File uploaded: {audio_file.display_name}")

response = model.generate_content([
    "Transcribe this audio file exactly. Only return the transcription.",
    audio_file
])

with open("transcriptionfiles/transcription.txt", "a") as file:
    file.write(response.text)
# 5. Print the result
print(response.text)
