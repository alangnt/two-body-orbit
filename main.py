import math

G = 6.6743*10e-11
MASS_PLUTO = 1.303*10e22        # (m_a)
MASS_CHARON = 1.586*10e21       # (m_b)
MEAN_SEPARATION = 1.9596*10e7   # (r)
ORBITAL_ECCENTRICITY = 0        # (e)

def calculate_orbital_velocity(angular_velocity, distance_to_barycenter):
    return angular_velocity * distance_to_barycenter

def calculate_angular_velocity(orbital_period):
    return (2 * math.pi) / orbital_period

def calculate_orbital_period(combined_grav_param):
    return (2 * math.pi) * math.sqrt((MEAN_SEPARATION ** 3) / combined_grav_param)

def calculate_relative_orbital_velocity(combined_grav_param):
    return math.sqrt(combined_grav_param / MEAN_SEPARATION)

def calculate_reduced_mass(multiplied_mass, total_mass):
    return multiplied_mass / total_mass

def calculate_combined_gravitational_parameter(total_mass):
    return G * total_mass

def calculate_distance_to_barycenter(total_mass, m_b):
    return MEAN_SEPARATION * (m_b / total_mass)

def main():
    # TODO: input planets
    
    # total mass and multiplied mass
    # calculed once, won't change
    total_mass = MASS_PLUTO + MASS_CHARON
    multiplied_mass = MASS_PLUTO * MASS_CHARON
    
    # locate the barycenter
    barycenter_a = calculate_distance_to_barycenter(total_mass, MASS_CHARON)        # r_a
    barycenter_b = calculate_distance_to_barycenter(total_mass, MASS_PLUTO)         # r_b
    
    combined_grav_param = calculate_combined_gravitational_parameter(total_mass)    # µ(grav)
    reduced_mass = calculate_reduced_mass(multiplied_mass, total_mass)              # µ
    
    # now we calculate the relative orbital velocity
    # and the relative orbital period
    orbital_velocity = calculate_relative_orbital_velocity(combined_grav_param)     # v(rel)
    orbital_period = calculate_orbital_period(combined_grav_param)                  # T
    
    # we can then calculate the angular velocity
    angular_velocity = calculate_angular_velocity(orbital_period)                   # ω
    
    # now we calculate both orbital velocities
    orbital_speed_a = calculate_orbital_velocity(angular_velocity, barycenter_a)    # v_a
    orbital_speed_b = calculate_orbital_velocity(angular_velocity, barycenter_b)    # v_b
    
    print(math.isclose((orbital_speed_a + orbital_speed_b), orbital_velocity))
    
main()