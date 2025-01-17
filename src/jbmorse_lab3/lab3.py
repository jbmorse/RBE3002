#!/usr/bin/env python

import rospy, tf

import AStar

from tf.transformations import euler_from_quaternion

from kobuki_msgs.msg import BumperEvent
from geometry_msgs.msg import Quaternion
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Point
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry
from nav_msgs.msg import OccupancyGrid

import time
import math

def MapCallback(occupancy):
	global mapReady, occupancyGrid
	
	mapReady = 1
	occupancyGrid = occupancy

def GoalCallback(goalPoint):
	global goalReady, goal

	goalReady = 1
	goal.x = int(round(goalPoint.pose.position.x))
	goal.y = int(round(goalPoint.pose.position.y))
	goal.z = 0
	print "printing goal"
	print goal

if __name__ == '__main__':

	global mapReady, occupancyGrid, goalReady, goal

	mapReady = 0
	goalReady = 0

	goal = Point()
	occupancyGrid = None

	rospy.init_node('jbmorse_Lab_3_node')

	rospy.Subscriber('map', OccupancyGrid, MapCallback)
	#rospy.Subscriber('map_metadata', MapMetaData, MapMetaCallback)
	rospy.Subscriber('move_base_simple/goal', PoseStamped, GoalCallback)
	#rospy.Subscriber('initialpose', PoseWithCovarianceStamped, InitialPoseCallback)

	odom_list = tf.TransformListener()

	rospy.sleep(rospy.Duration(1, 0))

	print "Starting Lab 3"

	start = Point()
	start.x = 1
	start.y = 1
	start.z = 0

	rospy.wait_for_service('GetPath')

	while 1:
		while not mapReady or not goalReady:
			time.sleep(.3)
			print "waiting"

		print "what are you stuck on"
		try:
			pathService = rospy.ServiceProxy('GetPath', Pathsrv)
			path = pathService(occupancyGrid, start, goal)
			goalReady = 0
			start.x = goal.x
			start.y = goal.y
		except rospy.ServiceException, e:
			print "Service call failed"

	print "Lab 3 complete!"
