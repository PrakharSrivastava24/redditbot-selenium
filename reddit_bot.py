from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import getpass
from google import genai


#Fetch Information
username = input("Enter your user name : ")
password = getpass.getpass("Enter your password(not visible) : ")
apikey = getpass.getpass("Enter your api key(not visible) : ")

#Sample dictionary for example
dictionary = {"AskIndia":"What are your views about technology advancement in India","Btechtards":"What should you do in final year ?","AskIndianMen":"What challenges you face as a Indian man ?","Fitness_India":"What should be the daily diet to be a healthy person"}

# Using Google's Gemini model for text generation 
client = genai.Client(api_key=apikey)


#Used delays of 2 or 3 seconds can be adjusted according to need
driver = webdriver.Chrome()
driver.get("https://www.reddit.com/")
time.sleep(2)
login=driver.find_element(By.XPATH,"//span[contains(text(), 'Log In')]")
login.click()
time.sleep(3)
inputfield = driver.find_element(By.NAME,"username")
inputfield.send_keys(username)
passfield = driver.find_element(By.NAME,"password")
passfield.send_keys(password)
loginbutton = driver.find_element(By.XPATH,"//*[@id='login']/auth-flow-modal/div[2]/faceplate-tracker/button")
loginbutton.click()
time.sleep(3)



def automate(redditsub,prompt):
    response1 = client.models.generate_content(
    model="gemini-1.5-flash",
    contents="Assume yourselve as curious person and write using I as if you're a human on topic :"+prompt
    )
    driver.refresh()
    driver.get(f"https://www.reddit.com/r/{redditsub}/submit/?type=TEXT")
    time.sleep(3)
    titletarea = driver.find_element(By.NAME, "title")
    titletarea.send_keys(prompt)
    bodyarea = driver.find_element(By.NAME,"body")
    bodyarea.send_keys(response1.text)
    time.sleep(2)
    addflair = driver.execute_script("""document.querySelector("#post-flair-modal").shadowRoot.querySelector("#reddit-post-flair-button").click();""")
    time.sleep(3)
    flairtype = driver.execute_script("""document.querySelector("#post-flair-modal").shadowRoot.querySelector("#post-flair-radio-input-0").shadowRoot.querySelector("label").click();""")
    time.sleep(3)
    applyflair = driver.execute_script("""let button = document.querySelector("#post-flair-modal").shadowRoot.querySelector("#post-flair-modal-apply-button");
    if (button) {
    button.focus();  // Focus on the button
    button.click();  // Click after focusing
    }""")
    time.sleep(3)
    postbutton = driver.execute_script("""document.querySelector("#submit-post-button").shadowRoot.querySelector("#inner-post-submit-button").click();""")

for redditsub,prompt in dictionary.items():
    automate(redditsub,prompt)
    
input("pause")