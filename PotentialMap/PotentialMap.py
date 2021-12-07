#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file PotentialMap.py
 @brief Elliptical_potential_method
 @date $Date$


"""
from __future__ import print_function
import json
import sys
import time
sys.path.append(".")
import math
import datetime
import PotentialModule
import numpy as np
import csv
# Import RTM module
import RTC
import OpenRTM_aist


# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
potentialmap_spec = ["implementation_id", "PotentialMap", 
		 "type_name",         "PotentialMap", 
		 "description",       "Elliptical_potential_method", 
		 "version",           "1.0.0", 
		 "vendor",            "TomokiTanikawa", 
		 "category",          "Navigation", 
		 "activity_type",     "STATIC", 
		 "max_instance",      "1", 
		 "language",          "Python", 
		 "lang_type",         "SCRIPT",
		 "conf.default.Goal_Place_x", "0.0",
		 "conf.default.Goal_Place_y", "0.0",
		 "conf.default.Map_making", "False",

		 "conf.__widget__.Goal_Place_x", "text",
		 "conf.__widget__.Goal_Place_y", "text",
		 "conf.__widget__.Map_making", "text",

         "conf.__type__.Goal_Place_x", "float",
         "conf.__type__.Goal_Place_y", "float",
         "conf.__type__.Map_making", "string",

		 ""]
# </rtc-template>

##
# @class PotentialMap
# @brief Elliptical_potential_method
# 
# 
class PotentialMap(OpenRTM_aist.DataFlowComponentBase):
	
	##
	# @brief constructor
	# @param manager Maneger Object
	# 
	def __init__(self, manager):
		OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

		Robot_place_arg = [None] * ((len(RTC._d_TimedPose2D) - 4) / 2)
		self._d_Robot_place = RTC.TimedPose2D(RTC.Time(0,0), RTC.Pose2D(RTC.Point2D(0.0,0.0), 0.0))
		"""
		"""
		self._Robot_DataIn = OpenRTM_aist.InPort("Robot_Data", self._d_Robot_place)
		Goal_area_arg = [None] * ((len(RTC._d_TimedPoint2D) - 4) / 2)
		self._d_Goal_area = RTC.TimedPoint2D(RTC.Time(0,0), RTC.Point2D(0.0,0.0))
		"""
		"""
		self._Goal_DataIn = OpenRTM_aist.InPort("Goal_Data", self._d_Goal_area)
		Object_Place_1_arg = [None] * ((len(RTC._d_TimedPoint2D) - 4) / 2)
		self._d_Object_Place_1 = RTC.TimedPoint2D(RTC.Time(0,0), RTC.Point2D(0.0,0.0))
		"""
		"""
		self._Place_Data_1In = OpenRTM_aist.InPort("Place_Data_1", self._d_Object_Place_1)
		Object_Place_2_arg = [None] * ((len(RTC._d_TimedPoint2D) - 4) / 2)
		self._d_Object_Place_2 = RTC.TimedPoint2D(RTC.Time(0,0), RTC.Point2D(0.0,0.0))
		"""
		"""
		self._Place_Data_2In = OpenRTM_aist.InPort("Place_Data_2", self._d_Object_Place_2)
		Human_Data_arg = [None] * ((len(RTC._d_TimedPoint2D) - 4) / 2)
		self._d_Human_Data = RTC.TimedPoint2D(RTC.Time(0,0), RTC.Point2D(0.0,0.0))
		"""
		"""
		self._Human_DataIn = OpenRTM_aist.InPort("Human_Data", self._d_Human_Data)
		Map_Data_arg = [None] * ((len(RTC._d_TimedPoint3D) - 4) / 2)
		self._d_Map_Data = RTC.TimedPoint3D(RTC.Time(0,0), RTC.Point3D(0.0,0.0,0.0))
		"""
		"""
		self._Map_DataOut = OpenRTM_aist.OutPort("Map_Data", self._d_Map_Data)
		R_move_arg = [None] * ((len(RTC._d_TimedVelocity2D) - 4) / 2)
		self._d_R_move = RTC.TimedVelocity2D(RTC.Time(0,0), RTC.Velocity2D(0.0,0.0,0.0))
		"""
		"""
		self._R_moveOut = OpenRTM_aist.OutPort("R_move", self._d_R_move)


		


		# initialize of configuration-data.
		# <rtc-template block="init_conf_param">
		"""
		
		 - Name:  Goal_Place_x
		 - DefaultValue: 0.0
		"""
		self._Goal_Place_x = [0.0]
		"""
		
		 - Name:  Goal_Place_y
		 - DefaultValue: 0.0
		"""
		self._Goal_Place_y = [0.0]
		"""
		
		 - Name:  Map_making
		 - DefaultValue: False
		"""
		self._Map_making = ['False']
		
		# </rtc-template>


		 
	##
	#
	# The initialize action (on CREATED->ALIVE transition)
	# formaer rtc_init_entry() 
	# 
	# @return RTC::ReturnCode_t
	# 
	#
	def onInitialize(self):
		# Bind variables and configuration variable
		self.bindParameter("Goal_Place_x", self._Goal_Place_x, "0.0")
		self.bindParameter("Goal_Place_y", self._Goal_Place_y, "0.0")
		self.bindParameter("Map_making", self._Map_making, "False")
		
		# Set InPort buffers
		self.addInPort("Robot_Data",self._Robot_DataIn)
		self.addInPort("Goal_Data",self._Goal_DataIn)
		self.addInPort("Place_Data_1",self._Place_Data_1In)
		self.addInPort("Place_Data_2",self._Place_Data_2In)
		self.addInPort("Human_Data",self._Human_DataIn)
		
		# Set OutPort buffers
		self.addOutPort("Map_Data",self._Map_DataOut)
		self.addOutPort("R_move",self._R_moveOut)
		
		# Set service provider to Ports
		
		# Set service consumers to Ports
		
		# Set CORBA Service Ports
		print("check1")
		return RTC.RTC_OK
	
	#	##
	#	# 
	#	# The finalize action (on ALIVE->END transition)
	#	# formaer rtc_exiting_entry()
	#	# 
	#	# @return RTC::ReturnCode_t
	#
	#	# 
	#def onFinalize(self):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The startup action when ExecutionContext startup
	#	# former rtc_starting_entry()
	#	# 
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onStartup(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The shutdown action when ExecutionContext stop
	#	# former rtc_stopping_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onShutdown(self, ec_id):
	#
	#	return RTC.RTC_OK
	
		##
		#
		# The activated action (Active state entry action)
		# former rtc_active_entry()
		#
		# @param ec_id target ExecutionContext Id
		# 
		# @return RTC::ReturnCode_t
		#
		#
	def onActivated(self, ec_id):
		print("Activated")
		self.Goal = [self._Goal_Place_x[0], self._Goal_Place_y[0]]
		self.x = 0
		self.pre_x = 0
		self.y = 0
		self.pre_y = 0
		self.heading = 0
		self.odometory_x = 0
		self.odometory_y = 0
		self.Potential = PotentialModule.PotentialMod(weight = {'goal':5,'obst':1,'human':2})
		self.Goal_flag = False
		self.object_flag = False
		self.human_flag = False
		if self._Map_making[0] == 'False':
			self.memory_flag = False
		else:
			self.memory_flag = True
		self.Previous_human_Data = [0.0,0.0]
		self.area_pot = [[]]
		print("check2")
		now =datetime.datetime.now()
		self.filename = 'C:\workspace\PotentialMap\logCSV\logdata' + now.strftime('%Y%m%d_%H%M%S')+'.csv'
		with open(self.filename,'w') as f:
			writer =csv.writer(f,lineterminator='\n')
		
		return RTC.RTC_OK
	
		##
		#
		# The deactivated action (Active state exit action)
		# former rtc_active_exit()
		#
		# @param ec_id target ExecutionContext Id
		#
		# @return RTC::ReturnCode_t
		#
		#
	def onDeactivated(self, ec_id):
	
		return RTC.RTC_OK
	
		##
		#
		# The execution action that is invoked periodically
		# former rtc_active_do()
		#
		# @param ec_id target ExecutionContext Id
		#
		# @return RTC::ReturnCode_t
		#
		#
	def onExecute(self, ec_id):
		print("start_Execute")
		goal = []
		Object = []
		human = []

		if self._Goal_DataIn.isNew():
			print("goal_check_start")
			self._d_Goal_area = self._Goal_DataIn.read()
			self.Goal_flag = False
			self.Goal[0] = self._d_Goal_area.data.x
			self.Goal[1] = self._d_Goal_area.data.y
			print(self.Goal)
			print("goal_check_finish")
			self.Goal_flag = False
		goal = [self.Goal]

		if self._Robot_DataIn.isNew():
			self.object_flag = True
			print("Ex_Robot_Place")
			self._d_Robot_place = self._Robot_DataIn.read()
			self.odometory_x = (-1.0) * self._d_Robot_place.data.position.y
			self.odometory_y = self._d_Robot_place.data.position.x
			self.x = (-1.0) * self._d_Robot_place.data.position.y
			self.y = self._d_Robot_place.data.position.x
			head = self._d_Robot_place.data.heading
			self.heading = math.atan2(math.sin(head),math.cos(head))
			print(self.x,self.y,self.heading)
			print("finish_Ex_Robot_place")
		
		if self.Goal_flag == False:
					
			if self._Place_Data_1In.isNew():
				self._d_Object_Place_1 = self._Place_Data_1In.read()
				if self._Place_Data_2In.isNew():
					self._d_Object_Place_2 = self._Place_Data_1In.read()
					print('Object_reading')			
			Object = [[self._d_Object_Place_1.data.x,self._d_Object_Place_1.data.y,self._d_Object_Place_2.data.x,self._d_Object_Place_2.data.y]]
			print(Object[0][0])
			print(Object[0][1])
			print(Object[0][2])
			print(Object[0][3])
			print('check_obst_place')

			if self._Human_DataIn.isNew():
				self.object_flag = True
				if self.human_flag == False:
					self._d_Human_Data = self._Human_DataIn.read()
					self.Previous_human_Data = [self._d_Human_Data.data.x, self._d_Human_Data.data.y]
					self.human_flag = True

				if self.human_flag == True:
					self._d_Human_Data = self._Human_DataIn.read()
					self.human_flag = False
				print('human_reading')
			human = [[self._d_Human_Data.data.x, self._d_Human_Data.data.y, self.Previous_human_Data[0], self.Previous_human_Data[1]]]
			print(self._d_Human_Data.data.x,',',human[0][0])
			print(self._d_Human_Data.data.y,',',human[0][1])
			print(self.Previous_human_Data[0],',',human[0][2])
			print(self.Previous_human_Data[1],',',human[0][3])
			print('check_human_place')
			position = {'goal':goal,'obst':Object,'human':human,'robot':[self.x,self.y]}


			vx,vy = self.Potential.run(position)
			sendvx = math.sqrt((vx**2)+(vy**2))
			sendva = math.atan2(-vx,vy)
			if (self.heading * sendva) < (math.radians(90) * math.radians(-90)):
				if self.heading > math.radians(90):
					self.heading -= math.radians(360)
				elif self.heading < math.radians(-90):
					self.heading += math.radians(360)
			sendva -= self.heading

			if sendvx>0.7:    sendvx = 0.7
			if sendva>0.7:    sendva = 0.7
			elif sendva<-0.7: sendva = -0.7

		#mapping全体的に見直し
		
			
			etm_x = 1
			etm_y = 1
			if self.memory_flag == True:
				check_x = round(self.x,1)
				check_y = round(self.y,1)
			##forループ
				if check_x != self.pre_x or check_y != self.pre_y:
					self.pre_x = check_x
					self.pre_y = check_y
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
								i = iIn + (self.pre_x * 10) * etm_x
								j = jIn + (self.pre_y * 10) * etm_y
								obst_target_position, obst_Object = self.Potential.target_check(i,j,'obstacle')
								goal_target_position, goal_Object = self.Potential.target_check(i,j,'goal')
								self.area_pot[100 + jIn][100 + iIn] += self.Potential.Pot([i,j],obst_target_position,goal_target_position,'obst','goal')
				
								self._d_Map_Data.data.x = i / 10
								self._d_Map_Data.data.y = j / 10
								self._d_Map_Data.data.z = self.area_pot[100 + jIn][100 + iIn]

								##マップ生成(forループ内に入れる)
								OpenRTM_aist.setTimestamp(self._d_Map_Data)
								self._Map_DataOut.write()
					print('create_object_map')
				self.object_flag = False
		
					

			self._d_R_move.data.vx = sendvx
			self._d_R_move.data.vy = 0
			self._d_R_move.data.va = sendva
			OpenRTM_aist.setTimestamp(self._d_R_move)
			self._R_moveOut.write()
			
			Goal_area_x = (self.x - goal[0][0])**2
			Goal_area_y = (self.y - goal[0][1])**2
			if(math.sqrt(Goal_area_x + Goal_area_y) < 0.04 or (abs(vx)<0.01 and abs(vy)<0.01)):
				print("")
				print("goal")
				print("")
				self._d_R_move.data.vx = 0
				self._d_R_move.data.vy = 0
				self._d_R_move.data.va = 0
				OpenRTM_aist.setTimestamp(self._d_R_move)
				self._R_moveOut.write()
				self.Goal_flag = True

		elif self.Goal_flag == True:
			self._d_R_move.data.vx = 0
			self._d_R_move.data.vy = 0
			self._d_R_move.data.va = 0
			OpenRTM_aist.setTimestamp(self._d_R_move)
			self._R_moveOut.write()

		return RTC.RTC_OK
	
	#	##
	#	#
	#	# The aborting action when main logic error occurred.
	#	# former rtc_aborting_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onAborting(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The error action in ERROR state
	#	# former rtc_error_do()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onError(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The reset action that is invoked resetting
	#	# This is same but different the former rtc_init_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onReset(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The state update action that is invoked after onExecute() action
	#	# no corresponding operation exists in OpenRTm-aist-0.2.0
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#

	#	#
	#def onStateUpdate(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The action that is invoked when execution context's rate is changed
	#	# no corresponding operation exists in OpenRTm-aist-0.2.0
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onRateChanged(self, ec_id):
	#
	#	return RTC.RTC_OK
	



def PotentialMapInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=potentialmap_spec)
    manager.registerFactory(profile,
                            PotentialMap,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    PotentialMapInit(manager)

    # Create a component
    comp = manager.createComponent("PotentialMap")

def main():
	mgr = OpenRTM_aist.Manager.init(sys.argv)
	mgr.setModuleInitProc(MyModuleInit)
	mgr.activateManager()
	mgr.runManager()

if __name__ == "__main__":
	main()

