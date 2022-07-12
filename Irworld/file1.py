''' This file collects all urls and image links from the landing page and a creates a file containing all links and images'''



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



def get_data(link):

    driver = webdriver.Firefox()
    driver.get(link) # driver opens the link

    time.sleep(2)
    try: # wait for the link to open completelly
        WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "page"))
                                        )
    except:
        print("The page is not loaded!")


    #scroll to page end with JavaScript Executor
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    scroll_pause_time = 1 # You can set your own pause time. My laptop is a bit slow so I use 1 sec
    screen_height = driver.execute_script("return window.screen.height;")   # get the screen height of the web
    i = 1

    while True:
        # scroll one screen height each time
        driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
        i += 1
        time.sleep(scroll_pause_time)
        # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
        scroll_height = driver.execute_script("return document.body.scrollHeight;")
        # Break the loop when the height we need to scroll to is larger than the total scroll height
        if (screen_height) * i > scroll_height:
            break


    DATA = []
    products = (WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "product-element"))))
    
    print(len(products))

    DATA = []

    for p in products:
        data = []
        link = p.find_element(By.TAG_NAME, "a").get_attribute("href")
        data.append(link)
        # print(link)
        image = p.find_element(By.TAG_NAME, "img").get_attribute("src")
        data.append(image)
        # print(image)
        
        Text = p.find_element(By.CLASS_NAME, "content").text
        if len(Text.split('\n'))==3:
            name, price, price_per_litr = Text.split('\n')
        else:
            name, price = Text.split('\n')
            price_per_litr = '---'

        # print(name)
        # print(price)
        # print(price_per_litr)
        data.append(name)
        data.append(price_per_litr)
       
        
        if len(price.split('€'))>2:
            price = str(price.split('€')[0]) + '€'

            price_after_discount = str(price.split('€')[1]) + '€'

        else:
            price = str(price.split('€')[0]) + '€'
            price_after_discount = '---'

        data.append(price)
        data.append(price_after_discount)
        
        DATA.append(data)

    # print("Name = ", Name)
    # print("Price = ", Price)
    # print("Price_After_Discount = ", Price_After_Discount)
    # print("price_per_litr = ", price_per_litr)

    

    print(len(DATA))
    with open('Url.py','a') as writer:
        writer.write("urls = ")
        writer.write(str(DATA))
        writer.write("\n")
        writer.close()

    print(DATA)

    driver.quit()



if __name__ == '__main__':
    link = "https://shop.lrworld.com/cms/GR/en/care/care.html?casrnc=44dde"
    get_data(link)






