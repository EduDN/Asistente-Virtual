import streamlit as st
from PyPDF2 import PdfReader

def read_pdf(file):
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def main():
    st.title("Asistente Virtual UPIICSA")
    st.title("Equipo 5 - Aplicaciones de Redes")
    st.write("Adjunta un archivo PDF y haz preguntas sobre él.")

    uploaded_file = st.file_uploader("Subir archivo PDF", type=["pdf"])

    if uploaded_file is not None:
        pdf_text = read_pdf(uploaded_file)
        st.write("Archivo cargado exitosamente.")

        st.subheader("Haz tu pregunta:")
        question = st.text_input("Pregunta:")

        if st.button("Enviar"):
            # Aquí podrías agregar la lógica para procesar la pregunta
            # y mostrar la respuesta correspondiente.
            st.write("Aquí iría la respuesta a la pregunta:", question)

if __name__ == "__main__":
    main()
