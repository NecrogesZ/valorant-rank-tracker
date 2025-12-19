import customtkinter as ctk
from tracker import obtener_rango 

# --- CONFIGURACIÓN INICIAL ---
ctk.set_appearance_mode("dark") 
VAL_BG = "#0f1923"
VAL_RED = "#ff4655"
VAL_TEXT = "#ece8e1"

app = ctk.CTk()
app.geometry("400x450")
app.title("Valorant Tracker")
app.configure(fg_color=VAL_BG)

# --- ELEMENTOS VISUALES (UI) ---

# 1. Título
titulo = ctk.CTkLabel(app, text="VALORANT TRACKER", font=("Impact", 28), text_color=VAL_RED)
titulo.pack(pady=(40, 20))

# 2. Caja de Texto
entrada = ctk.CTkEntry(app, placeholder_text="Nombre#Tag", width=220, height=40,
                       fg_color="#1f2b36", border_color=VAL_TEXT, border_width=1,
                       text_color="white", corner_radius=0)
entrada.pack(pady=10)

# 3. Etiqueta de Resultado
# Aquí es donde aparecerá el rango. Empieza vacía.
etiqueta_resultado = ctk.CTkLabel(app, text="", font=("Arial", 18), text_color=VAL_TEXT)
etiqueta_resultado.pack(pady=10)

# --- LÓGICA (La Función) ---
def buscar():
    texto_usuario = entrada.get()

    try: # <--- Faltaban los dos puntos aquí
        nombre, tag = texto_usuario.split("#")

        # Feedback visual
        etiqueta_resultado.configure(text="⏳ Conectando...", text_color="yellow")
        app.update() 
        
        # Llamada a la API
        respuesta = obtener_rango(nombre, tag)
        
        # Mostrar resultado
        etiqueta_resultado.configure(text=respuesta, text_color=VAL_TEXT)

    except ValueError:
        etiqueta_resultado.configure(text="❌ Error: Falta el Tag (#)", text_color="red")

# --- BOTÓN DE ACCIÓN ---
boton = ctk.CTkButton(app, text="BUSCAR AGENTE", font=("Arial", 14, "bold"),
                      fg_color=VAL_RED, hover_color="#bd353f", text_color="white",
                      width=220, height=40, corner_radius=0, 
                      command=buscar)
boton.pack(pady=20)

# 5. Pie de página
footer = ctk.CTkLabel(app, text="Desarrollado por NecrogesZ", font=("Arial", 10), text_color="gray")
footer.pack(side="bottom", pady=10)

# --- EJECUTAR ---
app.mainloop()