from transformers import pipeline

class QuestionGenerator:
    def __init__(self, model_name="facebook/bart-large-cnn"):
        self.generator = pipeline("text2text-generation", model=model_name)

    def generate_question(self, context):
        prompt = f"Generate a quiz question from this text:\n{context}"
        result = self.generator(prompt, max_length=50, num_return_sequences=1)
        return result[0]['generated_text']

