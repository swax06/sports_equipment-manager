from django.apps import AppConfig
from apscheduler.schedulers.background import BackgroundScheduler
import sportsEquipment.updater as updater

class SportsEquipmentConfig(AppConfig):
	name = 'sportsEquipment'
	def ready(self):
		scheduler = BackgroundScheduler()
		scheduler.add_job(updater.update_penalty, 'interval', seconds=5)
		scheduler.start() 



