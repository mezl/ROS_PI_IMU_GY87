#!/usr/bin/env python
#****************************************************************************
#  Project: How to manage a stepper motor via ROS?
#  Description:  The Publisher Node. Sending direction data for rotation. The user enters the data via a query  
#  -------------------------------------------------------------------------
#  All rights reserved.
#
#****************************************************************************
import rospy
# In this case, we are going to use a String, defined in the ROS standart message pakage.
# Sinse we are using a message from another package, we have to tell the ROS build system 
# about this by adding a dependency to our package.xml
from std_msgs.msg import String 

rospy.init_node('Stepper_Publisher')	# Initializing the node
pub = rospy.Publisher('rotation', String, queue_size=10)

while not rospy.is_shutdown():		# The function will return True if the node is ready to be shut down and False otherwise
    # This node publishes the input data on the topic "rotation"
    rate = rospy.Rate(1)
    data = raw_input('Enter F/R for clockwise or counterclockwise: ')
    data2 = raw_input('Enter how many steps (1~10000): ')
    data3 = raw_input('Enter how speed (100~2000): ')
    if data in ("F","R"): 
        cmd = ",".join([data,data2,data3])
        print cmd
        pub.publish(cmd)
        rate.sleep()
