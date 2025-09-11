import google.generativeai as genai
import os

# Configure a chave da API: defina GEMINI_API_KEY como variável de ambiente
genai.configure(api_key=os.environ[""])

def get_car_ai_bio(model, brand, year):
    prompt = f"Crie uma descrição detalhada para um carro da marca {brand}, modelo {model}, ano {year}. A descrição deve incluir características, desempenho, conforto e tecnologia."
    model_gemini = genai.GenerativeModel("gemini-1.5-flash")
    response = model_gemini.generate_content(prompt)
    return response.text
