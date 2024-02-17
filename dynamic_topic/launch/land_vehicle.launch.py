#!/usr/bin/python3
import os
from launch_ros.actions import Node
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch.actions import IncludeLaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch.events import Shutdown
from launch.event_handlers import OnProcessExit
from launch.actions import RegisterEventHandler, EmitEvent

land_vehicle_path = get_package_share_directory('land_vehicle')
dynamic_topic_path = get_package_share_directory('dynamic_topic')

simulation_worlds_file = os.path.join(land_vehicle_path, 'world','upd_12.world')

simulation = ExecuteProcess(
            cmd=['gz', 'sim','-r', simulation_worlds_file],
            output='screen'
        )

simulation_server = ExecuteProcess(
            cmd=['gz', 'sim','-r', '-s', simulation_worlds_file],
            output='screen'
        )

#######################################
#              PACKAGES               #
#######################################
merged_depth_camera = Node(
    package='dynamic_topic',
    executable='dynamic_topic_node'
)

#######################################
#              LAUNCH FILE            #
#######################################
sim_bridge = IncludeLaunchDescription(
    PythonLaunchDescriptionSource(os.path.join(dynamic_topic_path, 'launch', 'bridge.launch.py'))
)

########################################
def generate_launch_description():    
    return LaunchDescription([
        simulation,
        sim_bridge,
        RegisterEventHandler(
            event_handler=OnProcessExit(
            target_action=simulation,
            on_exit=[EmitEvent(event=Shutdown)]
          )
        )
	])