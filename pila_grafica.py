import tkinter as tk
from tkinter import messagebox

class PilaGrafica:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualizador de Pila (LIFO)")
        self.root.geometry("350x450")
        
        self.pila = []
        self.max_elementos = 8
        
        frame_controles = tk.Frame(root)
        frame_controles.pack(pady=15)
        
        self.entry_valor = tk.Entry(frame_controles, width=10, font=("Arial", 12))
        self.entry_valor.grid(row=0, column=0, padx=5)
        
        btn_apilar = tk.Button(frame_controles, text="Apilar (Push)", 
                               command=self.apilar, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
        btn_apilar.grid(row=0, column=1, padx=5)
        
        btn_desapilar = tk.Button(frame_controles, text="Desapilar (Pop)", 
                                  command=self.desapilar, bg="#F44336", fg="white", font=("Arial", 10, "bold"))
        btn_desapilar.grid(row=0, column=2, padx=5)
        
        self.canvas = tk.Canvas(root, width=250, height=350, bg="white", relief=tk.SUNKEN, bd=2)
        self.canvas.pack()
        
        self.dibujar_contenedor()

    def dibujar_contenedor(self):
        self.canvas.create_line(30, 20, 30, 330, width=4, fill="#333")
        self.canvas.create_line(30, 330, 220, 330, width=4, fill="#333")
        self.canvas.create_line(220, 330, 220, 20, width=4, fill="#333")

    def actualizar_pila(self):
        self.canvas.delete("elemento") 
        
        x0, x1 = 40, 210
        y_base = 325
        alto_elemento = 35
        
        for i, valor in enumerate(self.pila):
            y1 = y_base - (i * alto_elemento)
            y0 = y1 - alto_elemento + 5
            
            self.canvas.create_rectangle(x0, y0, x1, y1, fill="#8BC34A", outline="black", width=2, tags="elemento")
            self.canvas.create_text((x0+x1)//2, (y0+y1)//2, text=str(valor), font=("Arial", 12, "bold"), tags="elemento")

    def apilar(self):
        valor = self.entry_valor.get()
        if not valor:
            messagebox.showwarning("Advertencia", "Por favor, ingresa un valor.")
            return
            
        if len(self.pila) >= self.max_elementos:
            messagebox.showerror("Error", "Desbordamiento (Stack Overflow): La pila está llena.")
            return
            
        self.pila.append(valor)
        self.entry_valor.delete(0, tk.END)
        self.actualizar_pila()

    def desapilar(self):
        if len(self.pila) == 0:
            messagebox.showerror("Error", "Subdesbordamiento (Stack Underflow): La pila está vacía.")
            return
            
        valor = self.pila.pop()
        self.actualizar_pila()
        messagebox.showinfo("Acción Pop", f"Elemento retirado: {valor}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PilaGrafica(root)
    root.mainloop()