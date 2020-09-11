# RM-codes
----------
This repository contains the codes we used for our Master by Research project which is entitled: "Data Fusion and Formation Control: Application to Wildlife Monitoring".

The project involves a Video Object Tracking (VOT) solution which is based on Particle Filter (PF). The PF uses two measurement providers which are switched on the basis of the Structural Similarity Index (SSIM) between the target's initial template and a patch of its current appearance. When the SSIM index is below a set threshold, the measurements are provided by a colour image segmentation technique. On the contrary, the measurement provider is another method. We first used the You Only Look Once (YOLO) algorithm. Next we change the latter to one of the eight trackers implemented in OpenCV. 

The project also contains other codes for the simulations of a target relay between two drones based on the SSIM index between two frames which represent the two drones Field of Views.


Description
-----------

Acknowledgments 
----------------
- For our implementation of the Particle Filter, we followed [mpatacchiola](https://github.com/mpatacchiola)'s great [motion tracking module](https://github.com/mpatacchiola/deepgaze/blob/master/deepgaze/motion_tracking.py) (who followed the [work of rlabbe](https://github.com/rlabbe/Kalman-and-Bayesian-Filters-in-Python)).

- Regarding the YOLO, we followed [Nayak's nice tutotrial](https://www.learnopencv.com/deep-learning-based-object-detection-using-yolov3-with-opencv-python-c/).
