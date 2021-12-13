#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

import math
import PotentialModule

class Pot_MapMod:

	def __Init__(self):
		self.pre_x = 0
		self.pre_y = 0
		self.area_pot = []
		self.Potential = PotentialModule.PotentialMod(weight = {'goal':5,'obst':1,'human':2})

	def mapmaker(self,x,y):
		etm_x = 1
		etm_y = 1
			
		check_x = round(x,1)
		check_y = round(y,1)
			##forループ
		if check_x != self.pre_x or check_y != self.pre_y:
				pre_x = check_x
				pre_y = check_y
				for pn in range(0,3):
					if pn == 0:
						etm_x = 1
						etm_y = 1
						pn += 1

					elif pn == 1:
						etm_x = -1
						etm_y = 1
						pn += 1

					elif pn == 2:
						etm_x = -1
						etm_y = -1
						pn += 1

					elif pn == 3:
						etm_x = 1
						etm_y = -1
						pn = 0

					for iIn in range(0,40):
						for jIn in range(0,40):
							i = iIn + (pre_x * 10) * etm_x
							j = jIn + (pre_y * 10) * etm_y
							obst_target_position, obst_Object = self.Potential.target_check(i,j,'obstacle')
							goal_target_position, goal_Object = self.Potential.target_check(i,j,'goal')
							self.area_pot[100 + jIn][100 + iIn] += self.Potential.Pot([i,j],obst_target_position,goal_target_position,'obst','goal')
							print('create_object_map')
		return self.area_pot
