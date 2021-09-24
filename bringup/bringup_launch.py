#!/usr/bin/env python3
#
# Copyright 2019 ROBOTIS CO., LTD.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Authors: Darby Lim
# 
# adapted to multi-robot + simple_launch, Olivier Kermorgant

import os
from simple_launch import SimpleLauncher
from nav2_common.launch import RewrittenYaml

def generate_launch_description():
    TURTLEBOT3_MODEL = os.environ['TURTLEBOT3_MODEL']
    
    sl = SimpleLauncher()
    
    # all happens in this namespace
    
    sl.declare_arg('name', os.uname().nodename)
    
    sl.declare_arg('usb_port', default_value='/dev/ttyACM0', description='Connected USB port with OpenCR')
    
    sl.declare_arg('tb3_param_dir', 
                   sl.find('turtlebot3_bringup', TURTLEBOT3_MODEL + '.yaml'),
                   description='Full path to turtlebot3 parameter file to load')
        
    sl.declare_arg('use_sim_time', 'false', description='Use simulation (Gazebo) clock if true')
    
    
    with sl.group(ns=sl.arg('name')):
        
        sl.robot_state_publisher('turtlebot3_description','turtlebot3_' + TURTLEBOT3_MODEL + '.urdf.xacro', 
                                 xacro_args={'prefix': sl.name_join(sl.arg('name'), '/')},
                                 parameters={'use_sim_time': sl.arg('use_sim_time')})
        
        sl.include('hls_lfcd_lds_driver', 'hlds_laser.launch.py', 
                   launch_arguments={'port': '/dev/ttyUSB0', 'frame_id': sl.name_join(sl.arg('name'), '/base_scan')})        
        
        configured_params = RewrittenYaml(
                            source_file=sl.arg('tb3_param_dir'),
                            root_key=sl.arg('name'),
                            param_rewrites={'frame_id': sl.name_join(sl.arg('name'), '/odom'),
                                            'child_frame_id': sl.name_join(sl.arg('name'), '/base_footprint')},
                            convert_types=True)
                
        
        sl.node('turtlebot3_node', 'turtlebot3_ros',
                parameters=[configured_params],
                arguments=['-i', sl.arg('usb_port')])

    return sl.launch_description()
