import openai

openai.api_key="sk-4rTQfabgEe6tRYpnqqspBo8QtK6fPEfGrMtJ02ECEmT3BlbkFJqusFw8cdUjgJ4cej-R5rJEePSO2aHbz0_d3w3gGH0A"

def get_fertilizers_recommendations(crop, nitrogen, phosphorus, potassium, soil_ph, symptoms):
    #Prompt is a natural language request pass to a model To get a desired outcome as a response
    prompt = f"""
    Crop: {crop}
    Soil Nutrients - Nitrogen: {nitrogen}, Phosphorus: {phosphorus}, Potassium: {potassium}, pH: {soil_ph}
    Observed Symptoms: {symptoms}

    Based on the above details, suggest:
    - Best organic and chemical fertilizers with reasons.
    - Any required pesticides if disease is detected.
    - When and how to apply fertilizers for best results.
    """
    #model defination
    '''
    Model Info:
    model_name=Chat-GPT-4
    api=openai api
    '''

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response["choices"][0]["message"]["content"]

# Example Usage
print(get_fertilizers_recommendations("Rice", 50, 40, 30, 6.5, "Yellowing of leaves"))

