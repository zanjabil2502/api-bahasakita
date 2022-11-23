import gradio as gr
import requests

# Set Token
token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoibWV0cm90diIsInBhc3N3b3JkIjoibWV0cm90djEyMyJ9.b7wTuaEZRgoY3KTFP8JqcIT84ewdR6hv9fd7Tms4lSE'

# Set Input
url = None  # String | None, url youtube for download video
filename = 'example.mp4' # String | None, file path audio

# Encode File to Base64
data_base64 = gr.processing_utils.encode_url_or_file_to_base64(filename)
data = {
    'name': filename,
    'data': data_base64,
}


lang = 'Indonesian' # Set Language
diarization = True # Bool, if true, you activate diarization process

# Request fot Post to API
req = requests.post(url='http://bhskita.dynu.com:1221/run/predict',json={
            "data": [token,url,data,lang,diarization]
        }).json()

print(req)
 