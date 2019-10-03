import time
from datetime import datetime as dt

host_temp = "hosts"

redirect = "any ip"

website_list = ["www.facebook.com", "www.youtube.com","any other url to block"]


while True:

    if dt(dt.now().year, dt.now().month, dt.now().day, 19) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 22):
        print("Working Hours")

        with open(host_temp, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website+"\n")
    else:
        with open(host_temp, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()

        print("Fun Hours")
    time.sleep(5)
