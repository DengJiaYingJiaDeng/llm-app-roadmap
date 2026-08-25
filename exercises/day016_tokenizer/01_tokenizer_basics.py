
import os
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"
from transformers import AutoTokenizer

MODEL_NAME = "google-bert/bert-base-multilingual-cased"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)



# print("Tokenizer class:")
# print(type(tokenizer))

# print("\nVocab size:")
# print(tokenizer.vocab_size)

# print("\nModel max length:")
# print(tokenizer.model_max_length)

# print("\nSpecial tokens:")
# print(tokenizer.special_tokens_map)

# text = "I am learning PyTorch and Transformers."

# tokens = tokenizer.tokenize(text)

# print("\nOriginal text:")
# print(text)

# print("\nTokens:")
# print(tokens)

# print("\nToken count:")
# print(len(tokens))

# texts = [
#     "我正在学习大语言模型",
#     "人工智能正在改变软件开发",
#     "今天学习Tokenizer",
#     "PyTorch非常好用",
# ]

# for text in texts:
#     tokens = tokenizer.tokenize(text)

#     print("\n==========================")
#     print("Text:", text)
#     print("Tokens:", tokens)
#     print("Characters:", len(text))
#     print("Tokens:", len(tokens))


# text = "I love machine learning."

# encoding = tokenizer(text)

# print("\nEncoding:")
# print(encoding)

# print("\nInput IDs:")
# print(encoding["input_ids"])

# print("\nTokens from IDs:")
# print(
#     tokenizer.convert_ids_to_tokens(
#         encoding["input_ids"]
#     )
# )


# print("CLS:", tokenizer.cls_token)
# print("SEP:", tokenizer.sep_token)
# print("PAD:", tokenizer.pad_token)
# print("UNK:", tokenizer.unk_token)
# print("MASK:", tokenizer.mask_token)


text = "Hello world"

tokens = tokenizer.tokenize(text)
encoding = tokenizer(text)

print("tokens:", tokens)
print("token count:", len(tokens))

print(
    "input tokens:",
    tokenizer.convert_ids_to_tokens(
        encoding["input_ids"]
    )
)

print(
    "input_ids length:",
    len(encoding["input_ids"])
)