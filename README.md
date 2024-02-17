## Creating Topics from Parameter Files in ROS2

The `params\topic_names.yml` file included in the package contains **publications** and **subscriptions** for ROS2. This file updates the package correctly on the ROS2 side when written accurately. This enables the generation of new publishers and subscribers on the ROS2 side by simply adding entries on the param side. 

#### Build
```
colcon build --packages-select dynamic_topic
```
#### Run
```
. install/setup.bash
ros2 run dynamic_topic dynamic_topic_node
```

- New features to be added are written in the `main.cpp` file.
- To write persistent code to the **.em** extension packages of `dynamic_topic.cpp` and `dynamic_topic.hpp` files, the code should be written directly to these files. Since these files are continuously recreated, any code you write to them will be invalidated.

- In case of errors resulting from adding or deleting new files, the build, log, install folders should be deleted, and the build process should be repeated.

- The (void)msg parts in the `dynamic_topic.cpp` file are written solely to suppress warnings.




