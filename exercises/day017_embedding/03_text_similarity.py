from sentence_transformers import SentenceTransformer

import matplotlib
matplotlib.use('Agg')   # 使用非交互式后端，不依赖 GUI

import matplotlib.pyplot as plt


MODEL_NAME = (
    "sentence-transformers/"
    "paraphrase-multilingual-MiniLM-L12-v2"
)


model = SentenceTransformer(
    MODEL_NAME
)


texts = [
    "我喜欢学习人工智能",
    "我正在学习机器学习和深度学习",
    "今天天气非常好",
    "The weather is nice today",
    "Artificial intelligence is fascinating",
]


embeddings = model.encode(
    texts,
    convert_to_tensor=True
)


print("Embedding shape:")
print(embeddings.shape)

similarities = model.similarity(
    embeddings,
    embeddings
)


print("\nSimilarity matrix:")
print(similarities)

print("\nDetailed similarities:")

for i in range(len(texts)):
    for j in range(i+1,len(texts)):

        score = similarities[i][j].item()

        print(
            f"\n{texts[i]}"
            f"\nVS"
            f"\n{texts[j]}"
            f"\nscore = {score:.4f}"
        )


matrix = similarities.cpu().numpy()

plt.figure(figsize=(9,7))

plt.imshow(matrix)

plt.colorbar(
    label="Cosine Similarity"
)

plt.xticks(
    range(len(texts)),
    range(len(texts))
)

plt.yticks(
    range(len(texts)),
    range(len(texts))
)

plt.xlabel("Text Index")
plt.ylabel("Text Index")
plt.title("Embedding Similarity Matrix")

plt.tight_layout()

plt.savefig(
    "similarity_matrix.png",
    dpi=150
)


print(
    "\nSaved: similarity_matrix.png"
)

documents = [
    "PyTorch 是一个深度学习框架。",
    "PostgreSQL 是关系型数据库。",
    "Transformer 使用注意力机制处理序列。",
    "Docker 用于容器化应用。",
]


query = "什么框架可以训练神经网络？"

document_embeddings = model.encode_document(
    documents,
    convert_to_tensor=True
)

query_embedding = model.encode_query(
    query,
    convert_to_tensor=True
)

scores = model.similarity(
    query_embedding,
    document_embeddings
)[0]

print("\nQuery:")
print(query)


print("\nRetrieval results:")


sorted_indices = scores.argsort(
    descending=True
)


for index in sorted_indices:

    index = index.item()

    print(
        f"{scores[index].item():.4f}"
        f"  {documents[index]}"
    )