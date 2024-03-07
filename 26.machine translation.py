from transformers import MarianMTModel, MarianTokenizer
def translate_text(input_text, model_name='Helsinki-NLP/opus-mt-en-fr'):
    model = MarianMTModel.from_pretrained(model_name)
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids
    translation_ids = model.generate(input_ids)
    translated_text = tokenizer.decode(translation_ids[0], skip_special_tokens=True)
    return translated_text
def main():
    english_text = "Hello, how are you? This is a sample translation program."
    french_translation = translate_text(english_text)
    print(f"English Text: {english_text}")
    print(f"French Translation: {french_translation}")
if __name__ == "__main__":
    main()
