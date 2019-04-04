import speech_recognition as sr

import webbrowser


def get_audio(recogniser):
    with sr.Microphone() as src:
        print("Say something")
        return recogniser.listen(src)


def get_text():
    recogniser = sr.Recognizer()

    audio = get_audio(recogniser)

    return recogniser.recognize_sphinx(audio)


def main():
    query = get_text()

    print("You said:", query or 'truck')
    webbrowser.open('https://unsplash.com/search/photos/%s' % query, new=0, autoraise=True)


if __name__ == '__main__':
    main()
