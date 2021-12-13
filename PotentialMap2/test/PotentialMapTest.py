#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file PotentialMapTest.py
 @brief ModuleDescription
 @date $Date$


"""
import sys
import time
sys.path.append(".")

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
potentialmaptest_spec = ["implementation_id", "PotentialMapTest",
		 "type_name",         "PotentialMapTest",
		 "description",       "ModuleDescription",
		 "version",           "1.0.0",
		 "vendor",            "TomokiTanikawa",
		 "category",          "Navigation",
		 "activity_type",     "STATIC",
		 "max_instance",      "1",
		 "language",          "Python",
		 "lang_type",         "SCRIPT",
		 "conf.default.Potential_Gain", "1",
		 "conf.default.Goal_Place_x", "0.0",
		 "conf.default.Goal_Place_y", "0.0",

		 "conf.__widget__.Potential_Gain", "text",
		 "conf.__widget__.Goal_Place_x", "text",
		 "conf.__widget__.Goal_Place_y", "text",

         "conf.__type__.Potential_Gain", "float",
         "conf.__type__.Goal_Place_x", "float",
         "conf.__type__.Goal_Place_y", "float",

		 ""]
# </rtc-template>

##
# @class PotentialMapTest
# @brief ModuleDescription
#
#
class PotentialMapTest(OpenRTM_aist.DataFlowComponentBase):

	##
	# @brief constructor
	# @param manager Maneger Object
	#
	def __init__(self, manager):
		OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

		self._d_Map_Data = OpenRTM_aist.instantiateDataType(RTC.TimedPoint3D)
		"""
		"""
		self._Map_DataIn = OpenRTM_aist.InPort("Map_Data", self._d_Map_Data)
		self._d_R_move = OpenRTM_aist.instantiateDataType(RTC.TimedVelocity2D)
		"""
		"""
		self._R_moveIn = OpenRTM_aist.InPort("R_move", self._d_R_move)
		self._d_Object_Place = OpenRTM_aist.instantiateDataType(RTC.TimedPoint2D)
		"""
		"""
		self._Place_DataOut = OpenRTM_aist.OutPort("Place_Data", self._d_Object_Place)
		self._d_Robot_place = OpenRTM_aist.instantiateDataType(RTC.TimedPose2D)
		"""
		"""
		self._Robot_DataOut = OpenRTM_aist.OutPort("Robot_Data", self._d_Robot_place)
		self._d_Goal_area = OpenRTM_aist.instantiateDataType(RTC.TimedPoint2D)
		"""
		"""
		self._Goal_DataOut = OpenRTM_aist.OutPort("Goal_Data", self._d_Goal_area)





		# initialize of configuration-data.
		# <rtc-template block="init_conf_param">
		"""
		
		 - Name:  Pot_Gain
		 - DefaultValue: 1
		"""
		self._Pot_Gain = [1]
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
		self.bindParameter("Potential_Gain", self._Pot_Gain, "1")
		self.bindParameter("Goal_Place_x", self._Goal_Place_x, "0.0")
		self.bindParameter("Goal_Place_y", self._Goal_Place_y, "0.0")

		# Set InPort buffers
		self.addInPort("Map_Data",self._Map_DataIn)
		self.addInPort("R_move",self._R_moveIn)

		# Set OutPort buffers
		self.addOutPort("Place_Data",self._Place_DataOut)
		self.addOutPort("Robot_Data",self._Robot_DataOut)
		self.addOutPort("Goal_Data",self._Goal_DataOut)

		# Set service provider to Ports

		# Set service consumers to Ports

		# Set CORBA Service Ports

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




def PotentialMapTestInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=potentialmaptest_spec)
    manager.registerFactory(profile,
                            PotentialMapTest,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    PotentialMapTestInit(manager)

    # Create a component
    comp = manager.createComponent("PotentialMapTest")

def main():
	mgr = OpenRTM_aist.Manager.init(sys.argv)
	mgr.setModuleInitProc(MyModuleInit)
	mgr.activateManager()
	mgr.runManager()

if __name__ == "__main__":
	main()

