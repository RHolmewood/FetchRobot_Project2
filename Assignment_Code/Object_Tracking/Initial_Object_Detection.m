%% OBJECT DETECTION  CODE
% USED PRIMARILY FOR THE FETCH ROBOT 
% Author: Reece Holmewood - 12875629
%         Alistair Higgins - 

%% SETUP
% Connect to ROS 
rosshutdown;                                                                % Disconnects any current ROS nodes open
gazeboAddress = 'localhost';                                                % Variable for the address of gazebo
rosinit(gazeboAddress);                                                     % Establishes initial connection
%% Setup ROS subscribers and publishers
RGB_ImageSubscriber = rossubscriber('/head_camera/rgb/image_raw/compressed');% Set the subscriber to the image feed from the fetch


%% SENSE
% Collect incoming Data
img = readImage(image.LatestMessage);                                       % Reads the latest message from the image subscriber

%% DISTINGUISHING COLOURS
figure(1);
fontSize = 10;
subplot(2,2,1);
imshow(img);       
drawnow();
caption = sprintf('Original Colour Image');                                 % Sets title for image
title(caption, 'FontSize', fontSize);                                       % Plots title
                                                        

% PROCESS AND FILTER
hold on;
% Colour Segmentation
R = img(:,:,1);                                                             % Red image data
G = img(:,:,2);                                                             % Green image data
B = img(:,:,3);                                                             % Blue image data

% Display Colour Segments
subplot(2,2,2);
imshow(R);
title('Red Array', 'FontSize', fontSize);
subplot(2,2,3);
imshow(G);
title('Green Array', 'FontSize', fontSize);
subplot(2,2,4);
imshow(B);
title('Blue Array', 'FontSize', fontSize);

%% DETERMINING COLOUR THRESHOLDS
figure(2);




%% SEND OPERATION ORDER CONTROL

%% FUNCTIONS
function [pixels] = HistogramPlot(colour,colourSTR)

    [pixels, ~] = imhist(colour);                                   % Output gray levels and pixel count from "imhist"
    maxPixelCount = max(pixels);
    bar(pixels, 'r');
    grid on;
    xlabel('Gray Level');
    ylabel('No. of Pixels');
    title(('Histogram of'+colourSTR), 'FontSize', fontSize);
    
end

    


