#import tkinter as tk
import math


""" 

Currently: 
Command line use tool where multitude of function calls will be required

Future:
- GUI implemented to expedite the carry out of calculations and ease of use.
- Can add visual graphical aids to asisst in presentations to customer.
- Break down the GUI to 2 frames - Suction and Discharge which are then 
broken down into parts of the friction loss total



*** When using constants from charts be sure the liquids/materials match 
as well as grabbing values with accurate fluid temperatures.***

Total Differential Head - 
TDH (Flooded Suction) = Hd - Hs
TDH (Suction Lift) = Hd + Hs

Hd, Hs are both sums of friction losses in terms of feet of head 
based upon the system and fluid parameters.

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
    Function takes piping friction loss per x amount of feet and returns 
    the head for pipe friction
    
    Ex:
    x = pipe_friction_loss(2.25/100.0, 5.0)
    """
    
    hpipe = pipe_friction_const*L
    print('hpipe (Piping friction loss) = {} ft'.format(hpipe))
    
    return hpipe


#-----------------------------------------------------------
def npsha(hp, hvpa, hst, hfs, ha, npshr = None):
    """ 
    Function to calculate NPSHa (available) in the system. We need to be sure NPSHr < NPSHa
    or cavitation begins.
    
    hp = absolute pressure on fluid surface = IF open to atmosphere then barometric pressure 
                                             - or - absolute pressure of existing fluid in tank
    hvpa = Vapor Pressure = gathered from charts (*be sure to base on temperature)
    hst = static pressure = +(above) or -(below) the centerline
    ha = (L*Vn*C*SG)/(2.31*K*g)
          Where:
          - L: length of suction line
          - 
    npshr = NPSH required - provided by pump manufacturer (optional)
      
    
    Ex:
    x = pipe_friction_loss(2.25/100.0, 5.0)
    """
    pass

    
#-----------------------------------------------------------
def convert_ft_to_psi(fthead, sg = None, W = None):
    """
    Conversion formula for calculating head in psi if head in ft is known, as well
    as either the specific gravity or Specific weight (ex. W for water = 62.32 lb/ft^3 @ 68 deg C)
    
    ex:
    >>> x = tdh.convert_ft_to_psi(15.0, sg = 1.0)
    or
    >>> x = tdh.convert_ft_to_psi(15.0, W = 62.32)
    """
    
    try:                #Try and except functionality added to ease traceability for end-user to identify problem area if not familiar with command line errors
        
        if sg:
            head_psi = (fthead*sg)/2.31
            print('Head in psi = {} psi,\nwhen head in feet = {}'.format(head_psi, fthead))
            return head_psi
        if W:
            head_psi = (fthead*W)/144.0
            print('Head in psi = {} psi,\nwhen head in feet = {}'.format(head_psi, fthead))
            return head_psi
        
    except Exception as e:
        print('Error in convert head to psi function')
        print(e)    
    
    
#-----------------------------------------------------------
def convert_psi_to_head(psihead, sg = None, W = None):
    """
    Conversion formula for calculating head in ft if head in psi is known, as well
    as either the specific gravity or Specific weight (ex. W for water = 62.32 lb/ft^3 @ 68 deg C)
    
    ex:
    >>> x = tdh.convert_psi_to_head(6.5, sg = 1.0)
    or
    >>> x = tdh.convert_psi_to_head(6.5, W = 62.32)
    """
    
    try:                    #Try and except functionality added to ease traceability for end-user to identify problem area if not familiar with command line errors
        
        if sg:
            head_ft = (psihead*2.31)/sg
            print('Head in ft = {} ft,\nwhen head in psi = {}'.format(head_ft, psihead))
            return head_ft
        if W:
            head_ft = (psihead*144.0)/W
            print('Head in ft = {} ft,\nwhen head in psi = {}'.format(head_ft, psihead))
            return head_ft
        
    except Exception as e:
        print('Error in convert psi to head function')
        print(e)
    
