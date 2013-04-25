from django.db import models

# from brabeion import badges
# from brabeion.base import Badge, BadgeAwarded


class Account(models.Model):
	"""docstring for Account"""
	currency = models.CharField(max_length=3)

class Budget(models.Model):
	"""docstring for Budget"""
	budget_title = models.CharField(max_length=30)
	amount_budget = models.IntegerField()
#	account = models.OneToOneField(Account)

class Expenses(models.Model):
	"""docstring for Expenses"""
	expense_title = models.CharField(max_length=30)
	expense_amount = models.IntegerField()
	expense_timestamp = models.DateField()

class Saving(models.Model):
	"""docstring for Savings"""
	saving_title = models.CharField(max_length=30)
	saving_amount = models.IntegerField()
		
# class PointsBadge(Badge):
# 	"""docstring for PointsBadge"""

# 	slug = "points"
# 	levels = [
# 		"Bronze",
# 		"Silver",
# 		"Gold",
# 	]
# 	events = [
# 		"points_awarded"
# 	]
# 	multiple = False

# 	def award(self, **state):
# 		user = state["user"]
# 		points = user.get_profile().points;
# 		if points > 10000;
# 			return BadgeAwarded(level=3)
# 		elif points > 7500;
# 			return BadgeAwarded(level=2)
# 		elif points > 5000;
# 			return BadgeAwarded(level=1)

# badges.register(PointsBadge)

