# FetchRobot_Project2
This repository will be used for the Fetch manipulator grasping task, as per the coursework for Sensors and Control (41014).

# Contributions
Lachlan Dunn (99143644) - 32.5%
Alistair Higgins (12934600) - 35%
Reece Holmewood (12875629)- 32.5%

Overall we are all happy with each other's contributions during this course.

#Description of code
Our code is based upon our own learning through lectures and tutorials in this subject, the ROS wiki, the Fetch Robotics tutorial pages, and tutorials regarding the use of MoveIt and python in the creation of a pick and place program. Our code utilises MoveiIt to establish our robot, its joints and linkages, movement groups, controllers and perception. We then created a unique world file to populate with our graspable items and some aesthetic background items, before establishing our actual grasping code with an adaptation of Michael Ferguson's pick_and_place.launch.

We would like to acknowledge Alberto Ezquerro of TheConstruct for his RBKairos robot MoveIt tutorial which we used to inform our own creation of a MoveIt package (named snc_fetch)for our fetch robot, and Michael Ferguson of Fetch Robotics, who created the simple grasping directory and its contents, which is utilised in this project. Key files that we created and/or edited in this project are:

1. fetch_gazebo > models directory: Numerous models (especially cubes and beer were modified in terms of scale, colour and physics properties) and liang_wall is a modified version of grey_wall with retexturing.
2. fetch_gazebo > simple_pick_place.sdf: this file contains the locations and attributes of the items we used to populate the Gazebo environment.
3. snc_fetch directory: this directory is the result of the MoveIt Setup Assistant Program, with some additions.
4. simple_grasping.yaml: this file contains important characteristic information for the use of the gripper; we reduced the tool_to_planning_frame distance to get the object deeper into the active grasp.
5. ros_controllers.yaml: Contains the controller information for the different planning groups. MoveIt Setup Assistant incorrectly assigned gripper controller which caused issues until it was resolved through research.
6. motion_planning_program.py: short python program to test movement of the robot in gazebo/rviz but with no grasping involved.
7. basic_grasping_perception_dbg.launch: initialises the simple_grasping ros topics for utilisation in rviz.
8. fetch_planning_execution.launch: file that launches the moveit.rviz for this project. Has issues loading the rviz file and this may need to be done manually through snc_fetch/launch/moveit.rviz in RVIZ.
9. pick_and_place.launch: Adapted version of Michael Ferguson's code that perceives and grasps objects in the fetch robot environment using the aforementioned grasping ros topic to identify said objects.


#Structure of code

To run our simulation, use the following steps:

1. Start up your roscore in terminal.

2. Launch the custom gazebo environment with 'roslaunch fetch_gazebo simple_grasp.launch'.

3. Launch the RVIZ of the gazebo environment using 'roslaunch snc_fetch fetch_planning_execution.launch'

4. Open the snc_fetch moveit.rviz file maually if it does not appear immediately
in the RVIZ window. This should now display the robot with the 3D point cloud visualising the table in front of it already loaded.

5. In RVIZ's motion planning window, plan and execute movement of the head from its <current> position to <down> position in order to visualise all graspable objects on the table.

6. Launch the perception topics with 'roslaunch simple_grasping basic_perception_dbg.launch'.

7. Inside RVIZ, change the topic being read in the point cloud to the newly available '/basic_grasping_perception/object_cloud' topic.

8. Call the action server 'find_objects' (which was initialised by step 6) by running the commands found in 'action_server_code'in two separate terminals in their specified order. Check in RVIZ to see visualised graspable objects appear.

9. Run the final program with 'roslaunch simple_grasping pick_and_place.launch'

10. Visualise the experiment either in Gazebo to watch the robot react in real time, in terminal to see the code pass through its iterative grasping, or in RVIZ to see a representation of the graspable objects actively update itself with each completed pick and place movement.

11.
