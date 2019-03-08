import codecs
import json
import logging
import time
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import requests


class Synthesizer(object):
    def __init__(self, api_id, api_token, lang, api_url='http://api.azreco.az/synthesize'):
        self.api_id = api_id
        self.api_token = api_token
        self.lang = lang
        self.api_url = api_url

    def synthesize(self, opts):
        """
        Upload a new text file to azreco to convert into the speech
        If upload suceeds then this method will return the audio in wave format
        """

        params = {'api_id':int(self.api_id),'api_token': self.api_token, 'lang':self.lang}
        try:
            files={'file':open(opts.text, "rb")}
        except IOError as ex:
            logging.error("Problem opening text file {}".format(opts.text))
            raise

        lang = {"lang": opts.lang}

        request = requests.post(self.api_url, files=files, params=params)
        if request.status_code == 200:
            return request.content
        else:
            logging.error("{}".format(request.text))
            raise Exception("Text-to-speech failed.")

def parse_args():
    """
    Parse command line arguments
    """

    # Parse the arguments
    parser = ArgumentParser(
        description='Convert your text into the speech through the Azreco text-to-speech API',
        formatter_class=ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument('-t', '--text', type=str, required=True,
                        help="Text file to be processed")
    parser.add_argument('-o', '--output', type=str, required=True,
                        help="Output wave filename")
    parser.add_argument('-i', '--id', type=str, required=True,
                        help="Your text-to-speech API ID")
    parser.add_argument('-k', '--token', type=str, required=True,
                        help="Your text-to-speech API Token")
    parser.add_argument('-l', '--lang', type=str, required=True,
                        help="Code of language to use (e.g., az-AZ, tr-TR)")
    parsed = parser.parse_args()

    return parsed


def main():
    """
    Example way to use the Azreco Client to convert you text into the speech
    """
    logging.basicConfig(level=logging.INFO)

    opts = parse_args()

    client = Synthesizer(opts.id, opts.token, opts.lang)

    result = client.synthesize(opts)
    with open(opts.output, "wb") as out:
        out.write(result)
    logging.info("Your audio has been written to file {}".format(opts.output))

if __name__ == '__main__':
    main()
