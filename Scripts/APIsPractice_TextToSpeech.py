from ibm_watson import SpeechToTextV1
from dotenv import load_dotenv
import json
import os
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()
authenticator_xs = IAMAuthenticator(os.getenv('IAM_api_key'))
speech_to_text = SpeechToTextV1(
    authenticator=authenticator_xs
    )
speech_to_text.set_service_url(os.getenv('url_S2T'))

"""This a project to understand the basics of the Speech to text API"""


with open('C:/Users/Dell Latitud E7450/PycharmProjects/API/Testdata/Bob Marley  redemption song (Vocals Only).mp3','rb') as audio_file:
    speech_results = speech_to_text.recognize(
        audio= audio_file,
        content_type= 'audio/mp3',
    ).get_result()

print(json.dumps(speech_results, indent=2))

transcripted = speech_results['results'][0]['alternatives'][0]['transcript']

print(transcripted)

#transcripted_file = open('C:/Users/Dell Latitud E7450/PycharmProjects/API/Transcripted data/file1.txt','w+')
#transcripted_file.writelines(transcripted)
#transcripted_file.close()