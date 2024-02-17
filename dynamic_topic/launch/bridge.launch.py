import os
from launch_ros.actions import Node
from launch import LaunchDescription

##########################################################
#                   BRIDGE                               #
##########################################################
imu_bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=['/imu@sensor_msgs/msg/Imu@gz.msgs.IMU'],
        remappings=[('/imu','/in/imu')],
    )

altimeter_bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=['/altimeter@std_msgs/msg/Float32@gz.msgs.Float'],
        remappings=[('/altimeter', '/in/altimeter')],
    )

lidar_bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=["/lidar/points@sensor_msgs/msg/PointCloud2[gz.msgs.PointCloudPacked"],
        remappings=[('/altimeter', '/in/lidar')],
    )

##########################################################
#                  CAMERA BRIDGE                         #
##########################################################

camera_bridge = Node(
            package='ros_gz_bridge',                                              
            executable='parameter_bridge',
            arguments=['/camera@sensor_msgs/msg/Image@gz.msgs.Image']
)

def generate_launch_description():
    return LaunchDescription([
        imu_bridge,
        altimeter_bridge,
        lidar_bridge,
        camera_bridge
    ])
    