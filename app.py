import streamlit as st
import pandas as pd
from PIL import Image
import time
import os
import screen_brightness_control as sbc
from playsound import playsound
from gtts import gTTS
import webbrowser
import wikipedia
import pandas as pd 
import random
import pyautogui
import PyPDF2
import docx;

#==================================================================

n2="sudharshan"
z="sir"
num=1

def voice(txt):
    print("hi")
numwe = 1
numwe2=1
def tvoice2(output):
    global numwe

    # num to rename every audio file
    # with different name to remove ambiguity
    numwe += 1

    toSpeak = gTTS(text = output, lang ='hi', slow = False)
    # saving the audio file given by google text to speech
    file = str(num)+".mp3"
    toSpeak.save(file)
    
    # playsound package is used to play the same file.
    playsound(file, True)
    os.remove(file)

numw = 1
numw2=1
def tvoice(output):
    global numw

    # num to rename every audio file
    # with different name to remove ambiguity
    numw += 1
    st.write("Kural : ", output)

    toSpeak = gTTS(text = output, lang ='ta', slow = False)
    # saving the audio file given by google text to speech
    file = str(num)+".mp3"
    toSpeak.save(file)
    
    # playsound package is used to play the same file.
    playsound(file, True)
    os.remove(file)

def printsv(text):
    from plyer import notification
    notification.notify(title = "Tris",message=text ,timeout=2)

#----------------------------------------------------------------------

def wordre(filename):
    doc=docx.Document(filename)
    fullText=[]
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

def pdfre(filename):
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage(0)
    a=pageObj.extractText()
    pdfFileObj.close()
    return a

def tellDate():
    a=time.asctime(time.localtime(time.time()))
    b,c,d,e,f,g,h,i=a[:3],a[4:7],a[8:10],a[11:19],a[20:],int(a[11:13]),int(a[14:16]),int(a[17:19])
    greet3=b+'day'+str(d)+"th"+" "+c+str(f)               # telling date and month
    voice(greet3)

def tellTime(): 
    a=time.asctime(time.localtime(time.time()))
    b,c,d,e,f,g,h,i=a[:3],a[4:7],a[8:10],a[11:19],a[20:],int(a[11:13]),int(a[14:16]),int(a[17:19])
    k=g
    if g<1:
        k=12
    if g>12:
        k=g-12
    if g>=12:
        j="PM"
    else:
        j="AM"
    greet20="time is %d"%k
    greet2=greet20+" "+str(h)+j                      # telling time
    voice(greet2)

def doha():
    dah=random.randint(0,4)
    if dah==0:
        st.write("Dohe        : मैं जानूँ मन मरि गया, मरि के हुआ भूत | , मूये पीछे उठि लगा, ऐसा मेरा पूत ||")
        tvoice2("मैं जानूँ मन मरि गया, मरि के हुआ भूत | , मूये पीछे उठि लगा, ऐसा मेरा पूत ")
        st.write("Translation : main jaanoon man mari gaya, mari ke hua bhoot | , mooye peechhe uthi laga, aisa mera poot")
        st.write("Meaning     : By mistake I had known that my mind was full, but he became a ghost after death. Even after death it got up and followed me, this is how my mind is like a child.")  
    elif dah==1:
        st.write("Dohe        : भक्त मरे क्या रोइये, जो अपने घर जाय | रोइये साकट बपुरे, हाटों हाट बिकाय ||")
        tvoice2("भक्त मरे क्या रोइये, जो अपने घर जाय | रोइये साकट बपुरे, हाटों हाट बिकाय")
        st.write("Translation : bhakt mare kya roiye, jo apane ghar jaay | roiye saakat bapure, haaton haat bikaay")
        st.write("Meaning     : Why do saints who have attained their imperishable home in the form of welfare, leave the body of such a devotee? ")
    elif dah==2:
        st.write("Dohe        : मैं मेरा घर जालिया, लिया पलीता हाथ |जो घर जारो आपना, चलो हमारे साथ ||")
        tvoice2("मैं मेरा घर जालिया, लिया पलीता हाथ |जो घर जारो आपना, चलो हमारे साथ ")
        st.write("Translation : main mera ghar jaaliya, liya paleeta haath |jo ghar jaaro aapana, chalo hamaare saath ")
        st.write("Meaning     : The world - in the body I - the ego of mineness - affection is happening - take the fire of knowledge in hand and burn this house. Your ego - sets the house on fire.")
    elif dah==3:
        st.write("Dohe        : मैं मेरा घर जालिया, लिया पलीता हाथ |जो घर जारो आपना, चलो हमारे साथ ||")
        tvoice2("मैं मेरा घर जालिया, लिया पलीता हाथ |जो घर जारो आपना, चलो हमारे साथ")
        st.write("Translation : shabd vichaaree jo chale, gurumukh hoy nihaal | kaam krodh vyaapai nahin, kaboon na graasai kaal ")
        st.write("Meaning     : The one who behaves by thinking of the words of Gurmukh, becomes fruitful. He is not tormented by lust and anger and he never falls in the mouth of imagination.")
    elif dah==4:
        st.write("Dohe        : शब्द विचारी जो चले, गुरुमुख होय निहाल | काम क्रोध व्यापै नहीं, कबूँ न ग्रासै काल ||")
        tvoice2("शब्द विचारी जो चले, गुरुमुख होय निहाल | काम क्रोध व्यापै नहीं, कबूँ न ग्रासै काल ")
        st.write("Translation : jab lag aash shareer kee, miratak hua na jaay | kaaya maaya man tajai, chaude raha bajaay")
        st.write("Meaning     : As long as there is hope and attachment to the body, one cannot destroy the mind. That's why after removing the attachment of the body and the lust of the mind, one should sit in the field of satsang.")
    else:
        st.write("Dohe        : जब लग आश शरीर की, मिरतक हुआ न जाय | काया माया मन तजै, चौड़े रहा बजाय ||")
        tvoice2(" जब लग आश शरीर की, मिरतक हुआ न जाय | काया माया मन तजै, चौड़े रहा बजाय ")
        st.write("Translation : main jaanoon man mari gaya, mari ke hua bhoot | , mooye peechhe uthi laga, aisa mera poot")
        st.write("Meaning     : By mistake I had known that my mind was full, but he became a ghost after death. Even after death it got up and followed me, this is how my mind is like a child.")

