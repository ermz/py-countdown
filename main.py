from datetime import datetime

task_date = input("Format as follow EAT BREAKFEST:02.05.2021 \n")
task_date_list = task_date.split(":")

goal = task_date_list[0]
finish_date = task_date_list[1]
deadline = datetime.strptime(finish_date, "%d.%m.%Y")
# print(type(datetime.strptime(finish_date, "%d.%m.%Y")))
current_day = datetime.today()

time_left = deadline - current_day
hours_till = int(time_left.total_seconds() / 60 / 60)
print(f"Hey user you currently have {hours_till} hours left to -- {goal} --")
