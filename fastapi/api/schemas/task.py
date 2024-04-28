from typing import Optional, List
from pydantic import BaseModel, Field #BaseModelはFastAPIで使われるスキーマモデルクラスのベースクラス

class TaskBase(BaseModel): #共通のフィールドを持つベースクラスを定義
    motion: Optional[str] = Field(None, example="This House Would Ban Tabacco.")
    source: Optional[str] = Field(None, example="WSDC_2019_R1_sKJoTL0Amk0.mp3")
    POIs: List[int] = Field(None, example="[1, 2, 3]")

class TaskCreate(TaskBase):
    pass

class TaskCreateResponse(TaskCreate):
    id: int

    class Config:
        orm_mode = True

class Task(TaskBase):
    id: int
    done: bool = Field(False, description="完了フラグ")

    class Config: #DBとの接続に使う
        orm_mode = True