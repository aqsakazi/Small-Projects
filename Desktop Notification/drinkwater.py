import time
from plyer import notification

if __name__ == "__main__":
    while True:
         notification.notify(
             title = "Please drink water",
             message = "Water is a natural appetite suppressant and, if consumed before a meal, can reduce your overall calorie intake. It's also the original zero-calorie diet drink.",
             app_icon = "F:\Desktop Notification\icon.ico",
             timeout=5  
        )
        time.sleep(60*60)
