from crontab import CronTab

my_cron = CronTab(user='krish')

my_cron.remove_all()

job = my_cron.new(command="python3 ~/wealth42/fetch_data.py")

job.minute.every(5)

my_cron.write()

