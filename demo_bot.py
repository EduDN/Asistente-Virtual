import streamlit as st

# Función para cargar archivo PDF y hacer preguntas
def cargar_pdf_y_hacer_preguntas(archivo, preguntas):
    # Aquí iría la lógica para procesar el PDF y hacer preguntas
    # Por ahora, simplemente mostramos un mensaje de éxito
    st.success(f'Se cargó el archivo PDF: {archivo.name}')
    st.write("Aquí puedes hacer preguntas sobre el PDF cargado.")

    # Mostrar preguntas y respuestas
    for pregunta in preguntas:
        st.write(f"Pregunta: {pregunta}")
        st.write("Respuesta: Aquí iría la respuesta correspondiente")

def main():
    st.title("ASISTENTE VIRTUAL UPIICSA")
    st.title("EQUIPO 5 - APLICACIONES DE REDES")

    archivo = st.file_uploader("Selecciona un archivo PDF", type="pdf")

    if archivo is not None:
        preguntas = st.text_input("Haz tu pregunta:")
        if preguntas:
            preguntas = preguntas.split(";")
            cargar_pdf_y_hacer_preguntas(archivo, preguntas)

if __name__ == "__main__":
    main()
