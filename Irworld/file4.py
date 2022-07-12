''' This file creates data.py file '''



from Url import urls
from file3 import get_data
import time


for i in range(100, 112):

    value = get_data(urls[i][0], urls[i][2], urls[i][3])

    with open('data.py', 'a') as writer:
        writer.write(str(value))
        writer.write(",")
        writer.write("\n")
        writer.close()
    
    time.sleep(3)
  

