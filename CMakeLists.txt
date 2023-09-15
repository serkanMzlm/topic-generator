cmake_minimum_required(VERSION 3.8)
project(topic_create)

add_custom_command(
    OUTPUT dynamic_topic.cpp
    COMMAND python3 ${CMAKE_CURRENT_SOURCE_DIR}/topic_create.py
            --yaml-file ${CMAKE_CURRENT_SOURCE_DIR}/topic_names.yml
            --template-file ${CMAKE_CURRENT_SOURCE_DIR}/dynamic_topic.cpp.em
            --outdir ${CMAKE_CURRENT_BINARY_DIR}

    DEPENDS
			${CMAKE_CURRENT_SOURCE_DIR}/topic_create.py
			${CMAKE_CURRENT_SOURCE_DIR}/dynamic_topic.cpp.em
			${CMAKE_CURRENT_SOURCE_DIR}/topic_names.yml
    COMMENT "Running Python script to generate topic header"
)

add_executable(${PROJECT_NAME} dynamic_topic.cpp)