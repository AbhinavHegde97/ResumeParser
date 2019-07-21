import pdftotext

class PdfToText:

	def __init__(self, filename):
		f = open(filename,"rb")
		self.pdf = pdftotext.PDF(f)
		f.close()
	def getTextContent(self):
		content = ("\n\n".join(self.pdf))
		content = content.strip()
		return content
