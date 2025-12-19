import customtkinter as ctk

# --- CONFIGURACIÓN INICIAL ---
ctk.set_appearance_mode("dark") 
# No necesitamos theme "blue" porque vamos a personalizar todo a mano

# Definimos los colores oficiales para usarlos fácil
VAL_BG = "#0f1923"      # Fondo oscuro
VAL_RED = "#ff4655"     # Rojo intenso
VAL_TEXT = "#ece8e1"    # Blanco hueso

app = ctk.CTk()
app.geometry("400x350")
app.title("Valorant Tracker")
app.configure(fg_color=VAL_BG) # Pintamos la ventana del color oscuro

# --- ELEMENTOS VISUALES ---

# 1. Título (Usamos fuente Impact que se parece a la del juego)
titulo = ctk.CTkLabel(
    app, 
    text="VALORANT TRACKER", 
    font=("Impact", 28),     # Fuente grande y gruesa
    text_color=VAL_RED       # Título en Rojo
)
titulo.pack(pady=(40, 20))   # Un poco de aire arriba

# 2. Caja de Texto (Input)
entrada = ctk.CTkEntry(
    app, 
    placeholder_text="Nombre#Tag",
    width=220,
    height=40,
    fg_color="#1f2b36",      # Un gris un poco más claro que el fondo
    border_color=VAL_TEXT,   # Borde claro
    border_width=1,
    text_color="white",
    corner_radius=0          # Bordes cuadrados (Estilo Valorant)
)
entrada.pack(pady=10)

# 3. Función temporal
def buscar():
    print("🎯 Iniciando búsqueda táctica...")

# 4. Botón de Acción
boton = ctk.CTkButton(
    app, 
    text="BUSCAR AGENTE",
    font=("Arial", 14, "bold"),
    fg_color=VAL_RED,        # Botón Rojo
    hover_color="#bd353f",   # Rojo más oscuro al pasar el mouse
    text_color="white",
    width=220,
    height=40,
    corner_radius=0,         # Botón cuadrado
    command=buscar
)
boton.pack(pady=20)

# 5. Pie de página
footer = ctk.CTkLabel(
    app,
    text="Desarrollado por NecrogesZ",
    font=("Arial", 10),
    text_color="gray"
)
footer.pack(side="bottom", pady=10)

# --- EJECUTAR ---
app.mainloop()