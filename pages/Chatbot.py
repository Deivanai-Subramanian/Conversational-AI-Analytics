import pandas as pd  
import pyttsx3                   #this model is to convert text to voice
import speech_recognition as sr  #this model is to recognize the voice
import streamlit as st
from streamlit_chat import message as st_message
from streamlit.components.v1 import html
df = pd.read_csv('Dataset.csv')
repeater=1

def open_page(url):
    open_script= """
        <script type="text/javascript">
            window.open('%s', '_blank').focus();
        </script>
    """ % (url)
    html(open_script)
def speak(string):              #function to convert text to voice using pyttsx3 module
    engine = pyttsx3.init()
    engine.say(string)
    engine.runAndWait()
def query():                     #function to recognize the user voice using speech_recognition
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio=r.listen(source)    
            text=r.recognize_google(audio)
            st.write(text)
        return (text)
    except:
        speak("the word is not clear,tell again")
        st.write("Tell Again ")
        text=query()
        return(text)
def search(): #function to search for the word in wikipedia
    speak("tell about the word to search")
    st.write("tell about the word to search")
    text=query()
    if text == "stop" or text == "thank you":
        st_message(text,is_user=True)
        st_message("Bye")
        return 1
    elif text == "product" or text == "i need to purchase " or text == "I need to purchase" or text =="Product":
        st_message(text,is_user=True)
        speak("Tell the Main  category from the list ")
        st_message('The Main Categories are Accesories,Appliances,Sports and Fitness,Home and Appliances')

    elif text== "Accessories" or text== "accessories":
        Main_category = text
        df_main_category = df.query("main_category == @Main_category")
        speak("Select the Sub Category")        
        Sub_category = st.multiselect(
        "Select the Sub-Category:",
        options=df_main_category["sub_category"].unique(),
        default=df_main_category["sub_category"].unique()
        )
        st.button("To View Products", key=None, help="Click Me", on_click=open_page,args=('https://www.amazon.in/s?k=Accesories&crid=1FE3OPUIS6436&sprefix=accesories%2Caps%2C332&ref=nb_sb_noss_2',))
        return 1  
     
    elif text=="appliances" or text=="Appliances":
        Main_category = text
        df_main_category = df.query("main_category == @Main_category")
        speak("Select the Sub Category")        
        Sub_category = st.multiselect(
        "Select the Sub-Category:",
        options=df_main_category["sub_category"].unique(),
        default=df_main_category["sub_category"].unique()
        )
        st.button("To View Products", key=None, help="Click Me", on_click=open_page, args=('https://www.amazon.in/s?k=Appliances&crid=27PRYAVKELEE6&sprefix=appliances%2Caps%2C404&ref=nb_sb_noss_1',))
        return 1   
    
    elif text== "home and appliances" or text=="Home and appliances":
        Main_category = text
        df_main_category = df.query("main_category == @Main_category")
        speak("Select the Sub Category")        
        Sub_category = st.multiselect(
        "Select the Sub-Category:",
        options=df_main_category["sub_category"].unique(),
        default=df_main_category["sub_category"].unique()
        )
        st.button("To View Products", key=None, help="Click Me", on_click=open_page, args=('https://www.amazon.in/s?k=Home+and+Appliances&crid=2LH056XN7AM1V&sprefix=home+and+appliances%2Caps%2C300&ref=nb_sb_noss_1',))
        return 1
    
    elif text == "sports and fitness" or text == "Sports and fitness" or text == "sport and fitness":
        Main_category = text
        df_main_category = df.query("main_category == @Main_category")
        speak("Select the Sub Category")        
        Sub_category = st.multiselect(
        "Select the Sub-Category:",
        options=df_main_category["sub_category"].unique(),
        default=df_main_category["sub_category"].unique()
        )
        st.button("To View Products", key=None, help="Click Me", on_click=open_page, args=('https://www.amazon.in/s?k=Sports+and+Fitness&crid=341IKVU9SS2YS&sprefix=sports+and+fitness%2Caps%2C320&ref=nb_sb_noss_1',))
        return 1
    
    else:
        speak("Please Say The relevant word")
        search()
st.title("CHATBOT")
if st.session_state['LOGGED_IN'] == True:
    speak("hi,i am your assistant ")
    while(repeater==1):
        checker=search()
        if checker==1:
            repeater=0
    speak("It is my pleasure to help you,see you again, bye")
else:
	st.warning("Please Loggin")
