import openai

def send_message(request):
    request_json = request.get_json(silent=True)
    if request_json and 'prompt' in request_json:
        prompt = request_json['prompt']

        # Set up the OpenAI API client
        openai.api_key = "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"

        # Set the desired model and parameters
        model = "text-davinci-002"
        max_tokens = 2048
        temperature = 0.5

        # Print the received prompt to the console (for debugging)
        print("Received prompt:", prompt)

        # Make a request to the OpenAI API
        response = openai.Completion.create(
            engine=model,
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        # Print the response from the OpenAI API to the console (for debugging)
        print("Response from OpenAI API:", response)

        return response.choices[0].text
    else:
        return "Error: No prompt received"
