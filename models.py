# Models for rest api and sever side.


from typing import List
from pydantic import BaseModel

# Model for the message that OpenAI receives
class Message(BaseModel):
    role: str
    content: str

# Model for the conversation
class Conversation(BaseModel):
    messages: List[Message]
    
# Model for the interaction between user and bot 
class Interaction(BaseModel):
    conversation: Conversation # Past conversation with the user.
    query: str # The query is the message sent by the user to continue the conversation.
    

    