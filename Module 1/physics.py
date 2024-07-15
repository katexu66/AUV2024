import numpy as np

# Basic physics

def calculate_buoyancy(V: float, density_fluid): # type hints (not enforced but helpful)
    """Calculates buoyancy of an object in a fluid.

    Args:
        V (float): volume of object, m^3
        density_fluid (float): density of fluid, kg/m3

    Returns:
        float: buoyancy of the object, Newtons
    """
    # ^ is docstrings, which explains function (helpful when using function); must be directly under function
    # buoyancy = pgV
    if V > 0 and density_fluid > 0:
        buoyancy = density_fluid*V*9.81
        return f"Buoyancy of the object is + {buoyancy} Newtons."
    else:
        return "Both buoyancy and density fluid should be positive values."

def will_it_float(V, mass):
    """Calculates if an object will float in water.

    Args:
        V (float): volume of object
        mass (float): mass of object

    Returns:
        boolean: True or False for if the object floats
    """
    if V > 0 and mass > 0:
        if 1000*V > mass:
            # floats if buoyant force is greater than force of gravity
            return True
        else:
            return False
    else:
        return "Both volume and mass should be positive values."
    
def calculate_pressure(depth, atmospheric_pressure=101352.932):
    # pressure = pgh
    if depth == 0:
        # if depth is 0, pressure is atmospheric pressure (not zero)
        pressure = atmospheric_pressure
    else:
        # pressure underwater is pgh + atmospheric pressure (pressure is just the pressure of all the fluids above you)
        pressure = depth * 1000 * 9.81 + atmospheric_pressure
    return f"Pressure is + {pressure} Pascals"

def calculate_acceleration(F, m):
    # F = ma
    if m > 0:
        acceleration = F / m
        return acceleration
    else:
        return "Mass must be a positive value."

def calculate_angular_acceleration(tau, I):
    # T = Ia
    angular_accel = tau/I
    return angular_accel

def calculate_torque(F_magnitude, F_direction, r):
    # T = Fr
    torque = F_magnitude * r * np.sin(F_direction)
    return torque

def calculate_moment_of_inertia(m, r):
    # I = mr2
    moment_of_inertia = m * r**2
    
    
# AUV physics

def calculate_auv_acceleration(F_magnitude, F_angle, mass=100, volume=0.1, thruster_distance=0.5):
    F = F_magnitude*np.array([np.cos(F_angle), np.sin(F_angle)]) # use linalg to calculate F components
    # batch operations as much as possible (e.g. linalg > indiv operations)
    acceleration = F/mass
    return acceleration
def calculate_auv_angular_acceleration(F_magnitude, F_angle, inertia=1, thruster_distance=0.5):
    if inertia <= 0:
        raise ZeroDivisionError("Cannot divide by 0 or negative inertia.")
    torque = F_magnitude*thruster_distance*np.sin(F_angle) # torque is only perpendicular force
    angular_accel = torque/inertia
    return angular_accel

def calculate_auv2_acceleration(T, alpha, theta, mass=100):
    # F = ma
    accel = (T*np.cos(alpha))/mass
    return accel
def calculate_auv2_angular_acceleration(T, alpha, L, l, inertia=100):
    pass