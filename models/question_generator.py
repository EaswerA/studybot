from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained('t5-small')
model = T5ForConditionalGeneration.from_pretrained('t5-small')

def generate_t5_question(context):
    input_text = f"generate question: {context}"
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    outputs = model.generate(input_ids, max_length=64)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

print(generate_template_question("photosynthesis"))
print(generate_t5_question("Photosynthesis is the process by which plants convert light energy..."))

