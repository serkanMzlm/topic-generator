cmake_minimum_required(VERSION 3.8)
project(dynamic_topic)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)

# add_custom_command(
#     OUTPUT dynamic_topic.cpp
#     COMMAND python3 ${CMAKE_CURRENT_SOURCE_DIR}/topic_create.py
#             --yaml-file ${CMAKE_CURRENT_SOURCE_DIR}/topic_names.yml
#             --template-file ${CMAKE_CURRENT_SOURCE_DIR}/dynamic_topic.cpp.em
#             --outdir ${CMAKE_CURRENT_SOURCE_DIR}
#             # --outdir ${CMAKE_CURRENT_BINARY_DIR}
            
#     DEPENDS
# 			${CMAKE_CURRENT_SOURCE_DIR}/topic_create.py
# 			${CMAKE_CURRENT_SOURCE_DIR}/dynamic_topic.cpp.em
# 			${CMAKE_CURRENT_SOURCE_DIR}/topic_names.yml
#     COMMENT "Running Python script to generate topic header"
# )

execute_process(
    COMMAND python3 ${CMAKE_CURRENT_SOURCE_DIR}/topic_create.py
            --yaml-file ${CMAKE_CURRENT_SOURCE_DIR}/topic_names.yml
            --template-file ${CMAKE_CURRENT_SOURCE_DIR}/dynamic_topic.hpp.em
            --outdir ${CMAKE_CURRENT_SOURCE_DIR}/include
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    RESULT_VARIABLE result
)

file(GLOB_RECURSE SOURCE_CODE  ${PROJECT_SOURCE_DIR}/src/*.cpp)

include_directories(${PROJECT_SOURCE_DIR}/include)
add_executable(dynamic_topic_node ${SOURCE_CODE})
# add_executable(dyn dynamic_topic.cpp)

ament_target_dependencies(dynamic_topic_node 
  rclcpp
  std_msgs
  sensor_msgs
  geometry_msgs
)

install(TARGETS
  dynamic_topic_node
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
