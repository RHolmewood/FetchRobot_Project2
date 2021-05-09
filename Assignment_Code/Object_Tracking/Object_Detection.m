%% OBJECT DETECTION  CODE
% USED PRIMARILY FOR THE FETCH ROBOT 
% Written By: Reece Holmewood ST.ID> 12875629

%% SETUP
% Connect to ROS 
rosshutdown;                                                                % Disconnects any current ROS nodes open
gazeboAddress = '11311';                                          % Variable for the address of gazebo
rosinit(gazeboAddress);                                                     % Establishes initial connection

% Setup ROS subscribers and publishers
videoData = rossubscriber('/head_camera/rgb/image_raw/compressed');         % Set the subscriber to the image feed from the fetch
receive(videoData,10);                                                      % Wait for first message

% IF HAND or BASE MOVEMENT IS PLACED IN SAME FILE CREATE THE PUBLISHER FOR 
% MOVEMENT COMMANDS...

vidPlayer = vision.DeployableVideoPlayer;

%% PROGRAM LOOP

while(1)
    %% SENSE
    % Collect incoming Data
    img = readImage(videoData.LatestMessage);                               % Reads the latest message from the image subscriber
    
    %% PROCESS AND FILTER
    % Object Detection Function/Algorithm
    
    %% CONTROL
    
    %% VISUALISE
    step(vidPlayer,img);
end
