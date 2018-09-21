import speech_recognition as sr
sample_rate = 48000
chunk_size = 4096
r = sr.Recognizer()
#prints the mic devices in list
mic_list = sr.Microphone.list_microphone_names()
print(mic_list)
print('-'*20)
print(list(enumerate(mic_list)))
print('-'*20)
device_id=0
with sr.Microphone(device_index = device_id, sample_rate = sample_rate, chunk_size = chunk_size)
as source:
    r.adjust_for_ambient_noise(source)
    print("Say something")
    #Listens to the user's input
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        #r.recognize_google(audio, key="GOOGLE_RECOGNITION_API_KEY")
        print("you said: " + text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")

    except sr.RequestError as e:
        print("Could not request results from Google \ Speech Recognition service; [0]".format(e))


        































