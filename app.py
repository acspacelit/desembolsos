import streamlit as st

# Diccionario para mapear las páginas
pages = {
    "Página Principal": "main",  # Suponiendo que tienes un script principal
    "Ejecutado vs Programado": "ejecutado_vs_programado"
}

def main():
    st.sidebar.title("Navegación")
    selection = st.sidebar.radio("Ir a:", list(pages.keys()))

    if selection == "Página Principal":
        # importa y ejecuta la función principal de ese script
        from main import main_function
        main_function()
    elif selection == "Ejecutado vs Programado":
        from Ejecutado_vs_Programado import main_function
        main_function()

if __name__ == "__main__":
    main()
