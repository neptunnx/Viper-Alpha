import random
import string
import requests


def gencode():
	letters = string.ascii_letters + string.digits
	return ''.join(random.choice(letters) for i in range(19))


class NitroGenerator:
	def __init__(self):
		self.codes = []
		self.check()
	
	def check(self):
		while True:
			code = gencode()
			self.codes.append(code)
			response = requests.get(
				"https://discord.com/api/v7/entitlements/gift-codes/" + code + "?with_application=false&with_subscription_plan=true")
			data = response.json()
			if data["message"] == 'Unknown Gift Code':
				print("Not Working: " +"https://discord.gift/"+ code)
			else:
				print("Possibly Working: " +"https://discord.gift/"+ code)
				file = open("workedcodes.txt", "a+")
				file.write("\n" +"https://discord.gift/"+ code)


NitroGenerator()
