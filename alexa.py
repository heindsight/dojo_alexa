import speech_recognition as sr


def get_audio(recogniser):
    with sr.Microphone() as src:
        recogniser.adjust_for_ambient_noise(src)
        print("Say something")
        return recogniser.listen(src)


def get_text():
    recogniser = sr.Recognizer()

    audio = get_audio(recogniser)

    with open("sound.wav", "wb") as stream:
        stream.write(audio.get_wav_data())

    print("Analysing...")

    return recogniser.recognize_sphinx(audio)


def main():
    query = get_text()

    print("You said:", query)


if __name__ == '__main__':
    main()
