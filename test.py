import google.generativeai as genai

genai.configure(api_key="AIzaSyAXWIcGQsd6HYKH3BZYgkzBXG9i9-mOlMw")

models = genai.list_models()

for model in models:
    print(f"{model.name} -> {model.supported_generation_methods}")
