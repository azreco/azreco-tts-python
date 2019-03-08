# AzReco Text To Speech API Python example
Example python script to help you integrate with our text-to-speech API.

This is an example python script for uploading text file and saving the audio into a .wav file.

# Supporting languages
AZERBAIJANI (az-AZ)

TURKISH  (tr-TR)

# Requirements

You will need to have the requests module installed in your Python environment.

pip install requests

# Usage example:

python client.py -t text/example-tr.txt -l tr-TR -i api_user_id -k api_token -o example-tr.wav  

In this example the script uploads 'example-tr.txt', synthesizes speech using our tr-TR text-to-speech and saves the resulting audio as 'example-tr.wav' when the synthesizing process finished.


# How to get user id and token?

To get user id and API token, send a request to info@azreco.az.
To confirm your request, we will ask you some details about your purpose in using API.
