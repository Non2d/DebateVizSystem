from typing import Optional, List
from pydantic import BaseModel, Field #BaseModelはFastAPIで使われるスキーマモデルクラスのベースクラス

class Source(BaseModel):
    title: str = Field(..., example="WSDC 2019 Round 1")
    url: Optional[str] = Field(None, example="www.youtube.com")

class Rebuttal(BaseModel):
    src: int = Field(..., example=11)
    tgt: int = Field(..., example=22)

class TaskBase(BaseModel): #共通のフィールドを持つベースクラスを定義
    motion: str = Field(..., example="This House Would Ban Tabacco.")
    source: Source = Field(..., example={"title": "WSDC 2019 Round 1", "url": "www.youtube.com"})
    POIs: Optional[List[int]] = Field(None, example="[11, 22, 33]")
    rebuttals: List[Rebuttal] = Field(..., example=[{'src': 11, 'tgt': 22}, {'src': 22, 'tgt': 33}])

class TaskCreate(TaskBase):
    pass

class TaskCreateResponse(TaskCreate):
    id: int

    class Config:
        orm_mode = True

class Task(TaskBase):
    id: int
    # done: bool = Field(False, description="完了フラグ")

    class Config: #DBとの接続に使う
        orm_mode = True