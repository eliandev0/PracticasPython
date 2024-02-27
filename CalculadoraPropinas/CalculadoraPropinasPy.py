import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class CalculadoraPropinas:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Propinas")

        # Variables para almacenar los valores
        self.importe_factura = tk.DoubleVar()
        self.porcentaje_propina = tk.StringVar()
        self.importe_propina = tk.DoubleVar()
        self.importe_total = tk.DoubleVar()

        # Crear widgets
        ttk.Label(root, text="Importe factura").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.entry_factura = ttk.Entry(root, textvariable=self.importe_factura)
        self.entry_factura.grid(row=0, column=1, padx=10, sticky="ew", pady=5)


        ttk.Label(root, text="Porcentaje propina (%)").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.combo_porcentaje = ttk.Combobox(root, textvariable=self.porcentaje_propina, state="readonly")
        self.combo_porcentaje['values'] = ["Seleccione porcentaje","5", "10", "15", "20", "25", "30", "40", "50"]
        self.combo_porcentaje.grid(row=1, column=1, padx=10, pady=5)
        self.combo_porcentaje.current(0)

        ttk.Label(root, text="Importe propina").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.label_propina = ttk.Label(root, textvariable=self.importe_propina)
        self.label_propina.grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(root, text="Factura total").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.label_total = ttk.Label(root, textvariable=self.importe_total)
        self.label_total.grid(row=3, column=1, padx=10, pady=5)

        ttk.Button(root, text="Calcular", command=self.calcular_propina_total).grid(row=4, column=0, columnspan=2, padx=10, pady=5)
        ttk.Button(root, text="Nueva Factura", command=self.limpiar_campos).grid(row=5, column=0, columnspan=2, padx=10, pady=5)

    def calcular_propina_total(self):
        try:
            importe_factura = float(self.importe_factura.get())

            if self.porcentaje_propina.get() and int(self.porcentaje_propina.get()) > 0:
                porcentaje = int(self.porcentaje_propina.get())
                importe_propina = importe_factura * porcentaje / 100.0
                importe_total = importe_factura + importe_propina
                self.importe_propina.set("{:.2f}".format(importe_propina))
                self.importe_total.set("{:.2f}".format(importe_total))
            else:
                messagebox.showwarning("Advertencia", "Seleccione un porcentaje de propina válido.")
                self.importe_propina.set("")
                self.importe_total.set("")

        except ValueError:
            messagebox.showerror("Error", "Complete los campos vacios.")

    def limpiar_campos(self):
        self.importe_factura.set("0.0")
        self.porcentaje_propina.set("Seleccione porcentaje")
        self.importe_propina.set("0.0")
        self.importe_total.set("0.0")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraPropinas(root)
    root.mainloop()
