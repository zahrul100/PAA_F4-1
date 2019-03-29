# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 17:31:49 2019

@author: ASUS
"""

def daftarkota(cityname):
	citylist = []
	count = 0
	for i in cityname:
		citylist.append(i)
		count+=1
		if count%4 == 0:
			citylist.append('\n')

	citylist = ' '.join(citylist)
	print(citylist)