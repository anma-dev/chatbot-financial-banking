Home Trust Chatbot using Python & Flask 

## Initial Setup:

Clone repo and create a virtual environment
```
$ python3 -m venv venv
$ .venv\scripts\activate
```
Install dependencies
```
$ (venv) pip install Flask torch torchvision nltk flask-cors
```
Install nltk package
```
$ (venv) python
>>> import nltk
>>> nltk.download('punkt')
```
Modify `intents.json` with different intents and responses for your Chatbot

This will dump data.pth file. And then run
the following command to test it in the console.
```
$ (venv) python train.py
$ (venv) python chat.py
```
Run
```
$ (venv) python -m flask run
```
## Helpful Links:
Trouble with virtual environments: https://code.visualstudio.com/docs/python/tutorial-flask

<img width="269" alt="chatbot" src="https://user-images.githubusercontent.com/54012492/162278849-674ff635-2511-4312-a920-3061ee0d47f3.png">

Credits: Python Engineer
