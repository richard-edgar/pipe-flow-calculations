import math


class Pipe:
    def __init__(
            self, internal_diameter, roughness, length, density, viscosity,
            flowrate):
        self.int_dia = internal_diameter
        self.roughness = roughness
        self.length = length
        self.density = density
        self.viscosity = viscosity
        self.flowrate = flowrate
        self.velocity = 0
        self.Re = 0
        self.f = 0
        self.deltaP = 0

    def update(self):
        area = math.pi*self.int_dia**2/4
        self.velocity = self.flowrate/area
        self.Re = self.int_dia*self.density*self.velocity/self.viscosity
        rel_rough = self.roughness/self.int_dia/3.7
        f = 1.0
        for i in range(1000):
            fnew = (1/(-2*math.log10(rel_rough+2.51/self.Re/math.sqrt(f))))**2
            if abs(fnew-f) < 0.00001:
                break
            f = fnew
        self.f = fnew
        self.deltaP = self.velocity**2*(
            self.f*self.length/self.int_dia)*self.density/2

    def int_dia_set(self, internal_diameter):
        self.int_dia = internal_diameter

    def roughness_set(self, roughness):
        self.roughness = roughness

    def length_set(self, length):
        self.length = length

    def density_set(self, density):
        self.density = density

    def viscosity_set(self, viscosity):
        self.viscosity = viscosity

    def flowrate_set(self, flowrate):
        self.flowrate = flowrate


def main():
    my_pipe = Pipe(0.100, 0.00005, 100, 1000, 0.001, 0.014)
    my_pipe.update()
    print("Pipe pressure loss = {0:0.1f} kPa".format(my_pipe.deltaP/1000.))
    print("velocity = {0:0.1f} m/s".format(my_pipe.velocity))
    print("Reynolds number = {0:0.2e}".format(my_pipe.Re))
    print("Friction factor = {0:0.5f}".format(my_pipe.f))


if __name__ == '__main__':
    main()
