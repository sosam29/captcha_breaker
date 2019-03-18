import requests
import os
import time
# /Users/samuelsonawane/Downloads/pyimageTutorial/captcha_breaker/download_images.py
url = "https://wwww.e-zpassny.com/vector/jcaptcha.do"

total= 0
for i in range (0, 10):
    try:
        r = requests.get(url, timeout=60)
        p = os.path.sep.join(downloads, "{}.jpg".format(str(total).zfill(5)))
        f = open(p, "wb")
        f.write(r.content)
        f.close
    except :
        print("Error in downloading the file")

time.sleep(0.1)
