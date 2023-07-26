# Puchu AI Desktop Assistant

Puchu AI is a simple desktop assistant script that allows you to interact with your computer using voice commands. The assistant can perform various tasks, including opening websites, playing music, and providing the current time.

## Requirements

Before running the script, make sure you have the following Python packages installed:

- pyttsx3
- speech_recognition
- pygame

You can install these packages using pip:


## Usage

1. Clone the repository and navigate to the project folder.

2. Run the `openAitest.py` script using Python:


3. The assistant will greet you and start listening for your commands.

## Features

### Speech Recognition

The assistant uses the `speech_recognition` package to recognize your voice commands. Speak clearly and wait for the assistant to process your input.

### Open Websites

You can ask the assistant to open popular websites by saying "open <website_name>". For example, saying "open Google" will open Google in your default web browser.

### Play Music

To play music, say "open music". The assistant will play a pre-defined music file using the `pygame` package.

### Stop Music

To stop the music, say "stop music". The assistant will stop the currently playing music.

### Current Time

You can ask the assistant for the current time by saying "the time". The assistant will respond with the current time in hours, minutes, and seconds.

### Exit the Assistant

To exit the assistant, simply say "exit", and the assistant will bid you farewell and terminate.

## Extending the Assistant

You can extend the capabilities of the assistant by adding more voice commands and actions. The script currently supports opening websites, playing music, and providing the current time. You can customize the list of websites or add new features based on your preferences.

## Note

This project uses the GPT-3.5 Turbo model from OpenAI for speech recognition and text-to-speech tasks. To use the OpenAI API, you need to set up an API key. Please refer to the OpenAI documentation for more information on how to obtain and use the API key.




