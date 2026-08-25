from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained(
    "gpt2"
)

text = "I love machine learning"

encoding = tokenizer(
    text,
    add_special_tokens=False
)

input_ids = encoding["input_ids"]

tokens = tokenizer.convert_ids_to_tokens(
    input_ids
)


print("Text:")
print(text)

print("\nTokens:")
print(tokens)

print("\nInput IDs:")
print(input_ids)

print("\nNext-token prediction")
print("=" * 60)


for i in range(len(tokens) - 1):

    context = tokens[: i + 1]

    target = tokens[i + 1]

    print(
        f"{context} -> {target}"
    )


inputs = input_ids[:-1]

labels = input_ids[1:]


print("Inputs:")
print(inputs)

print("Labels:")
print(labels)