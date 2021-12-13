#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-
import math

class PositionMaker:

	def __Init__(self):
		self.human_flag = False
		self.Goal = []

	def MakeGoal(self,Goal_x,Goal_y):
		print("goal_check_start")
		Goal = [Goal_x,Goal_y]
		print("goal_check_finish")
		return Goal

	def MakeHumanPosition(self,Human_x,Human_y):
		Human = []
		if self.human_flag == False:
			Human = [Human_x, Human_y, Human_x, Human_y]
			self.human_flag = True

		elif self.human_flag == True:
			Human[2] = Human[0]
			Human[3] = Human[1]
			Human[0] = Human_x
			Human[1] = Human_y
		
		print('human_reading')
		return Human