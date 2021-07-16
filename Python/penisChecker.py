import math


class penisChecker(object):

	def __init__(self):
		pass


	def lenDev(self, length, erec=False):
		return math.floor(((length - (13.12 if erec else 9.14)) / (1.66 if erec else 1.57)*10 + 50)*10) / 10


	def thickDev(self, thick, erec=False):
		return math.floor(((thick - (11.66 if erec else 9.31)) / (1.1 if erec else 0.9)*10 + 50)*10) / 10


	def makeRank(self, a, b, c):
		e = (c - a) / math.sqrt(2*b*b)
		f = 1 / (1 + 0.3275911*abs(e))
		g = 0.254829592
		h = -0.284496736
		i = 1.421413741
		j = -1.453152027
		k = 1.061405429
		l = 1 - (((((k*f + j)*f) + i)*f + h)*f + g)*f*math.exp(-e*e)
		m = -1 if e < 0 else 1
		return math.floor(((1 / 2)*(1 + m*l))*100)


	def lenRank(self, length, erec=False):
		n = self.makeRank((13.12 if erec else 9.14), (1.66 if erec else 1.57), length);
		rank = n if n < 50 else 100 - n
		if rank == 0:
			rank = 1
		ret = ("上位" if n >= 50 else "下位") + str(rank) + "%"
		if rank == 1:
			ret = ret + ("以上" if n >= 50 else "以下")
		return ret


	def thickRank(self, length, erec=False):
		n = self.makeRank((11.66 if erec else 9.31), (1.1 if erec else 0.9), length);
		rank = n if n < 50 else 100 - n
		if rank == 0:
			rank = 1
		ret = ("上位" if n >= 50 else "下位") + str(rank) + "%"
		if rank == 1:
			ret = ret + ("以上" if n >= 50 else "以下")
		return ret


	def comment(self, len=0, thick=0, erec=False):
		lenDev, thickDev = self.lenDev(len, erec), self.thickDev(thick, erec)
		lengthTxt = ""
		thickTxt = ""
		if thickDev:
			if thickDev < 25:
				thickTxt = "細めで、" if lenDev else "細め"
			else:
				if (thickDev >= 25) and (thickDev < 50):
					thickTxt = "やや細めで、" if lenDev else "やや細目"
				else:
					if (thickDev >= 50) and (thickDev < 60):
						thickTxt = "やや太くて、" if lenDev else "やや太い"
					else:
						if (thickDev >= 60) and (thickDev < 70):
							thickTxt = "太くて、" if lenDev else "太い"
						else:
							if thickDev >= 70:
								thickTxt = "極太で、" if lenDev else "極太"
		if lenDev:
			if lenDev < 25:
				lengthTxt = "短い"
			else:
				if (lenDev >= 25) and (lenDev < 50):
					lengthTxt = "やや短い"
				else:
					if (lenDev >= 50) and (lenDev < 60):
						lengthTxt = "やや長い"
					else:
						if (lenDev >= 60) and (lenDev < 70):
							lengthTxt = "長い"
						else:
							if lenDev >= 70:
								lengthTxt = "とても長い"
		return thickTxt + lengthTxt


# The original code (JavaScript) was developed by https://penis-checker.com
# Ported to Python by Hidegon
# If you use this, be sure to read this original (https://penis-checker.com/?page_id=16) note.
# If you have any problems, please contact me. We will remove it at any time.
