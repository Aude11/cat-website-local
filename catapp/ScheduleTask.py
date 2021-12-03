import time
import schedule


# initial idea was to have the app adding automatically every saturday a cat image
class ScheduleTask:
    def __init__(self, task):
        self.task = task

    def schedule_minutes(self, every_x_times):
        schedule.every(every_x_times).minutes.do(self.task)
        self._run_scheduled_task()

    def schedule_sunday_task(self, every_x_times, starting_time):
        schedule.every().sunday.at(starting_time).do(self.task)
        self._run_scheduled_task()

    def schedule_saturday_task(self, every_x_times, starting_time):
        schedule.every().saturday.at(starting_time).do(self.task)
        self._run_scheduled_task()

    def _run_scheduled_task(self):
        while True:
            schedule.run_pending()
            time.sleep(1)
