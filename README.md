# Intelligent Chatbot for the Banking, Financial Industry 

This project is built using Python, Flask, HTMl, CSS, Javascript, and Natural Language Processing (NLTK). It includes some basic neural networks for processing updated data (.json format) to train the chatbot to update its responses. 

This chatbot was made to save time for team leads and make the onboarding process for new employees smoother. Onboarding to a new company takes time and new knowledge of terms, proccesses, and company specific 'lingo'. The chatbot helps employees in gaining a baseline knowledge of information, while also helping experienced developers gain knowledge from other projects. This chatbot is mainly focused to help the banking/financial industry, specifically knowledge related to mortgages and loan processes. 

A focus of this project is keeping it accessible to various teams within a company and having its data updated to ensure its knowledge remains current. This led to the idea of building a 'data dictionary' for team leads of different knowledge levels to contribute to the chatbot, maintaing its usability and ensuring it remains in use for the foreseeable future. 

## Demonstration 
<img width="269" alt="chatbot" src="https://user-images.githubusercontent.com/54012492/162278849-674ff635-2511-4312-a920-3061ee0d47f3.png">

### Initial Setup:

Create a virtual environment
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

**Helpful Links:**
Trouble with virtual environments: https://code.visualstudio.com/docs/python/tutorial-flask
