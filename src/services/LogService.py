from datetime import datetime 

def wrt_screen(msg):
    date_time = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    print(f"[{date_time}] => {msg}")