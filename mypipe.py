import math


class Pipe:

    def __init__(self, internal_diameter, roughness, length, fluid):
        self.int_dia = internal_diameter
        self.roughness = roughness
        self.length = length
        self.fluid = fluid
        self.velocity = 0
        self.Re = 0
        self.f = 0
        self.deltaP = 0

    def update(self, fluid, flowrate):
        self.v(flowrate)
        self.reynolds(fluid)
        rel_rough = self.roughness / self.int_dia
        f = 1.0
        for i in range(1000):
            fnew = (1/(-2 * math.log10(rel_rough / 3.7 + 2.51
                    / self.Re / math.sqrt(f)))) ** 2
            if abs(fnew-f) < 0.00001:
                break
            f = fnew
        self.f = fnew
        self.deltaP = self.velocity ** 2\
            * (self.f * self.length / self.int_dia) * fluid.density / 2

    def v(self, flowrate):
        area = math.pi * self.int_dia ** 2 / 4
        self.velocity = flowrate / area

    def reynolds(self, fluid):
        self.Re = self.int_dia * self.velocity\
                  * fluid.density / fluid.viscosity

    def int_dia_set(self, internal_diameter):
        self.int_dia = internal_diameter

    def roughness_set(self, roughness):
        self.roughness = roughness

    def length_set(self, length):
        self.length = length


class Fluid:

    def __init__(self, density, viscosity):
        self.density = density
        self.viscosity = viscosity

    def density_set(self, density):
        self.density = density

    def viscosity_set(self, viscosity):
        self.viscosity = viscosity


def get_inputs(varname):
    returnval = 0.
    while True or returnval <= 0:
        try:
            returnval = float(input("Enter {0}: ".format(varname)))
            if returnval > 0:
                break
            else:
                print("Value must be greater than 0.")
        except ValueError:
            print("Invalid input!")
    return returnval


def get_input_roughness(varname):
    returnval = -1.
    while True or returnval < 0:
        try:
            returnval = float(input("Enter {0}: ".format(varname)))
            if returnval >= 0:
                break
            else:
                print("Value must be non-negative.")
        except ValueError:
            print("Invalid input!")
    return returnval


def main():

    density = get_inputs("fluid density (kg/m3)")
    viscosity = get_inputs("viscosity (centipoise)")
    int_dia = get_inputs("pipe internal diameter (mm)")
    roughness = get_input_roughness("pipe roughness (mm)")
    length = get_inputs("pipe length (m)")
    flowrate = get_inputs("fluid flow rate (m3/h)")
    my_fluid = Fluid(density, viscosity / 1000)
    my_pipe = Pipe(int_dia / 1000, roughness / 1000, length, my_fluid)
    my_pipe.update(my_fluid, flowrate / 3600)
    print("Pipe pressure loss = {0:0.1f} kPa".format(my_pipe.deltaP / 1000.))
    print("velocity = {0:0.2f} m/s".format(my_pipe.velocity))
    print("Reynolds number = {0:0.2e}".format(my_pipe.Re))
    print("Friction factor = {0:0.5f}".format(my_pipe.f))


if __name__ == '__main__':
    main()
