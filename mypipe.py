import math


class Pipe:

    def __init__(self, internal_diameter, roughness, length):
        self.int_dia = internal_diameter
        self.roughness = roughness
        self.length = length
        self.rel_rough = self.roughness / self.int_dia

class Fluid:

    def __init__(self, density, viscosity):
        self.density = density
        self.viscosity = viscosity


class Flow:

    def __init__(self, pipe, fluid, flowrate):
        self.pipe = pipe
        self.fluid = fluid
        self.flowrate = flowrate
        self.v = self.velocity()
        self.NRe = self.reynolds()
        self.darcy = self.f_darcy()
        self.rel_rough = self.pipe.roughness / self.pipe.int_dia
        self.deltaP = self.v ** 2\
            * (self.darcy * self.pipe.length / self.pipe.int_dia) * self.fluid.density / 2


    def f_darcy(self):
        f = 1.0
        for i in range(1000):
            fnew = (1/(-2 * math.log10(self.pipe.rel_rough / 3.7 + 2.51
                    / self.NRe / math.sqrt(f)))) ** 2
            if abs(fnew-f) < 0.00001 or i == 999:
                break
            if i != 999:
                f = fnew
            else:
                f = i
        return fnew

    def velocity(self):
        area = math.pi * self.pipe.int_dia ** 2 / 4
        return self.flowrate / area

    def reynolds(self):
        return self.pipe.int_dia * self.v\
                  * self.fluid.density / self.fluid.viscosity


def get_input(varname, test, message):
    returnval = -1
    while test(returnval):
        try:
            returnval = float(input("Enter {0}: ".format(varname)))
        except ValueError:
            print("Input a valid number")
        if test(returnval):
            print(message)
    return returnval


def main():

    density = get_input("fluid density (kg/m3)", lambda x: x <= 0, "may not be zero or less")
    viscosity = get_input("viscosity (centipoise)", lambda x: x <= 0, "may not be zero or less") / 1000.
    int_dia = get_input("pipe internal diameter (mm)", lambda x: x <= 0, "may not be zero or less") / 1000.
    roughness = get_input("pipe roughness (mm)", lambda x: x < 0, "may not be less than zero") / 1000.
    length = get_input("pipe length (m)", lambda x: x < 0, "may not be less than zero")
    flowrate = get_input("fluid flow rate (m3/h)", lambda x: x <= 0, "may not be zero or less") / 3600.
    my_fluid = Fluid(density, viscosity)
    my_pipe = Pipe(int_dia, roughness, length)
    my_flow = Flow(my_pipe, my_fluid, flowrate)
    print("Pipe pressure loss = {0:0.1f} kPa".format(my_flow.deltaP / 1000.))
    print("velocity = {0:0.2f} m/s".format(my_flow.v))
    print("Reynolds number = {0:0.2e}".format(my_flow.NRe))
    print("Friction factor = {0:0.5f}".format(my_flow.darcy))


if __name__ == '__main__':
    main()
