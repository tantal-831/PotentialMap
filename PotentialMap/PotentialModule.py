#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

import math

class PotentialMod:

	def __init__(self,weight = {'goal':5,'obst':1,'human':2},minimum_dist=5,speed=0.1):
		self.weight           = weight
		self.delt             = 0.01
		self.speed            = speed
		self.minimum_dist     = minimum_dist
		self.goal             = {}
		self.obst             = {}
		self.potential_max    = 1
		self.potential_min    = -1
		

	def run(self,Object_position):
			
		self.Object_position = Object_position
		for Object, position in self.Object_position.items():
			
			if Object =='goal':
				self.goal[Object] = position
			elif Object =='obst' or Object =='human':
				self.obst[Object] = position
			elif Object =='robot':
				x,y = position

		print("check4")
		vx,vy,obst_Object,goal_Object = self.cal_route(x, y)
		#vx = 0
		#vy = 1	
		return vx, vy

	def Pot(self,position,obst_target_position,goal_target_position,obst_Object,goal_Object):
		pot = 0
		b = 0.25
		x,y = position
		obst_target_x, obst_target_y ,trajectory_obst_target_x, trajectory_obst_target_y= obst_target_position
		goal_target_x, goal_target_y ,trajectory_goal_target_x, trajectory_goal_target_y= goal_target_position
		next_x=0
		next_y=0

		center_x=0
		center_y=0

		weight_obst = 1

		if obst_target_x == None or obst_target_y == None or obst_Object == '' : 
			obst_pot = 0

		elif obst_target_x == x and obst_target_y == y:
			obst_pot = self.potential_max

		elif obst_Object == 'obst':
			# weight_obst = self.weight[obst_Object]    
			weight_obst = self.weight['obst']
			if (math.sqrt(pow(obst_target_x-trajectory_obst_target_x,2)+pow(obst_target_y-trajectory_obst_target_y,2))/2)>b:
				center_x=obst_target_x+(obst_target_x-trajectory_obst_target_x)/2
				center_y=obst_target_y+(obst_target_y-trajectory_obst_target_y)/2

				#2点から長軸を算出
				a=math.sqrt(pow(b,2)+(pow((trajectory_obst_target_x-obst_target_x),2)+pow((trajectory_obst_target_y-obst_target_y),2)))
				
				#2点間の直線と水平軸との角度を算出
				theta=math.atan2((trajectory_obst_target_y-obst_target_y),(trajectory_obst_target_x-obst_target_x))

			   			#楕円ポテンシャル計算の各係数
			   	A=(pow(math.cos(theta),2)/pow(a,2))+(pow(math.sin(theta),2)/pow(b,2))
			   	B=2*math.cos(theta)*math.sin(theta)*((1/pow(a,2))-(1/pow(b,2)))
			   	C=(pow(math.sin(theta),2)/pow(a,2))+(pow(math.cos(theta),2)/pow(b,2))
			
				diff_x = x - center_x
				diff_y = y - center_y

			   	obst_pot=1/math.sqrt(A*pow(diff_x,2)+B*diff_x*diff_y+C*pow(diff_y,2))
			   	obst_pot *= weight_obst
			else:
			 	#移動していない時,点ポテンシャル
				diff_x = x - obst_target_x
		   		diff_y = y - obst_target_y
		   
				obst_pot =  1 / math.sqrt(pow(diff_x, 2) + pow(diff_y, 2))
			   	obst_pot *= weight_obst
		   
		
		elif obst_Object == 'human':
			#人回避
			weight_obst = self.weight[obst_Object]
			if (math.sqrt(pow(obst_target_x-trajectory_obst_target_x,2)+pow(obst_target_y-trajectory_obst_target_y,2))/2)>b:
				next_x = obst_target_x + (obst_target_x - trajectory_obst_target_x)*1000
				next_y = obst_target_y + (obst_target_y - trajectory_obst_target_y)*1000
				center_x = obst_target_x + (obst_target_x - trajectory_obst_target_x)*500
				center_y = obst_target_y + (obst_target_y - trajectory_obst_target_y)*500

				a = math.sqrt(b**2 + ((next_x - obst_target_x)**2 + (next_y - obst_target_y)**2))
				theta = math.atan((next_y - obst_target_y) / (next_x - obst_target_x))
				A = ((math.cos(theta))**2 / a**2) + ((math.sin(theta))**2 / b**2)
				B = 2 * math.cos(theta) * math.sin(theta) * ((1 / (a**2)) - (1 / (b**2)))
				C = ((math.sin(theta))**2 / (a**2)) + ((math.cos(theta))**2 / (b**2))
			
				diff_x = x - center_x
				diff_y = y - center_y
				
				print(weight_obst)
				obst_cal = A*(diff_x**2)+B*diff_x*diff_y+C*(diff_y**2)
				obst_pot = 1 / math.sqrt(obst_cal)
				obst_pot *= weight_obst

			else:
				print(weight_obst)
                #移動していない時,点ポテンシャル
				diff_x = x - obst_target_x
				diff_y = y - obst_target_y
            
				obst_pot =  1 / math.sqrt(pow(diff_x, 2) + pow(diff_y, 2))
                obst_pot *= weight_obst
                #print('point')
            

				#ゴール
		if goal_target_x == x and goal_target_y == y:
			goal_pot = self.potential_min
		else:
			weight_goal = self.weight[goal_Object]
			print(weight_goal)
			diff_x = x - goal_target_x
			diff_y = y - goal_target_y
			goal_pot = -1 / math.sqrt((diff_x**2) + (diff_y**2)) 
			goal_pot *= weight_goal
	
		pot = obst_pot + goal_pot

		return pot
			

	def cal_route(self, start_x, start_y):
			print("start_calculation")
			x = start_x
			y = start_y
			count = 0
			 
			count += 1
			# 対象となる障害物の座標を代入
			obst_target_position, obst_Object = self.target_check(x,y,'obstacle')
			goal_target_position, goal_Object = self.target_check(x,y,'goal')
			print("set_position")

			delt = self.delt
			# ポテンシャル場を偏微分して，xとy合成
			dx = self.Pot([x + delt, y       ], obst_target_position, goal_target_position, obst_Object, goal_Object)
			dy = self.Pot([x       , y + delt], obst_target_position, goal_target_position, obst_Object, goal_Object)
			xy = self.Pot([x       , y       ], obst_target_position, goal_target_position, obst_Object, goal_Object)
			vx = -(dx - xy) / self.delt
			vy = -(dy - xy) / self.delt
			
			v = math.sqrt(vx * vx + vy * vy)
			print(v)
			# 正規化
			vx /= v / self.speed
			vy /= v / self.speed
			
			# 進める
			x += vx
			y += vy
			
			if abs(vx) < 0.1 and abs(vy) < 0.1 and goal_Object !='goal' and abs(x-goal_target_position[0])<0.1 and abs(y-goal_target_position[1])<0.1:
				print('sub goal')
			
			print("vx = ")
			print(vx)
			print("vy = ")
			print(vy)

			return vx,vy,obst_Object,goal_Object

	def target_check(self, x, y, type):

		def calculate_theta(x, y, g_x, g_y):
			theta = math.atan2((g_y-y),(g_x-x))
			if theta<0: theta+=2*math.pi
			return theta
		target_list = []
		if type=="goal": target_list=self.goal
		if type=="obstacle": target_list=self.obst
			
		dist,tmp_dist = 0,9999
		target_x,target_y,trajectory_target_x,trajectory_target_y=0,0,0,0
		target_type = ''
		theta_goal, theta_sub_goal = 0,0
			
		#現在地との距離を計算して最も近いものを返す
		#閾値以上だったらNone
		for position_type, position_list in target_list.items():
			for position in position_list:
				if(position[0]==None or position[1]==None):
					pass
				else:
					print(position)
					dist      = math.sqrt((x - position[0])**2 + (y - position[1])**2 )
					if tmp_dist>dist:
						if type=='obstacle':
							tmp_dist = dist
							if dist <= self.minimum_dist: 
								target_x, target_y, trajectory_target_x, trajectory_target_y, target_type = position[0], position[1], position[2], position[3], position_type
							else: target_x, target_y, trajectory_target_x, trajectory_target_y ,target_type = None,None,None,None,None
						
						elif type == 'goal':
							if position_type =='goal': target_x, target_y, target_type ,trajectory_target_x, trajectory_target_y = position[0],position[1], position_type, None,None
							else:
								theta_goal = calculate_theta(x,y,self.goal['goal'][0][0],self.goal['goal'][0][1])
								theta_sub_goal = calculate_theta(x,y,position[0],position[1])
								if abs(theta_sub_goal - theta_goal)<=math.radians(45):
									target_x, target_y, target_type ,trajectory_target_x, trajectory_target_y = position[0],position[1], position_type,None,None
									tmp_dist = dist
			return [target_x, target_y,trajectory_target_x,trajectory_target_y], target_type
