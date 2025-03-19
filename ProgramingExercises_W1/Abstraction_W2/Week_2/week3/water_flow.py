import math

g = 9.80665  # Acceleration due to gravity (m/s^2)
rho = 998.2  # Density of water (kg/m^3)
mu = 0.001003  # Dynamic viscosity of water (Pa.s)


def water_column_height(tower_height, tank_height):
    return tower_height + tank_height


def pressure_gain_from_water_height(height):
    return rho * g * height / 1000  # Convert to kPa


def pressure_loss_from_pipe(length, diameter, velocity, friction_factor):
    return -(friction_factor * (length / diameter) * (rho * velocity**2 / 2) / 1000)


def pressure_loss_from_fittings(velocity, quantity):
    k = 0.04  # Loss coefficient per fitting
    return -(quantity * k * (rho * velocity**2 / 2) / 1000)


def reynolds_number(diameter, velocity):
    return (rho * velocity * diameter) / mu


def pressure_loss_from_pipe_reduction(diameter1, diameter2, velocity1, velocity2):
    k = (1 - (diameter2 / diameter1) ** 2) ** 2
    return -(k * (rho * velocity1**2 / 2) / 1000)


def main():
    tower_height = float(input("Enter the tower height (m): "))
    tank_height = float(input("Enter the tank height (m): "))
    pipe_length = float(input("Enter the pipe length (m): "))
    pipe_diameter = float(input("Enter the pipe diameter (m): "))
    velocity = float(input("Enter the water velocity (m/s): "))
    friction_factor = float(input("Enter the pipe friction factor: "))
    fittings = int(input("Enter the number of pipe fittings: "))
    diameter2 = float(input("Enter the reduced pipe diameter (m): "))

    height = water_column_height(tower_height, tank_height)
    pressure_height = pressure_gain_from_water_height(height)
    pressure_pipe = pressure_loss_from_pipe(pipe_length, pipe_diameter, velocity, friction_factor)
    pressure_fittings = pressure_loss_from_fittings(velocity, fittings)
    re = reynolds_number(pipe_diameter, velocity)
    velocity2 = velocity * (pipe_diameter / diameter2) ** 2
    pressure_reduction = pressure_loss_from_pipe_reduction(pipe_diameter, diameter2, velocity, velocity2)

    total_pressure = pressure_height + pressure_pipe + pressure_fittings + pressure_reduction

    print(f"Total pressure at the house: {total_pressure:.2f} kPa")
    print(f"Reynolds number: {re:.0f}")


if __name__ == "__main__":
    main()
