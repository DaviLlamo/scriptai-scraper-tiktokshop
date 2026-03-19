from google import genai

client = genai.Client(api_key="chaveapiakiiii!!!!")


def gerar_resposta(prompt):
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )

    return response.text