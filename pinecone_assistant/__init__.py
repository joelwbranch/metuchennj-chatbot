# This file contains the functions that are used to create an assistant and upload files to it.

def create_assistant(pc, name):
    return pc.assistant.create_assistant(
        assistant_name=name,
        instructions="Use American English for spelling and grammar.",
        timeout=30
    )

def upload_file(assistant, file_path, metadata):
    return assistant.upload_file(
        file_path=file_path,
        metadata=metadata,
        timeout=None
    )
