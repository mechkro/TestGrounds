import tkinter as tk
import math


""" 
Currently: 
Command line use tool where multitude of function calls will be required

Future:
GUI implemented to expedite the carry out of calculations and ease of use.
Can add visual graphical aids to asisst in presentations to customer.

*** When using constants from charts be sure the liquids/materials match 
as well as grabbing values with accurate fluid temperatures.***

"""






#-----------------------------------------------------------
def tdh(sorl, hd, hs):
    """ 
    """
    
    if sorl == 'head':
        H = hd - hs
        return H
    
    if sorl == 'lift':
        H = hd + hs
        return H

#-----------------------------------------------------------
def velocity_head(vel = None, Q = None, d = None):
    """ 
    Function to velocity head calculations. Either enter Velocity if known or
    Q(flow) and d(inner diameter of pipe)
    ex: *NOTE - must explicitly write variable = something
    
    >>> x = tdh.velocity_head(vel = 4.5)
    >>> x = tdh.velocity_head(Q = 1000.0, d = 10.0)
    """
    
    g = 32.174  # ft/sec^2
    if vel:
        hv = (vel**2)/(2*g)
        print('Velocity Head = {} ft'.format(hv))
        return hv
    
    if Q:
        v = (0.4085*Q)/(d**2)
        hv = (v**2)/(2*g)
        print('Velocity Head = {} ft'.format(hv))
        return hv


#-----------------------------------------------------------
def fixtures_friction_loss(vel_head, *args):
    """ 
    Func takes velocity_head output as well as K constants for each of the piping fixtures.
    ex:
    
    >>> x = tdh.velocity_head(Q = 1000.0, d = 10.0)
    >>> y = tdh.friction_loss(x, *[1.3, 0.27, 1.5]) Where 1.3,0.27,1.5 are all K's found in reference charts
    """
    
    K_sum = sum([i for i in args])
    hf = vel_head*K_sum
    print('hf (Pipe fixtures head loss) = {} ft'.format(hf))
    return hf


#-----------------------------------------------------------
def pipe_friction_loss(pipe_friction_const, L):
    """ 
    
    """
    
    hpipe = pipe_friction_loss*L
    print('hpipe (Piping friction loss) = {} ft'.format(hpipe))
    return hpipe
