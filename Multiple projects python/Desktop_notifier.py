from plyer import notification
import time


if __name__ == '__main__':
    while True:
        notification.notify(
            title = "Time for break",
            message = "Take a break",
            app_icon = "calendar_clock_schedule_icon-icons.com_51085.ico",
            timeout = 5
        )
        time.sleep(3600) # 1 hour repeat, you can change
        

# pythonw file.py for background run        