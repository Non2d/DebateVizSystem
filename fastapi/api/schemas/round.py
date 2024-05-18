from typing import Optional, List
from pydantic import BaseModel, Field #BaseModelはFastAPIで使われるスキーマモデルクラスのベースクラス
from datetime import datetime

speeches_example = [
    {
      "start_time": 60.12,
      "ADUs": [
        {
          "segments": [
            {
              "start": 0,
              "end": 100,
              "text": "We are proud to propose."
            }
          ],
          "sequence_id": 1,
          "transcript": "Some transcript"
        }
      ]
    }
]

class Source(BaseModel):
    title: str = Field(..., example="WSDC 2019 Round 1")
    url: Optional[str] = Field(None, example="www.youtube.com")

class Rebuttal(BaseModel):
    src: int = Field(..., example=11)
    tgt: int = Field(..., example=22)

class Segment(BaseModel):
    start: float = Field(..., example=0)
    end: float = Field(..., example=100)
    text: str = Field(..., example="We are proud to propose.")

class ADU(BaseModel):
    sequence_id: Optional[int] = Field(None, example=1)
    segments: List[Segment] = Field(..., example=[{"start": 0, "end": 100, "text": "We are proud to propose."}, {"start": 100, "end": 300, "text": "Thank you."}])
    transcript: Optional[str] = Field(None, example="We are proud to propose.")

class Speech(BaseModel):
    start_time: Optional[float] = Field(None, example=0)
    ADUs: List[ADU] = Field(..., example= [{"sequence_id":1, "transcript":"We agree."}])

class RoundBase(BaseModel): #共通のフィールドを持つベースクラスを定義
    created_at: datetime = Field(None, example=datetime.now())
    updated_at: datetime = Field(None, example=datetime.now())
    deleted_at: Optional[datetime] = Field(None)
    motion: str = Field(..., example="This House Would Ban Tabacco.")
    source: Source = Field(..., example={"title": "WSDC 2019 Round 1", "url": "www.youtube.com"})
    POIs: Optional[List[int]] = Field(None, example="[11, 22, 33]")
    rebuttals: Optional[List[Rebuttal]] = Field(None, example=[{'src': 11, 'tgt': 22}, {'src': 22, 'tgt': 33}])
    speeches: List[Speech] = Field(..., example=speeches_example)

class RoundCreate(RoundBase):
    pass

class RoundCreateResponse(RoundBase):
    id: int
    class Config:
        orm_mode = True

class Round(RoundBase):
    id: int

    class Config: #DBとの接続に使う
        orm_mode = True