def decv():
    try:
        from ctypes import cast, POINTER
        from comtypes import CLSCTX_ALL
        from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
        import math
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        currentVolumeDb = volume.GetMasterVolumeLevel()
        volume.GetMasterVolumeLevel()
        volume.SetMasterVolumeLevel(currentVolumeDb - 10.0, None)
        volume.GetMasterVolumeLevel()

    except:
        st.write("Minimum Volume Attained "+z)
        voice("Minimum volume attained "+z)

def incv():
    try:
        from ctypes import cast, POINTER
        from comtypes import CLSCTX_ALL
        from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
        import math
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        currentVolumeDb = volume.GetMasterVolumeLevel()
        volume.GetMasterVolumeLevel()
        volume.SetMasterVolumeLevel(currentVolumeDb + 10.0, None)
        volume.GetMasterVolumeLevel()

    except:
        st.write("Maximum Volume Attained "+z)
        voice("Maximum volume attained "+z)

def qp(asd):
        if "open google" in asd:
            voice("Opening Google ")
            webbrowser.open("www.google.com")
        
        elif "good word" in asd:
            import streamlit as st
            import random
            df=pd.read_csv(r"Thirukural.csv")
            df2=pd.read_csv(r"Thirukural With Explanation.csv")
            
            #replacing tabs with spaces to read clearly
            df['Verse']=df['Verse'].str.replace('\t',' ')
            # I dont see more difference between df and df_exp than an Explanation column.
            #Adding the Explanation column to df.
            df.loc[:,'Explanation']=df2.loc[:,'Explanation']
            df.reset_index()
                
            sv=random.randint(0,1329)
            result = df.loc[sv]
            tvoice(result["Verse"])
            #st.write("Kural        :",result["Verse"])
            st.write("Kural Number :",sv)
            st.write("Translation  :",result["Translation"])
            st.write("Meaning      :",result["Explanation"].split("Explanation :")[1])
            st.write("Paal         :",result["Chapter Name"])
            st.write("Adigaram     :",result["Section Name"])


        elif "open chrome" in asd:
            voice("Opening Google Chrome ")
            webbrowser.open("www.google.com")
            

        elif "open brave" in asd:
            voice("Opening Brave ")
            webbrowser.open("www.google.com")
            
        
        elif "open browser" in asd:
            voice("Opening Browser ")
            webbrowser.open("www.google.com")

        elif "today date" in asd:
            tellDate()
        
        elif "tell me a joke" in asd:
            import streamlit as st
            import pyjokes
            jo = pyjokes.get_joke(language="en", category="neutral")
            st.write(jo)
            voice(jo)

        elif "set task" in asd:
            import streamlit as st
            voice("Say your tasks "+z+"...")
            stas=st.text_input("Enter the event")
            file = open("example.txt", "w")
            file.write(" "+stas+"\n")
            file.close()
            st.success("Successfully updated ...")

        elif "my task" in asd:
            import streamlit as st
            file = open("example.txt", "r")
            contents = file.read()
            file.close()
            st.write(contents)
            voice("Your tasks :\n"+contents)
        
        elif "fortune time" in asd:
            import streamlit as st
            st.write("Fortune Teller!!!")
            voice("Enter The Event"+z)
            a=st.text_input("Enter the event")
            if a != "":
                import random
                s=random.randint(1,8)
                if s==1:
                    st.write(a," will not happen in this lifetime!!!")
                    voice(a+" will not happen in this lifetime!!!")
                elif s==2:
                    st.write(a," will happen surely!!!")
                    voice(a+" will happen surely!!!")
                elif s==3:
                    st.write(a," will happen when you are 80 years!!!")
                    voice(a+" will happen when you are 80 years!!!")
                elif s==4:
                    st.write(a," may or may not happen!!!")
                    voice(a+" may or may not happen!!!")
                elif s==5:
                    st.write(a," will happen when you lose something which you like the most!!!")
                    voice(a+" will happen when you lose something which you like the most!!!")
                elif s==6:
                    st.write(a," can happen under gods grace!!!")
                    voice(a+" can happen under gods grace!!!")
                elif s==7:
                    st.write(a," will happen after a lot of struggle!!!")
                    voice(a+" will happen after a lot of struggle!!!")
                elif s==8:
                    st.write(a," will happen soon!!!")
                    voice(a+" will happen soon!!!")
                
                else:
                    st.write(a," will not happen!!!")
                    voice(a+" will not happen!!!")
            
            else:
                st.write("Please enter an event to check")
            time.sleep(3)
            st.warning("Note: Future changes every second and this may or may not happen")

        
        
        elif "tell me the time" in asd:
            tellTime()
        
        elif "bye" in asd:
                voice("Bye. Have a great day"+z)
                playsound(r"katham.mp3")
            
                # Simulate pressing the "Ctrl" key
                pyautogui.keyDown('ctrl')
                # Add a delay to keep the "Ctrl" key pressed for a moment
                time.sleep(2)
                pyautogui.keyDown('w')
                # Add a delay to keep the "Ctrl" key pressed for a moment
                time.sleep(2)
                pyautogui.keyUp('w')
                # Simulate releasing the "Ctrl" key
                pyautogui.keyUp('ctrl') 
        
        elif "search wikipedia" in asd:
        # if any one wants to have a information
        # from wikipedia
            voice("Checking the wikipedia ")
            asd = asd.replace("wikipedia", "")
        # it will give the summary of 4 lines from
        # wikipedia we can increase and decrease it also.
            result = wikipedia.summary(asd, sentences=4)
            voice("According to wikipedia")
            voice(result)


        elif "dohe" in asd:
            doha()
        

        elif "who are you" in asd:
            playsound(r"bhasha.mp3")

        elif "decrease brightness" in asd:
            for bri in sbc.get_brightness():
                if bri<10:
                    sbc.set_brightness(0)
                else:
                    sbc.set_brightness(bri-10)

        elif "increase brightness" in asd:
            for bri in sbc.get_brightness():
                if bri>90:
                    sbc.set_brightness(100)
                else:
                    sbc.set_brightness(bri+10)

            
        
        elif "tris" in asd:
                voice("Welcome to Integrated virtual automated machine system")
                firstgrt()
                            

