from transformers import BartTokenizer, BartForConditionalGeneration
import torch

# 1. Load Pretrained Model and Tokenizer
model_name = "facebook/bart-large-cnn"
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)

# 2. Input Text (You can change this)
text = """
The Transformers library by Hugging Face provides general-purpose architectures for Natural Language Understanding (NLU) and Natural Language Generation (NLG) with over 32+ pre-trained models in 100+ languages and deep interoperability between TensorFlow and PyTorch.
"""

# 3. Encode the input text into tokens
inputs = tokenizer.encode(text, return_tensors="pt", max_length=1024, truncation=True)

# 4. Generate Summary (can tune max_length and min_length)
summary_ids = model.generate(
    inputs,
    max_length=50,
    min_length=20,
    length_penalty=2.0,
    num_beams=4,
    early_stopping=True
)

# 5. Decode the tokens into human-readable text
summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

# 6. Print the result
print("Original Text:\n", text)
print("\n--- Summary ---\n", summary)
