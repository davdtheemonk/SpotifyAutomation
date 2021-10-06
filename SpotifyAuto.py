#Program to automate Your web spotify from login page to limitless bounds


from selenium import webdriver
from time import sleep

browser = webdriver.Firefox(executable_path=r"C:\Users\user\Desktop\code!code!code!\Instagrambot\geckodriver")
browser.implicitly_wait(5)

class Home():
    def __init__(self,browser):
        self.browser = browser
        self.browser.get("https://www.spotify.com/us")
        sleep(5)


    def login_page(self):
        self.browser.get("https://accounts.spotify.com/login/?continue=https%3A%2F%2Fopen.spotify.com%2F%3Fl2l%3D1")
        sleep(5)
        return Login_Spotify(self.browser)


class Login_Spotify():
    def __init__(self,browser):
        self.browser = browser
    def details(self,email,password):
        user_email =  self.browser.find_element_by_id("login-username")
        user_psswd = self.browser.find_element_by_id("login-password")
        user_email.send_keys(email)
        user_psswd.send_keys(password)
        login = browser.find_element_by_id("login-button")
        login.click()
        sleep(30)
        dismiss = browser.find_elements_by_css_selector("button.Button-sc-1dqy6lx-0.gBHmLl.EgJUUJEjjlqltHsVq2eG._BD_QhoLIEwN43cc9lXh")
        dismiss.click()
        sleep(5)
        return Player(self.browser)

class Player():
    def __init__(self,browser):
        self.browser = browser


    def player(self,artist):
        play_button = browser.find_element_by_css_selector("button.jn05jgnCWyQjLZKqyKFa._LL_A9TkcmSEuHntj_bw")
        play_button.click()
        sleep(5)
        search_button = browser.find_element_by_xpath("//a[@href='/search'")
        search_button.click()
        sleep(5)
        search_input = browser.find_element_by_xpath("//form[@role=search")
        search_input.send_keys(artist)
        return "\n"
        







        
def autologin(browser):
    page1 = Home(browser)
    log_in = page1.login_page()
    #Enter your email and password here for you to login to your account
    log_in.details("youremail","yourpassword").player("Artist")
    

autologin(browser)


    















    

