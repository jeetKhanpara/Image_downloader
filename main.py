from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import requests
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")

search_text = driver.find_element(By.XPATH,'//*[@id="APjFqb"]')
search_text.send_keys("kitchen")
search_text.send_keys(Keys.RETURN)

images_field = driver.find_element(By.XPATH,'//*[@id="hdtb-msb"]/div[1]/div/div[2]/a')
images_field.click()

for i in range(1,11):
    try:
        image_before_click = driver.find_element(By.XPATH,f'//*[@id="islrg"]/div[1]/div[{i}]/a[1]/div[1]/img')
        image_before_click.click()
        time.sleep(2)
        image_after_click = driver.find_element(By.XPATH,'//*[@id="Sva75c"]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img[1]')
        final_image_url = image_after_click.get_attribute('src')

        response = requests.get(final_image_url)

        
        if response.status_code == 200:
            
                with open(f"kitchen{i}.jpg",'wb') as file:
                    file.write(response.content)
                print(f"image {i} has been downloaded successfully")

    except:
        print(f"{i}th image could not be downloaded")

    

    # time.sleep(2)

# print(final_image_url)

