from celery import  shared_task
import time



@shared_task
def send_emails():
    for x in range(10):
        time.sleep(5)
        #send email
        print(f'Sending email number {x}')