def firstgrt():
        #---------------------------------------------------------------------- Telling time and greeting
        time.sleep(1)
        a=time.asctime(time.localtime(time.time()))
        b,c,d,e,f,g,h,i=a[:3],a[4:7],a[8:10],a[11:19],a[20:],int(a[11:13]),int(a[14:16]),int(a[17:19])
        if g>=0 and g<4:
                st.write("Itz Mid Night "+z+"!!!\nStill",6-g,"Hours to dawn!!!")
                printsv("Itz Mid Night "+z+"!!!\nStill"+str(6-g)+"Hours to dawn!!!")
                greet="Itz Mid Night"+z
        if g>=4 and g<7:
                st.write("Its Early Moring "+z+"!!!")
                printsv("Its Early Moring "+z+"!!!")
                greet="Its Early Moring"+z
        if g>=7 and g<12:
                st.write("Good Morning "+z+"!!!")
                printsv("Good Morning "+z+"!!!")
                greet="Good Morning "+z
        if g>=12 and g<16:
                st.write("Good Afternoon "+z+"!!")
                printsv("Good Afternoon "+z+"!!")
                greet="Good Afternoon "+z
        if g>=16 and g<20:
                st.write("Good Evening "+z+"!!!")
                printsv("Good Evening "+z+"!!!")
                greet="Good Evening "+z
        if g>=20:
                st.write("Seems we are gonna have a wonderful night today "+z)
                printsv("Seems we are gonna have a wonderful night today "+z)
                greet="seems we are gonna have a wonderful night today "+z

        voice(greet)


        k=g    
        if g<1:
                k=12
        if g>12:
                k=g-12    
        if g>=12:
                j="PM"
        else:
                j="AM"
        time.sleep(1)
        st.write("\nDay   :",b)
        st.write("Month :",c)
        st.write('Date  :',d)
        st.write('Year  :',f)
        st.write('Time  :',e,"   OR   ",k,":",h,":",i,j)
        printsv("\nDay   :"+str(b)+"\nMonth :"+str(c)+'\nDate  :'+str(d)+'\nYear  :'+str(f)+'\nTime  :'+str(e)+"   OR   "+str(k)+":"+str(h)+":"+str(i)+j)

        greet20="time is %d"%k
        greet2=greet20+" "+str(h)+j                      # telling time

        voice(greet2)

        greet3=b+'day'+str(d)+"th"+" "+c+str(f)               # telling date and month

        voice(greet3)

#==========================================================================================


def main():
        st.markdown("<h4 style='text-align: center; color: green;'>Integrated Virtual Automated Machine System</h4>", unsafe_allow_html=True)
        asd=st.text_input("Enter your command").lower()
        qp(asd)
        
if __name__ == '__main__':
        main()
