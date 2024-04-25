import streamlit as st
import openai

# Set your OpenAI API key here
openai.api_key = 'sk-proj-sHLNZSy43TmxXgKgMJaHT3BlbkFJtouoJQDVAdCVOr8LW6JG'

# Función para cargar archivo PDF y hacer preguntas
def cargar_pdf_y_hacer_preguntas(archivo, preguntas):
    # Aquí iría la lógica para procesar el PDF y hacer preguntas
    # Por ahora, simplemente mostramos un mensaje de éxito
    st.success(f'Se cargó el archivo PDF: {archivo.name}')
    st.write("Aquí puedes hacer preguntas sobre el PDF cargado.")

    # Mostrar preguntas y respuestas
    for pregunta in preguntas:
        st.write(f"Pregunta: {pregunta}")
        respuesta = obtener_respuesta_openai(pregunta)
        st.write("Respuesta:", respuesta)

# Función para obtener respuesta de OpenAI
def obtener_respuesta_openai(pregunta):
    # Llamar a la API de OpenAI para obtener la respuesta
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",  # Utilizar el modelo 'text-davinci-002'
        prompt=pregunta,
        temperature=0.5,
        max_tokens=100
    )
    return response.choices[0].text.strip()

def main():
    st.title("ASISTENTE VIRTUAL UPIICSA")
    st.title("EQUIPO 5 - APLICACIONES DE REDESS")

    archivo = st.file_uploader("Selecciona un archivo PDF", type="pdf")

    if archivo is not None:
        preguntas = st.text_input("Haz tu pregunta:")
        if preguntas:
            preguntas = preguntas.split(";")
            cargar_pdf_y_hacer_preguntas(archivo, preguntas)

if __name__ == "__main__":
    main()
