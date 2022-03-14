#! /usr/bin/env python

import rospy
"""
    演示参数查询
        get_param(键,默认值)
        当键存在时，返回对应的值，如果不存在返回默认值
        get_param_cached
        get_param_names
        has_param
        search_param
"""


if __name__ == "__main__":
    rospy.init_node("get_param_p")
    #1.get_param(根据键获取值)
    radius = rospy.get_param("radius_p",0.5)
    radius2 = rospy.get_param("radius_p_xxx",0.5)
    rospy.loginfo("radius = %.2f",radius)
    rospy.loginfo("radius = %.2f",radius2)

    #2.get_param_ached(和1一致，但底层效率高，能从缓存中取数据)
    radius3 = rospy.get_param("radius_p",0.5)
    radius4 = rospy.get_param("radius_p_xxx",0.5)
    rospy.loginfo("radius = %.2f",radius3)
    rospy.loginfo("radius = %.2f",radius4)

    #3.get_param_names(获取键名称)
    names = rospy.get_param_names()
    for name in names:
        rospy.loginfo("names = %s",name)

    #4.has_param 判断某个键是否存在
    flag1 = rospy.has_param("radius_p")
    if flag1:
        rospy.loginfo("radius_p 存在")
    else:
        rospy.loginfo("不存在")

    flag2 = rospy.has_param("radius_p_xxx")
    if flag2:
        rospy.loginfo("radius_p_xxx 存在")
    else:
        rospy.loginfo("不存在")

    #5.search_param(寻找某个键，如果存在，则返回键名)
    key = rospy.search_param("radius_p")
    rospy.loginfo("key = %s",key)
