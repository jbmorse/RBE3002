import rospy
import math

from nav_msgs.msg import OccupancyGrid
from nav_msgs.msg import MapMetaData
from nav_msgs.msg import GridCells
from geometry_msgs.msg import Point

def ColorCells():
	global GridCells
	gridPub = rospy.Publisher('map_color', GridCells)
	PathPub = rospy.Publisher('map_path', GridCells)
	NeighPub = rospy.Publisher('map_neighbors', GridCells)
	ExpandPub = rospy.Publisher('map_expanded', GridCells)
	#rospy.Subscriber('map', OccupancyGrid, mapCallback)
	rospy.sleep(.5)

	gridCells = GridCells()
	gridCells.cell_width = 7
	gridCells.cell_height = 7
	gridCells.cells = [Point()]
	gridCells.cells[0].x = .6
	gridCells.cells[0].y = .6
	gridCells.cells[0].z = 0
	gridCells.header.frame_id = 'map'
	gridPub.publish(gridCells)


if __name__== '__main__':
	rospy.init_node('megagnon_Lab_3_ColorCells_node')
	print "starting ColorCells"
	ColorCells()
	print "end ColorCells"


def ColorCells():
	global GridCells
	gridPub = rospy.Publisher('map_color', GridCells)
	PathPub = rospy.Publisher('map_path', GridCells)
	NeighPub = rospy.Publisher('map_neighbors', GridCells)
	ExpandPub = rospy.Publisher('map_expanded', GridCells)
	#rospy.Subscriber('map', OccupancyGrid, mapCallback)
	rospy.sleep(.5)

	gridCells = GridCells()
	gridCells.cell_width = 7
	gridCells.cell_height = 7
	gridCells.cells = [Point()]
	gridCells.cells[0].x = .6
	gridCells.cells[0].y = .6
	gridCells.cells[0].z = 0
	gridCells.header.frame_id = 'map'
	gridPub.publish(gridCells)

if __name__== '__main__':
	rospy.init_node('megagnon_Lab_3_ColorCells_node')
	print "starting ColorCells"
	ColorCells()
	print "end ColorCells"

