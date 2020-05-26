import time 
import matplotlib.pyplt as plt 
from tqdm import tqdm
import math 

class NeuralNet():
  def __init__(self, flattened_input_shape, hidden_layer_dims_array, n_outputs, activations):
    self.flattened_input_shape = flattened_input_shape
    self.hidden_layer_dims = hidden_layer_dims_array
    self.n_outputs = n_outputs
        
  def loss_backward(self, loss): # For back_propagation and optimizing the weights
    pass
    
  def __str__(self): # For printing the neural network
    pass
    
  def __repr__(self): # For representing the network as an object
    pass
    
  def __call__(self, input): # For feed_forward
    pass
