from transformers import AutoTokenizer


MODEL_NAME = "google-bert/bert-base-multilingual-cased"

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_NAME
)


texts = [
    "Hello.",
    "I am learning Transformers.",
    "Today I am learning how tokenizers work in large language models.",
]


encoded = tokenizer(
    texts,
    padding=True,
    return_tensors="pt"
)


print("input_ids:")
print(encoded["input_ids"])

print("\nshape:")
print(encoded["input_ids"].shape)

print("\nattention_mask:")
print(encoded["attention_mask"])

encoded = tokenizer(
    texts,
    padding="max_length",
    max_length=20,
    return_tensors="pt"
)

print(encoded["input_ids"].shape)

long_text = (
    "Artificial intelligence is changing software development. "
    * 20
)


without_truncation = tokenizer(
    long_text
)

with_truncation = tokenizer(
    long_text,
    truncation=True,
    max_length=32
)


print(
    "Before:",
    len(without_truncation["input_ids"])
)

print(
    "After:",
    len(with_truncation["input_ids"])
)

full = tokenizer(
    long_text,
    add_special_tokens=False
)

truncated = tokenizer(
    long_text,
    add_special_tokens=False,
    truncation=True,
    max_length=32
)


full_tokens = tokenizer.convert_ids_to_tokens(
    full["input_ids"]
)

truncated_tokens = tokenizer.convert_ids_to_tokens(
    truncated["input_ids"]
)


print("\nFull token count:")
print(len(full_tokens))

print("\nTruncated token count:")
print(len(truncated_tokens))

print("\nLast 10 original tokens:")
print(full_tokens[-10:])

print("\nLast 10 retained tokens:")
print(truncated_tokens[-10:])