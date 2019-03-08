# AzReco Speech Recognition API Python example
Example python script to help you integrate with our speech recognition API.

This is an example python script for uploading audio(.wav , .mp3 , .opus, .m4a) or video(.mp4 , .mkv) file and saving the transcript into a .json file.

# Supporting languages
AZERBAIJANI (az-AZ)

TURKISH  (tr-TR)

RUSSIAN  (ru-RU)

# Requirements

You will need to have the requests module installed in your Python environment.

pip install requests

# Usage example:

python client.py -a audio/example-ru.wav -l ru-RU -i api_user_id -k api_token -o example-ru.json  

In this example the script uploads 'example.wav', transcribes it using our ru-RU speech to text and saves the resulting transcription as 'example.json' when the transcribing process finished.


# How to get user id and token?

To get user id and API token, send a request to info@azreco.az.
To confirm your request, we will ask you some details about your purpose in using API.
