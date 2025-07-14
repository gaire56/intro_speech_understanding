import datetime, gtts, bs4, random, speech_recognition

def what_time_is_it(lang, filename):
    '''
    Tell me what time it is.
    
    Parameters:
    lang (str) - language in which to speak
    filename (str) - the filename into which the audio should be recorded
    '''
    #raise RuntimeError("You need to write this part!")

    (date, time) = datetime.datetime.now().isoformat().split("T")
    (hour, minutes, seconds) = time.split(":")
    if lang=="en":
        text = hour+" hours and "+minutes+" minutes"
    elif lang=="ja":
        text = hour+"時"+minutes+"分です"
    elif lang=="zh":
        text = "现在是"+hour+"点"+"分"
    else:
        text="I'm sorry, I don't know that language"
    gtts.gTTS(text,lang=lang).save(filename)
    
def tell_me_a_joke(lang, audiofile):
    '''
    Tell me a joke.
    
    @params:
    filename (str) - filename containing the database of jokes
    lang (str) - language
    audiofile (str) - audiofile in which to record the joke
    '''
    #raise RuntimeError("You need to write this part!")
    filename = 'jokes_%s.txt'%(lang)
    with open(filename) as f:
        jokes = f.readlines()
    joke = random.choice(jokes)
    print(joke.strip())
    gtts.gTTS(joke.strip(), lang=lang).save(audiofile)

def what_day_is_it(lang, audiofile):
    '''
    Tell me what day it is.

    @params:
    lang (str) - language in which to record the date
    audiofile (str) - filename in which to read the date
    
    @returns:
    url (str) - URL that you can look up in order to see the calendar for this month and year
    '''
    # raise RuntimeError("You need to write this part!")
    today = datetime.date.today()
    year = today.year
    month = today.month
    day = today.day
    weekday = today.isoweekday()
    if lang=="en":
        weekdays=['','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        months=['','January','February','March','April','May','June','July','August','September','October','November','December']
        text = "%s, %s %d, %d"%(weekdays[weekday],months[month],day,year)
        gtts.gTTS("Today is "+text,lang="en").save(audiofile)
    elif lang=="ja":
        weekdays=' 月火水木金土日'
        text="%s曜日,%d月%d日, %d年"%(weekdays[weekday],month,day,year)
        gtts.gTTS("今日は"+text,lang="ja").save(audiofile)
    elif lang=="zh":
        weekdays=['','周一','周二','周三','周四','周五','周六','星期日']
        text='%s, %d月%d日, %d年'%(weekdays[weekday],month,day,year)
        gtts.gTTS("今天是"+text,lang="zh").save(audiofile)

def personal_assistant(lang, filename):
    '''
    Listen to the user, and respond to one of three types of requests:
    What time is it?
    What day is it?
    Tell me a joke!
    
    @params:
    lang (str) - language
    filename (str) - filename in which to store the result
    '''
    # raise RuntimeError("You need to write this part!")
    if lang=="en":
        keywords = ["what time", "joke", "what day", "I'm sorry, I didn't understand you"]
    elif lang=="ja":
        keywords = ["何時","冗談","何日","すみません、よくわかりませんでした"]
    elif lang=="zh":
        keywords = ["几奌","玩笑","什么日子","对不起，我没听懂你的话"]
    else:
        speech_package.synthesize("I don't know that language!","en",filename)
        return

    r = speech_recognition.Recognizer()

    while True:
        print('Listening...')
        with speech_recognition.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            try:
                audio = r.listen(source)
                text = r.recognize_google(audio, language=lang)
            except speech_recognition.UnknownValueError:
                print('I did not understand that, I will try again')
                continue
            except sr.RequestError:
                print('Sorry, I could not reach the internet, I will try again')
                continue
            except sr.WaitTimeoutError:
                continue
            
        print("I heard",text)
        if keywords[0] in text:
            what_time_is_it(lang, filename)
            break
        elif keywords[1] in text:
            tell_me_a_joke(lang, filename)
            break
        elif keywords[2] in text:
            what_day_is_it(lang, filename)
        else:
            print(keywords[3])
            print('I will try again')