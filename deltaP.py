import tkinter as tk
from tkinter import ttk
import mypipe

"""
This program calculates the pipe pressure loss for incompressible,
Newtonian flow.
"""


class InputScreen:

    def __init__(self, root):

        # Main Window

        self.root = root
        self.root.title("Incompressible deltaP Newtonian")
        self.root.geometry("+250+300")
        self.mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=("N", "W", "E", "S"))
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)

        # Pipe data

        self.dia_int = tk.StringVar()
        self.roughness = tk.StringVar()
        self.length = tk.StringVar()
        self.P1 = tk.StringVar()
        self.P1.set(0)

        # Fluid data

        self.density = tk.StringVar()
        self.viscosity = tk.StringVar()
        self.flowrate = tk.StringVar()

        # Entry internal diameter

        rowvar = 1
        self.dia_entry = ttk.Entry(self.mainframe, width=15,
                                   textvariable=self.dia_int)
        self.dia_entry.grid(column=2, row=rowvar, sticky=("W", "E"))
        self.dia_label1 = ttk.Label(self.mainframe, text="Pipe internal diameter:")
        self.dia_label1.grid(column=1, row=rowvar, sticky=("W", "E"))
        self.dia_label2 = ttk.Label(self.mainframe, text="mm")
        self.dia_label2.grid(column=3, row=rowvar, sticky=("W", "E"))

        # Entry roughness

        rowvar += 1
        self.roughness.set(0.046)  # default
        self.roughness_entry = ttk.Entry(self.mainframe, width=15, textvariable=self.roughness)
        self.roughness_entry.grid(column=2, row=rowvar, sticky=("W", "E"))
        self.roughness_label1 = ttk.Label(self.mainframe, text="Pipe absolute roughness").grid(column=1, row=rowvar, sticky=("W", "E"))
        self.roughness_label2 = ttk.Label(self.mainframe, text="mm").grid(column=3, row=rowvar, sticky=("W", "E"))

        # Entry length

        rowvar += 1
        self.length_entry = ttk.Entry(self.mainframe, width=15, textvariable=self.length)
        self.length_entry.grid(column=2, row=rowvar, sticky=("W", "E"))
        self.length_label1 = ttk.Label(self.mainframe, text="Pipe length").grid(column=1, row=rowvar, sticky=("W", "E"))
        self.length_label2 = ttk.Label(self.mainframe, text="m").grid(column=3, row=rowvar, sticky=("W", "E"))

        # Entry fluid density

        rowvar += 1
        self.density_entry = ttk.Entry(self.mainframe, width=15, textvariable=self.density)
        self.density_entry.grid(column=2, row=rowvar, sticky=("W", "E"))
        self.density_label1 = ttk.Label(self.mainframe, text="Fluid density").grid(column=1, row=rowvar, sticky=("W", "E"))
        self.density_label2 = ttk.Label(self.mainframe, text="kg/m3").grid(column=3, row=rowvar, sticky=("W", "E"))

        # Entry viscosity

        rowvar += 1
        self.viscosity_entry = ttk.Entry(self.mainframe, width=15, textvariable=self.viscosity)
        self.viscosity_entry.grid(column=2, row=rowvar, sticky=("W", "E"))
        self.viscosity_label1 = ttk.Label(self.mainframe, text="Fluid viscosity").grid(column=1, row=rowvar, sticky=("W", "E"))
        self.viscosity_label2 = ttk.Label(self.mainframe, text="cP").grid(column=3, row=rowvar, sticky=("W", "E"))

        # Entry flow rate

        rowvar += 1
        self.flowrate_entry = ttk.Entry(self.mainframe, width=15, textvariable=self.flowrate)
        self.flowrate_entry.grid(column=2, row=rowvar, sticky=("W", "E"))
        self.flowrate_label1 = ttk.Label(self.mainframe, text="Flow rate").grid(column=1, row=rowvar, sticky=("W", "E"))
        self.flowrate_label2 = ttk.Label(self.mainframe, text="m3/h").grid(column=3, row=rowvar, sticky=("W", "E"))

        # upstream pressure

        rowvar += 1
        self.P1_label = ttk.Entry(self.mainframe, width=15, textvariable=self.P1)
        self.P1_label.grid(column=2, row=rowvar, sticky=("W", "E"))
        self.P1_label1 = ttk.Label(self.mainframe,  text="Pressure upstream").grid(column=1, row=rowvar, sticky=("W", "E"))
        self.P1_label2 = ttk.Label(self.mainframe,  text="kPag").grid(column=3, row=rowvar, sticky=("W", "E"))

        # Execute calculation

        rowvar += 1
        ttk.Button(self.mainframe, text="Calculate",
                   command=lambda: self.calculate()).grid(column=2, row=rowvar, sticky="W")

        # Labels to contain programme outputs

        # output deltaP

        rowvar += 1
        self.deltaP = tk.StringVar()
        self.deltaP_label = ttk.Label(self.mainframe, width=10, textvariable=self.deltaP)
        self.deltaP_label.grid(column=2, row=rowvar, sticky=("W", "E"))
        self.deltaP_label1 = ttk.Label(self.mainframe, text="Pressure drop").grid(column=1, row=rowvar, sticky=("W", "E"))
        self.deltaP_label2 = ttk.Label(self.mainframe, text="kPa").grid(column=3, row=rowvar, sticky=("W", "E"))

        # downstream pressure

        rowvar += 1
        self.P2 = tk.StringVar()
        self.P2_label = ttk.Label(self.mainframe, width=10, textvariable=self.P2)
        self.P2_label.grid(column=2, row=rowvar, sticky=("W", "E"))
        self.P2_label1 = ttk.Label(self.mainframe,  text="Pressure downstream").grid(column=1, row=rowvar, sticky=("W", "E"))
        self.P2_label2 = ttk.Label(self.mainframe,  text="kPag").grid(column=3, row=rowvar, sticky=("W", "E"))

        # velocity

        rowvar += 1
        self.v = tk.StringVar()
        self.v_label = ttk.Label(self.mainframe, width=10,  textvariable=self.v)
        self.v_label.grid(column=2,  row=rowvar,  sticky=("W", "E"))
        self.v_label1 = ttk.Label(self.mainframe, text="Velocity").grid(column=1, row=rowvar, sticky=("W", "E"))
        self.v_label2 = ttk.Label(self.mainframe,  text="m/s").grid(column=3,  row=rowvar,  sticky=("W", "E"))

        # Reynolds Number

        rowvar += 1
        self.NRe = tk.StringVar()
        self.NRe_label = ttk.Label(self.mainframe, width=12, textvariable=self.NRe)
        self.NRe_label.grid(column=2, row=rowvar, sticky=("W", "E"))
        self.NRe_label1 = ttk.Label(self.mainframe, text="Reynolds no.").grid(column=1, row=rowvar, sticky=("W", "E"))

        # friction factor

        rowvar += 1
        self.f_darcy = tk.StringVar()
        self.f_darcy_label = ttk.Label(self.mainframe, width=10, textvariable=self.f_darcy)
        self.f_darcy_label.grid(column=2, row=rowvar, sticky=("W", "E"))
        self.f_darcy_label1 = ttk.Label(self.mainframe,  text="Friction Factor").grid(column=1, row=rowvar, sticky=("W", "E"))

        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        self.dia_entry.focus()
        self.root.bind('<Return>', lambda x: self.calculate())

    def deltaPset(self, dp):
        dp = '{:0.2f}'.format(dp)
        self.deltaP.set(dp)

    def NReset(self, NRe):
        NRe = '{:0.2e}'.format(NRe)
        self.NRe.set(NRe)

    def velocityset(self, v):
        v = '{:0.2f}'.format(v)
        self.v.set(v)

    def f_darcyset(self, darcy):
        darcy = '{:0.5f}'.format(darcy)
        self.f_darcy.set(darcy)

    def P2set(self, P2):
        P2 = '{:0.2f}'.format(P2)
        self.P2.set(P2)

    def calculate(self):
        try:
            dia_int = check_inputs(self.dia_int) / 1000.
            length = check_inputs(self.length)
            roughness = check_inputs(self.roughness) / 1000.
            density = check_inputs(self.density)
            viscosity = check_inputs(self.viscosity) / 1000.
            flowrate = check_inputs(self.flowrate) / 3600.
        except TypeError:
            return
        my_fluid = mypipe.Fluid(density, viscosity)
        my_pipe = mypipe.Pipe(dia_int, roughness, length, my_fluid)
        my_pipe.update(my_fluid, flowrate)
        self.deltaPset(my_pipe.deltaP / 1000.)
        self.velocityset(my_pipe.velocity)
        self.f_darcyset(my_pipe.f)
        self.NReset(my_pipe.Re)
        self.P2set(float(self.P1.get()) - my_pipe.deltaP / 1000.)


def check_inputs(var):
    try:
        a = float(var.get())
        return a
    except ValueError:
        var.set('enter a number')


def main():
    root = tk.Tk()
    InputScreen(root)
    root.mainloop()

# Main programme


if __name__ == '__main__':
    main()
