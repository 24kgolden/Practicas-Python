import tkinter as tk
from tkinter import ttk, messagebox
from abc import ABC, abstractmethod

# ===================== CLASE ABSTRACTA =====================

class Vehiculo(ABC):
    def __init__(self, placa, horas_parqueo, monto_factura):
        self._placa = placa
        self._horas_parqueo = horas_parqueo
        self._monto_factura = monto_factura
        self._vlr_parqueo = 0.0
        self._vlr_descuento = 0.0

    @abstractmethod
    def valor_parqueo(self):
        pass

    def valor_descuento(self):
        if 100 <= self._monto_factura <= 500:
            self._vlr_descuento = self._vlr_parqueo * 0.50
        elif 500 < self._monto_factura <= 1000:
            self._vlr_descuento = self._vlr_parqueo * 0.60
        elif self._monto_factura > 1000:
            self._vlr_descuento = self._vlr_parqueo * 0.70
        else:
            self._vlr_descuento = 0.0

    def factura(self):
        neto = self._vlr_parqueo - self._vlr_descuento
        return (f"Placa: {self._placa}\n"
                f"Horas de Parqueo: {self._horas_parqueo}\n"
                f"Valor Parqueo: ${self._vlr_parqueo:.2f}\n"
                f"Descuento: ${self._vlr_descuento:.2f}\n"
                f"Total a pagar: ${neto:.2f}")

# ===================== SUBCLASES =====================

class Carro(Vehiculo):
    def valor_parqueo(self):
        self._vlr_parqueo = self._horas_parqueo * 1.20

class Moto(Vehiculo):
    def valor_parqueo(self):
        self._vlr_parqueo = self._horas_parqueo * 1.20

# ===================== INTERFAZ GRÁFICA =====================

def calcular():
    try:
        placa = entrada_placa.get().strip()
        horas = int(entrada_horas.get())
        monto = float(entrada_factura.get())
        tipo = combo_tipo.get()

        if not placa:
            raise ValueError("Placa vacía")

        if tipo == "Carro":
            vehiculo = Carro(placa, horas, monto)
        else:
            vehiculo = Moto(placa, horas, monto)

        vehiculo.valor_parqueo()
        vehiculo.valor_descuento()
        resultado.set(vehiculo.factura())

    except ValueError:
        messagebox.showerror("Error", "Ingrese datos válidos en todos los campos.")

# ===================== VENTANA =====================

ventana = tk.Tk()
ventana.title("Parqueadero S.A. - Guayaquil")
ventana.geometry("400x400")
ventana.resizable(False, False)

# Entrada de datos
tk.Label(ventana, text="Placa:").pack()
entrada_placa = tk.Entry(ventana)
entrada_placa.pack()

tk.Label(ventana, text="Horas de Parqueo:").pack()
entrada_horas = tk.Entry(ventana)
entrada_horas.pack()

tk.Label(ventana, text="Monto de Factura ($):").pack()
entrada_factura = tk.Entry(ventana)
entrada_factura.pack()

tk.Label(ventana, text="Tipo de Vehículo:").pack()
combo_tipo = ttk.Combobox(ventana, values=["Carro", "Moto"])
combo_tipo.current(0)
combo_tipo.pack()

# Botón para calcular
tk.Button(ventana, text="Calcular Total a Pagar", command=calcular).pack(pady=10)

# Mostrar resultado
resultado = tk.StringVar()
tk.Label(ventana, textvariable=resultado, justify="left").pack(pady=10)

# Iniciar la ventana
ventana.mainloop()
