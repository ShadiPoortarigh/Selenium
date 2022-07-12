''' This file collects the data inside each url '''


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time






def get_data(link, name, price_per_litr):

    driver = webdriver.Firefox()
    driver.get(link) # driver opens the permalink

    time.sleep(2)

    try: # wait for the link to open completelly
        WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "page"))
                                        )
    except:
        print("The page is not loaded!")


   
    scroll_pause_time = 1
    screen_height = driver.execute_script("return window.screen.height;")  
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


    data = []
    data.append(link)
    data.append(name)
    data.append(price_per_litr)


    a = driver.find_element(By.CLASS_NAME, "product-description-name").text
    if len(a.split('\n')) == 3:
        volume = a.split('\n')[2]
    else:
        volume = '---'
    print(volume)

    data.append(volume)


    b = driver.find_element(By.CLASS_NAME, "image")
    image = b.find_element(By.TAG_NAME, "img").get_attribute("src")
    data.append(image)
    description = driver.find_element(By.CLASS_NAME, "elements-wrapper").text
    data.append(description.replace('\n', '.'))
    net = driver.find_element(By.CLASS_NAME, "product-price").text
    
    # print(image)
    # print('\n')
    # print(description)
    # print('\n')

    
    
    
    
    
    
    # print(net.split('€'))
    # print(net.split('\n'))


  
    
    if len(net.split('€')) == 4:
        splited = (net.split('\n'))
        
        price = splited[0]
        # print("price =", price)
        data.append(price)
        price_after_discount = splited[1]
        # print("price_after_discount = ", price_after_discount)
        data.append(price_after_discount)
        
        for i in splited:
            if 'get' in i:
                discount = i
                
                # print("discount = ", discount)
        if discount:
            data.append(discount)
        else:
            data.append('---')

                
           
        for i in splited:
            if 'net' in i:
                net_price = i
                # print("net_price = ", net_price)
        if net_price:
            data.append(net_price)
        else:
            data.append('---')
             # print("net_price = ", net_price)
    
    else:
        splited = (net.split('\n'))
        price = splited[0]
        # print("price =", price)
        data.append(price)
        price_after_discount = '---'
        # print("price_after_discount = ", price_after_discount)
        data.append(price_after_discount)
        
        for i in splited:
            if 'get' in i:
                discount = i
                
                # print("discount = ", discount)
        if discount:
            data.append(discount)
        else:
            data.append('---')

                
           
        for i in splited:
            if 'net' in i:
                net_price = i
                # print("net_price = ", net_price)
        if net_price:
            data.append(net_price)
        else:
            data.append('---')
             # print("net_price = ", net_price)

    print(data)
    driver.quit()

    return data



if __name__ == '__main__':
    link = 'https://shop.lrworld.com/product/gr/en/aloe_vera_nutri-repair_hair_set.html?productAlias=20763-1'
    name =  'Aloe Vera Nutri-Repair Hair Set'
    price_per_litr = '147.95 € per 1 l'
    get_data(link, name, price_per_litr)