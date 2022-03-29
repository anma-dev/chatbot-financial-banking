Home Trust Chatbot using Python & Flask 

## Initial Setup:

Clone repo and create a virtual environment
```
$ python3 -m venv venv
$ . venv/bin/activate
```
Install dependencies
```
$ (venv) pip install Flask torch torchvision nltk
```
Install nltk package
```
$ (venv) python
>>> import nltk
>>> nltk.download('punkt')
```
Modify `intents.json` with different intents and responses for your Chatbot

Run
```
$ (venv) python train.py
$ (venv) python -m flask run
```
This will dump data.pth file. And then run
the following command to test it in the console.
```
$ (venv) python chat.py
```
##Helpful Links:
Trouble with virtual environments: https://code.visualstudio.com/docs/python/tutorial-flask

## Credits:
This repo was used for the frontend code:
https://github.com/hitchcliff/front-end-chatjs & Python Engineer
