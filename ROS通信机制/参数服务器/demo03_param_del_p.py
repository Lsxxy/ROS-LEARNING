#! /usr/bin/env python

import rospy
"""
    演示参数删除： 
        delete_param()

"""

if __name__ == "__main__":
    rospy.init_node("del_param_p")

    #删除参数
    try:
        rospy.delete_param("radius_p")
    except:
        rospy.loginfo("删除失败")