from .basemodel import BaseModel
from .gcn import GCN
from .savn import SAVN
from .newsavn import NEWSAVN
from .newbasemodel import NewBaseModel

__all__ = ["BaseModel", "GCN", "SAVN", "NEWSAVN"]

variables = locals()
