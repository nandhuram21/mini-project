from ollama import embeddings

response = embeddings(
    model = 'nomic-embed-text:latest',
    prompt = 'what is Artificial Intelligence'
)

print(response['embedding'])