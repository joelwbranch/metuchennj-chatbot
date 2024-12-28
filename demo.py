import pinecone_assistant
from pinecone import Pinecone
from pinecone_plugins.assistant.models.chat import Message

pc = Pinecone(api_key="pcsk_YJRqp_4SEHDq75DUmfPTo2o1NB2nZcFue86ThwmJzhxoA56sY6iwwcDy6Y6DT6haPEEXQ")
name = "metuchennj-assistant"

file_path = "data/metuchen_ordinances.pdf"
metadata = {"city": "Metuchen", "document_type": "ordinances", "year": 2024}

try:
    asst = pinecone_assistant.create_assistant(pc)
    resp = pinecone_assistant.upload_file(asst, file_path, metadata)
    print(resp)
except Exception as e:
    asst = pc.assistant.Assistant(assistant_name=name)
    print(asst)

msg = Message(role="user", content="What are the ordinances about dog ownership?")
resp = asst.chat(messages=[msg])
print(resp["message"]["content"])
