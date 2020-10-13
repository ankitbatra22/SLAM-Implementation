# SLAM Implementation

###  What is Slam?
SLAM is the computational method for constructing or updating a map of an unknown environment while simultaneously keeping track of the location within it. For example in autonomous vehicles it lets you build a map and localize your vehicle in that map at the same time. This helps plan things like path planning and obstacle avoidance. I will be implementing a feature based slam, which is essentially tracking points in one frame and then comparing these points in various frames. 

### To Do List
Begin with basic object detection with computer vision such as lane detection and sign detection on sample dataset
- [ ] Research different implementation techniques such as Kalman Filter, Particle Filter, Graph-SLAM
[ ] Choose tracking technique such as goodFeaturesToTrack or ORB in openCV
[ ] Match tracked points frame to frame and then estimate pose transformation
[ ] 3D mapping on Pangolin

