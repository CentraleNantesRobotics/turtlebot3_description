cmake_minimum_required(VERSION 3.5)
project(turtlebot3_description)

find_package(ament_cmake REQUIRED)

install(DIRECTORY meshes rviz urdf bringup
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
