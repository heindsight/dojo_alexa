import speech_recognition as sr


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

    print("You said:", query)


if __name__ == '__main__':
    main()
