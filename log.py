#log.py

'''
It's a class provides a storer directory of logs.
'''

#Imports
import logging
import os
from datetime import datetime
from pywinauto import actionlogger


class Log:

	#Method of opening log.
	def open():
		try:
			#Creating directory if it don't exist.
			os.mkdir('.\Log')
		except:
			pass

		#Setting up file log. 	
		file = 'Log\\' + datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.log'
		logging.basicConfig(
		    level=logging.NOTSET,
		    format="%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s",
		    handlers=[
		        logging.FileHandler(file),
		        logging.StreamHandler()
		    ])
		#Starting a traceback registry for pywinauto
		actionlogger.enable()


	#Method of standard input into the log
	def input(string):
		value = input(string)
		logging.info(string + value)
		return value

	#Method of standard output into the log
	def print(string):
		logging.info(string)
		print(string)

	#Method of closing log.
	def close():
		actionlogger.disable()


