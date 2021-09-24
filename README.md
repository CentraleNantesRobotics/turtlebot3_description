# TurtleBot3

This fork of `turtlebot3_description` simply adds a prefix argument for `.xacro` files.

It is used to rename all links within the model, together with a namespaced execution, allowing an easy multi-robot setup.

## Bringup

Assuming you have `simple_launch` and `nav2_common`, running the included `bringup_launch.py` will run ROS 2 on the Turtlebot and prefix or namespace nodes, topics and TF links with the `HOSTNAME` of the Turtlebot.

## Work in progress

Prefixed models:

 - `turtlebot3_waffle_pi.urdf.xacro`
 - `turtlebot3_waffle_pi.gazebo.urdf.xacro`
