from django.db import models
import datetime

class Brexit(models.Model):
	def get_time_diff(self):
		a = datetime.datetime.now()
		b = datetime.datetime(2019,3,29,12,0,0)
		return b-a		