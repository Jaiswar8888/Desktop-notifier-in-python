from email import message
import time 
from plyer import notification 

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Please take a short break",
            message = "Its good to take short breaks after 25 minutes of work (as per the Pomodoro Technique)",
            
            
        )
        time.sleep(3)

