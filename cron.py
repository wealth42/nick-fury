from crontab import CronTab

my_cron = CronTab(user='yourusername')
job = my_cron.new(command='python3 /path/to/nick-fury/fetch.py')
job.minute.every(5)
 
my_cron.write()