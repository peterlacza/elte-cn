""" Host class
"""

import threading
import logging


class Host(threading.Thread):
	""" Server

	Arguments:
		threading {Thread} -- runnable
	"""

	def __init__(self, config):
		""" Constructor

		Arguments:
			config {dict} -- host, port
		"""

		threading.Thread.__init__(self)
		print config["id"]
		self.logger = logging.getLogger(self.__class__.__name__ + "_" + config["id"])
		self.logger.info("Initializing %s", self.__class__.__name__)
		self.config = config
		self.server_addr = (config["host"], config["port"])
		self.running = True
