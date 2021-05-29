# RM-codes
----------
This repository contains the codes we implemented for our Master by Research project which is entitled: "Handover in a Distributed System of UAVs: Application to Wildlife Monitoring".

The project involves a Video Object Tracking (VOT) solution that is based on the Particle Filter (PF). Here, the PF uses two measurement providers which are switched based of the Structural Similarity Index (SSIM) between a template of the initial target appearance and a patch of its current appearance. When the SSIM index is below a set threshold, the measurements are provided by a colour image segmentation technique. Otherwise, the measurement provider is another method. We first use You Only Look Once version three (YOLOv3) algorithm. Next, we replaced YOLOv3 by one of the eight trackers implemented in OpenCV Contribution version 4.1.0. The project also contains other codes for the simulations of tracking relay between two drones based on the SSIM index between two frames that represent the drones Field of Views.

A "toy example", "the cows video" [(available here)](https://github.com/mpatacchiola/deepgaze/blob/master/examples/ex_particle_filter_object_tracking_video/cows.avi), can be used for testing. Note that, with this video, better results are achieved with Goturn and Median Flow as the second measurement provider for the proposed VOT solution as opposed to with Boosting or CSRT. 


Description
-----------

Acknowledgments 
----------------
- For our implementation of the Particle Filter, we used and modified codes from [mpatacchiola](https://github.com/mpatacchiola)'s great [motion tracking module](https://github.com/mpatacchiola/deepgaze/blob/master/deepgaze/motion_tracking.py) (who followed the [work of rlabbe](https://github.com/rlabbe/Kalman-and-Bayesian-Filters-in-Python)).

- Regarding the YOLOv3, we used and modified codes from [Nayak's nice tutotrial](https://www.learnopencv.com/deep-learning-based-object-detection-using-yolov3-with-opencv-python-c/).
