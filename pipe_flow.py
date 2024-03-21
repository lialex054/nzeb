import math

def main():
    # initial vals
    global velocity_u, head_loss, pressure_diff, total_loss, total_pressure_diff, skin_friction_coefficient, friction_factor, power, pressure_elevation, pressure_fittings, height
    
    flow_rate = 0.0016                 # Q in m^3s^-1
    diameter = 0.0408                   # d in m
    length_pipe = 49.42                     # L in m
    viscosity = 0.001                   # mu in Pa s
    density = 997                       # rho in kgm^-3
    roughness = 1.5*10**(-6)          # e in m
    number_bends = 26                   # number of 90 deg bends
    number_tees = 5                    # number of tees
    gravity_constant = 9.81             # g in m/s^2
    pump_efficiency = 0.5               # pump efficiency in percent
    height = 5.2                          # height difference

    # found vals
    velocity_u = 0                      # u_hat in m/s
    skin_friction_coefficient = 0       # Cf in f/4
    friction_factor = 0
    head_loss = 0
    pressure_diff = 0
    pressure_elevation = 0
    pressure_fittings = 0
    total_loss = 0
    total_pressure_diff = 0
    power = 0

    def moody_vals():
        # Find the Reynolds Number and RD ratio, for Moody Diagram
        global velocity_u
        area = (math.pi * (diameter ** 2)) / 4                               # calculates area of pipe
        velocity_u = flow_rate / area                                       # calculates the velocity of the flow
        reynolds_number = (density * velocity_u * diameter) / viscosity      # finds reynolds number
        print("Reynold's Number:", reynolds_number)

        # Roughness to diameter ratio
        rd_ratio = roughness / diameter
        print("Roughness to diameter ratio:", rd_ratio)

    def bernoulli():
        # Calculates head loss due to friction
        global head_loss
        head_loss = friction_factor * (length_pipe / diameter) * ((velocity_u ** 2) / (2 * gravity_constant))
        print("Head loss due to friction: ", str(head_loss))

    def pressure_loss():
        # Calculates pressure loss of pipe system
        global pressure_diff
        pressure_diff = friction_factor * (length_pipe / diameter) * (0.5 * density * (velocity_u ** 2))
        print("Pressure loss due to friction: ", str(pressure_diff))
    
    def pressure_loss_elevation():
        # Calculate pressure loss due to elevation
        global pressure_elevation
        pressure_elevation = (height * density * gravity_constant)
        print("Pressure loss due to elevation: ", str(pressure_elevation))
    
    def pressure_loss_fittings():
        # Calculate pressure loss due to fittings
        global pressure_fittings
        loss_bends = 0.9 * number_bends * (0.5 * density * velocity_u **2)
        loss_tee = 1.8 * number_tees * (0.5*density * velocity_u**2)
        pressure_fittings = loss_bends + loss_tee
        print("Pressure loss due to fittings: ", str(pressure_fittings))

    def total_head_loss():
        # calculate total head loss due to fittings
        global total_loss
        loss_bends = 0.9 * number_bends * ((velocity_u ** 2) / (2 * gravity_constant))
        loss_tee = 1.8 * number_tees * ((velocity_u ** 2) / (2 * gravity_constant))
        head_loss_fittings = loss_bends + loss_tee
        print("Head loss due to fittings: ", str(head_loss_fittings))
        total_loss = 2*(head_loss + head_loss_fittings)
        return total_loss
    
    def total_pressure_loss():
        # caculate total pressure loss
        global total_pressure_diff
        total_pressure_diff = 2*(pressure_elevation + pressure_diff + pressure_fittings)
        return total_pressure_diff
    
    def power_calc():
        # calculate total power consumption
        global power
        power = flow_rate * total_pressure_diff / pump_efficiency
        return power
    
    def run_prog():
        global skin_friction_coefficient
        global friction_factor
        moody_vals()
        skin_friction_coefficient = float(input("What is the skin friction coefficient?: \n"))
        friction_factor = skin_friction_coefficient * 4
        bernoulli()
        pressure_loss()
        pressure_loss_elevation()
        pressure_loss_fittings()
        total_head_loss()
        total_pressure_loss()
        power_calc()
        print("Your total head loss is:", total_loss)
        print("Your total pressure loss is:", total_pressure_diff)
        print("Your power consumption is: ", power)
    
    run_prog()

if __name__ == '__main__':
    main()
