
#The MIT License (MIT)

#Copyright (c) 2020 Juliana T.C. Marcos

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


#For our implementation of the Particle Filtering class, we inspired from the work of Patacchiola which followed R Labbe.
#Thanks for these great works which repositories are availabe here:
#https://github.com/mpatacchiola/deepgaze
#https://github.com/rlabbe/Kalman-and-Bayesian-Filters-in-Python


#Import of useful librairies
import cv2
import math
import numpy as np

class ParticleFilter:
    """ This class is an implementation of the Particle Filter algorithm applied for object tracking in videos.
    It involves several variables and methods."""

    def __init__(self,width,height,n_particles):
        """This method is the constructor of the class Particle Filter"""
    
        self.particles=np.array(np.random.uniform(low=[0,0], high=[width,height], size=(n_particles,2)))
        self.weights=np.array([1./n_particles for i in range(n_particles)])
        
    def particles_update(self,v_x,v_y,std,argwidth,argheight):
        """This function predicts the next movement of the object tracked in the video. This is done by adding
        to the particles' x and y coordinates the estimated velocities on X and Y axes and a Gaussian noise with
        a mean equal to zero and a standard deviation equal to std. It is assumed that there is a very small time
        between two frames which multiplies vx and vy to represent the target's distance between two consecutives
        frames"""
        
        self.particles[:,0]+=v_x+std*np.random.randn(len(self.particles))
        self.particles[:,1]+=v_y+std*np.random.randn(len(self.particles))
        
    def weigth_update(self,x,y):
        """This function updates the particle weigths given the new measurement for the position (x,y) of the tracked object  centroid"""
        
        #Difference between x and y axes of the particles and the new measurement
        dist_error=np.zeros((len(self.particles),2))
        dist_error[:,0]=self.particles[:,0]-x
        dist_error[:,1]=self.particles[:,1]-y
        #Computation of euclidean distance given error between coordinates
        dist_error_eucl = np.linalg.norm(dist_error, axis=1)
        #Inversion of euclidean distance of particles to obtain weights (small error will then have high weight)
        dist_error_eucl=1./dist_error_eucl
        #Prior multiply by non normalized likelihood
        self.weights*=dist_error_eucl
        #Division by zero avoidance
        self.weights+=1.e-500
        #Normalisation
        self.weights=self.weights/sum(self.weights)
    
    def position_estimation(self):
        """This function estimates the x and y coordonates of the center of the object tracked."""
        
        x_estimation = np.average(self.particles[:, 0], weights=self.weights, axis=0).astype(int)
        y_estimation = np.average(self.particles[:, 1], weights=self.weights, axis=0).astype(int)
        
        return x_estimation,y_estimation
    
    def resampling(self):
        """This function resamples the particles according to their weigths. The particles with the highest weigths 
        are more likely to be taken."""
        
        #Find the indices of the relevant elements in a uniform random list to respect sorted order of cumsum.
        indices = np.searchsorted(np.cumsum(self.weights), np.random.uniform(0.0, 1.0, len(self.particles))) 
        self.particles[:]=self.particles[indices]
        self.weights[:]=self.weights[indices]
        self.weights /= np.sum(self.weights)  
        
    def effective_particles(self):
        """This function return Neff which helps to decides if resampling or not"""
        
        return 1./sum(np.square(self.weights))
    
    def draw_box_particles(self,frame,BB,x,y,radius=3,color=[0,0,255]):
        """This function draw the particles represented by circles on the given frame."""
       
        for x, y in self.particles.astype(int):
            cv2.circle(frame, (x, y), radius, color, -1)
        #This function use the coordinates of the upper left corner of BB and its 
        # opposite point (on a diagonal)
        cv2.rectangle(frame, (BB[0],BB[1]), (BB[0]+BB[2],BB[1]+BB[3]), (255,0,0), 2)

       
