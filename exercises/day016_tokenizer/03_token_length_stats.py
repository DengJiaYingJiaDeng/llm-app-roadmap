from transformers import AutoTokenizer


MODEL_NAME = "google-bert/bert-base-multilingual-cased"

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_NAME
)


texts = [
    "Hello world.",
    "I am learning PyTorch.",
    "I am learning tokenization for large language models.",
    "你好世界。",
    "我正在学习大语言模型。",
    "今天学习Hugging Face Tokenizer，非常有意思。",
    "RAG combines retrieval and generation.",
    "检索增强生成可以让模型利用外部知识库回答问题。",
]


print(
    f"{'chars':>8}"
    f"{'tokens':>8}"
    f"  text"
)

print("-" * 80)


for text in texts:

    encoding = tokenizer(
        text,
        add_special_tokens=False
    )

    char_count = len(text)

    token_count = len(
        encoding["input_ids"]
    )

    print(
        f"{char_count:>8}"
        f"{token_count:>8}"
        f"  {text}"
    )


    print("\nDetailed tokenization")
print("=" * 80)


for text in texts:

    tokens = tokenizer.tokenize(text)

    print("\nText:")
    print(text)

    print("Tokens:")
    print(tokens)

    print(
        f"chars={len(text)}, "
        f"tokens={len(tokens)}"
    )



text = (
    "RAG systems retrieve relevant documents "
    "before generating an answer. "
    * 20
)

full_encoding = tokenizer(
    text,
    add_special_tokens=False
)

truncated_encoding = tokenizer(
    text,
    add_special_tokens=False,
    truncation=True,
    max_length=50
)

full_count = len(
    full_encoding["input_ids"]
)

truncated_count = len(
    truncated_encoding["input_ids"]
)

print("\nTruncation experiment")
print("=" * 80)

print(
    "Original tokens:",
    full_count
)

print(
    "Retained tokens:",
    truncated_count
)

print(
    "Removed tokens:",
    full_count - truncated_count
)

print(
    "Retention ratio:",
    f"{truncated_count / full_count:.2%}"
)
    