import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys


class WhatsAppBot:

    def user_chat(self, names, text):

        name_list = []


        for i in names:
            try:
                driver.refresh()
                time.sleep(5)
                chat_new = driver.find_element(By.CSS_SELECTOR, ".selectable-text.copyable-text.iq0m558w.g0rxnol2")
                chat_new.click()
                time.sleep(2)
                chat_new.send_keys(i)
                time.sleep(2)
                chat_new.send_keys(Keys.ENTER)
                time.sleep(2)
                message = driver.find_element(By.CSS_SELECTOR,
                                              "div[title='Type a message'] p[class='selectable-text copyable-text iq0m558w g0rxnol2']")
                message.click()
                time.sleep(2)
                message.send_keys(f"Hello {i}, {text}")
                time.sleep(2)
                message.send_keys(Keys.ENTER)
                time.sleep(2)


            except:
                print(f"There is no such name as {i}, in your contact list!")
                name_list.append(i)
                continue


        a = len(name_list)
        if a == 0:
            print("All messages were send successfully!")
        else:
            driver.execute_script(f"alert('{a} person were not in you contact list!')")
            time.sleep(5)


if __name__ == "__main__":
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://web.whatsapp.com/")
    driver.execute_script("alert('You have 15 seconds to log in to your WhatsApp Web')")
    time.sleep(15)

    whats_app_bot = WhatsAppBot()
    num_of_people = int(input("How many person you want to send the message? "))
    name = []
    for i in range(num_of_people):
        name.append(input(f"Enter the name of person [{i}]: "))

    message = input("Enter your Message: ")
    whats_app_bot.user_chat(name, message)
