import os
from crontab import CronTab

username = os.environ.get("LOGNAME")
path = os.environ.get("path_fetch")

my_cron = CronTab(user=username)
job = my_cron.new(command=path)
job.minute.every(5)
 
my_cron.write()