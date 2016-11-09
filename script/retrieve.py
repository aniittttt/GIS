#!/bin/python

import shapefile

class Retrieve(object):
	def __init__(self,namafile):
		self.sf = shapefile.Reader(namafile)
	def itungBaris(self):
		rec = self.sf.shapes()
		return len(rec)
	def selectProvinsi(self,PROVINSI):
		i = 0
		for a in self.sf.records():
			if a[8] == PROVINSI:
				return i
			i = i+1