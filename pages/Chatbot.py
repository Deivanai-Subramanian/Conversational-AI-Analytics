import pandas as pd 
import pyttsx3                  
import speech_recognition as sr 
import streamlit as st
from streamlit_chat import message as st_message

df = pd.read_csv('Dataset.csv')


if st.session_state['LOGGED_IN'] == True:
	repeater=1
	def speak(string):        
		engine = pyttsx3.init()
		engine.say(string)
		engine.runAndWait()
	def query():                    
		try:
			r = sr.Recognizer()
			with sr.Microphone() as source:
				audio=r.listen(source)    
				text=r.recognize_google(audio)
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
			return 1
		else:
			speak("Please Say The relevant word")
			search()
	st.title("CHATBOT")
	speak("hi,i am your assistant ")
	while(repeater==1):
		checker=search()
		if checker==1:
			repeater=0
	speak("It is my pleasure to help you,see you again, bye")
	
else:
	st.warning("Please Loggin")
