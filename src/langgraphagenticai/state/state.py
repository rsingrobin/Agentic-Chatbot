from typing_extensions import TypedDict,List
from langgraph.graph.message import add_messages
from typing import Annotated

class State(TypedDict):
    """sumary_line
    
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    messages: Annotated[list,add_messages]