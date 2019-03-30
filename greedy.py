# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 17:32:09 2019
@author: ASUS
"""
import heapq
def Greedy(map, start, goal):
	visited = set()	#mark visited city
	parent = {}		#mark the source to reach a city
	gn = {start : 0}	

	pq = []#list pq

	heapq.heappush(pq, (gn[start], start)) #enter to priorityqueue
	cnt = 1 #intialitation for order of step
	while pq:
		current = heapq.heappop(pq)[1] #push city to priorityque
		print()
		print('----------Step {}----------'.format(cnt))
		cnt+=1
		print('Now at {}'.format(current)) #print current city

		if current == goal: #ketika lokasi = tujuan langsung print Reach Goal
			print('Reach GOAL')
			print()
			path = []#Menyimpan Jalur fix
			while current in parent: 
				path.append(current)#mengepush current ke path
				current = parent[current]
			return path[::-1]	#reversed

		visited.add(current)	#mark current city as visited
		for c_name in map[current]:	#iterate to all neighbor
			if c_name in visited:			#city had been visited before
				continue
            
			gn_temp =  map[current][c_name]
			print('Sekarang Cek at {:5}\tg(n) = {} Kilo\t'.format(c_name, gn_temp))
			if c_name in gn and gn_temp < gn[c_name] or c_name not in gn:	# ketika f(n) lebih kecil dari f(n) yng 
                                                                        #pernaah di savenew  
                                                                        #atau kota yang belum pernah
				if c_name not in gn:											#expand to newly discovered city
					heapq.heappush(pq, (gn_temp, c_name)) #when push ti priorytyque
					print('Masukkan {} Ke Priorty Queue'.format(c_name))
				parent[c_name] = current #set source to reach city
				gn[c_name] = gn_temp		#update or set g(n)

	return None
