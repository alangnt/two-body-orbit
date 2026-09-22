import math

G = 6.6743*10e-11
MASS_PLUTO = 1.303*10e22        # (m_a)
MASS_CHARON = 1.586*10e21       # (m_b)
MEAN_SEPARATION = 1.9596*10e7   # (r)
ORBITAL_ECCENTRICITY = 0        # (e)

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
    barycenter_a = calculate_distance_to_barycenter(total_mass, MASS_CHARON)
    barycenter_b = calculate_distance_to_barycenter(total_mass, MASS_PLUTO)
    
    combined_grav_param = calculate_combined_gravitational_parameter(total_mass)
    reduced_mass = calculate_reduced_mass(multiplied_mass, total_mass)
    
    print(math.isclose((barycenter_a + barycenter_b), MEAN_SEPARATION))
    
main()