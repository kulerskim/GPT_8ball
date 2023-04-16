import boto3
import os
import pyaudio
import io

from config import POLLY_VOICES

class PollyTextToSpeech:
    def __init__(self, language = 'en-US'):
        self.polly_client = boto3.Session(
            aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
            aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
            region_name=os.environ['AWS_DEFAULT_REGION']
        ).client('polly')
        
        self.language = language
        self.output =io.BytesIO()

    def getStreamBytes(self, text_to_speak):
        response = self.polly_client.synthesize_speech(
                    Engine='neural',
                    LanguageCode=self.language,
                    Text=text_to_speak,
                    TextType='ssml',
                    OutputFormat='pcm',
                    VoiceId=POLLY_VOICES[self.language],
                )
        stream = response['AudioStream'].read()
        return io.BytesIO(stream)

    def playStreamBytes(self, stream):
        p = pyaudio.PyAudio()
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 16000

        stream_data = stream.read(CHUNK)
        stream_out = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                output=True)
        try:
            while len(stream_data) > 0:
                stream_out.write(stream_data)
                stream_data = stream.read(CHUNK)
        except Exception as e:
            raise e
        finally:
            stream_out.stop_stream()
            stream_out.close()

        p.terminate()


    def speak(self, text_to_speak):
        bytes = self.getStreamBytes(text_to_speak)
        self.playStreamBytes(bytes)        
        
        
