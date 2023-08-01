from ibm_watson import SpeechToTextV1
from dotenv import load_dotenv
import os
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def config():
    load_dotenv()
    authenticator_xs = IAMAuthenticator(os.getenv('IAM_api_key'))
    speech_to_text = SpeechToTextV1(
        authenticator=authenticator_xs
    )
    speech_to_text.set_service_url(os.getenv('url_S2T'))


config()


s2t = SpeechToTextV1(iam_apikey=os.getenv('api_key_S2T'), url= os.getenv('url_S2T'))
