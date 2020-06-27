import os 
from crontab import CronTab

username = os.environ.get("LOGNAME")

cron = CronTab(user = username)
job = cron.new(command="path/to/file/get_data.py")
job.minute.every(5)

cron.write()