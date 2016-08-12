
import io
import urllib.request
import PIL.Image
import aalib
import time
from halibot import HalModule, Message

class AA(HalModule):

	def init(self):
		pass

	def receive(self, msg):
		if msg.body.startswith('!aa '):

			# Setup the screen
			w = self.config.get('width', 40)
			h = self.config.get('height', 20)
			scr = aalib.AsciiScreen(width=w, height=h)

			# Get the image
			url = msg.body[len('!aa '):]
			fp = io.BytesIO(urllib.request.urlopen(url).read())
			image = PIL.Image.open(fp).convert('L').resize(scr.virtual_size)

			# Draw the image and reply
			scr.put_image((0, 0), image)

			for ln in scr.render().split('\n'):
				time.sleep(self.config.get('sleep', 0))
				self.reply(msg, body=ln)

