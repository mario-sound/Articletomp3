import tkinter as tk
from tkinter import messagebox, ttk, filedialog
import nltk_tool as nltk_tool
import gtts_tool as gtts_tool
import threading

class ArticleToMP3App:
    def __init__(self, root):
        """
        Inicializa la aplicación de conversión de artículos a MP3.
        """

        self.root = root
        self.root.title("Article to MP3 Converter")

        # URL Entry
        self.url_label = tk.Label(root, text="Introduce la URL del artículo:")
        self.url_label.pack(pady=5)
        self.url_entry = tk.Entry(root, width=50)
        self.url_entry.pack(pady=5)

        # Ratio Entry
        self.ratio_label = tk.Label(root, text="Ratio de reproducción (por ejemplo, 1.2 para 20% más rápido):")
        self.ratio_label.pack(pady=5)
        self.ratio_entry = tk.Entry(root, width=10)
        self.ratio_entry.pack(pady=5)
        self.ratio_entry.insert(0, '1.2')  # Valor predeterminado

        # Botones
        self.convert_button = tk.Button(root, text="Convertir a MP3", command=self.start_conversion)
        self.convert_button.pack(pady=10)

        self.cancel_button = tk.Button(root, text="Cancelar", command=self.cancel_conversion, state=tk.DISABLED)
        self.cancel_button.pack(pady=5)

        # Barra de progreso
        self.progress_bar = ttk.Progressbar(root, orient=tk.HORIZONTAL, length=300, mode='determinate')
        self.progress_bar.pack()

        # Hilo de conversión
        self.conversion_thread = None

        # Barra de estado
        self.status_bar = ttk.Label(root, text="Listo para convertir.", relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def start_conversion(self):
        """
        Inicia el proceso de conversión en un hilo separado.
        """

        url = self.url_entry.get()
        speed_factor = self.ratio_entry.get()

        if not url:
            messagebox.showerror("Error", "Por favor, introduzca una URL.")
            return

        try:
            speed_factor = float(speed_factor)
        except ValueError:
            messagebox.showerror("Error", "El valor del ratio de velocidad debe ser un número.")
            return

        # Pedir al usuario que seleccione la carpeta de destino
        save_path = filedialog.askdirectory(title="Seleccionar carpeta de destino")
        if not save_path:  # El usuario canceló la selección
            return

        self.convert_button.config(state=tk.DISABLED)
        self.cancel_button.config(state=tk.NORMAL)
        self.progress_bar['value'] = 0
        self.status_bar.config(text="Convirtiendo...")

        self.conversion_thread = threading.Thread(target=self.convert_to_mp3, args=(url, speed_factor, save_path))
        self.conversion_thread.start()

    def convert_to_mp3(self, url, speed_factor, save_path):
        """
        Realiza la conversión del artículo a MP3.
        """

        try:
            # Formatear el texto 
            text = nltk_tool.format_text(url)

            if text.startswith("Error"):
                messagebox.showerror("Error", text)
                self.reset_ui()
                return

            # Convertir a MP3 
            gtts_tool.convert_text_to_mp3(text, speed_factor=speed_factor, save_path=save_path)

            self.progress_bar['value'] = 100 
            messagebox.showinfo("Éxito", "Conversión completada exitosamente.")
            self.status_bar.config(text="Conversión completada exitosamente.") 

        except Exception as e:
            self.status_bar.config(text=f"Error: {e}") 
        finally:
            self.reset_ui()

    def cancel_conversion(self):
        """
        Intenta cancelar el proceso de conversión si está en ejecución.
        """

        if self.conversion_thread and self.conversion_thread.is_alive():
            # Intenta detener el hilo 
            self.conversion_thread.join(timeout=1)  
            self.reset_ui()
            messagebox.showinfo("Cancelado", "La conversión ha sido cancelada.")
            self.status_bar.config(text="Conversión cancelada.") 

    def reset_ui(self):
        """
        Restablece la interfaz de usuario a su estado inicial.
        """

        self.convert_button.config(state=tk.NORMAL)
        self.cancel_button.config(state=tk.DISABLED)
        self.progress_bar['value'] = 0
        self.status_bar.config(text="Listo para convertir.") 


# Crear la ventana principal
if __name__ == "__main__":
    root = tk.Tk()
    app = ArticleToMP3App(root)
    root.mainloop()