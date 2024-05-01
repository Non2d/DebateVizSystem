from typing import List, Tuple, Optional

from sqlalchemy import select, join
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

import models.round as round_model
import schemas.round as round_schema

async def create_round(
    db: AsyncSession, round_create: round_schema.RoundCreate
) -> round_model.Round:
    # round = round_model.Round(**round_create.model_dump()) #よくみたらコンストラクタか
    round = round_model.Round(
        motion=round_create.motion,
        source=round_create.source.model_dump(),
        POIs=round_create.POIs,
    )
    db.add(round)
    await db.commit()
    await db.refresh(round)

    rebuttals = [round_model.Rebuttal(src=rebuttal.src, tgt=rebuttal.tgt, round_id=round.id) for rebuttal in round_create.rebuttals]
    db.add_all(rebuttals)
    await db.commit()
    await db.refresh(round)
    return round

async def get_rounds_with_rebuttals(db: AsyncSession) -> List[any]:
    result = await db.execute(
        select(round_model.Round).options(joinedload(round_model.Round.rebuttals))
    )
    rounds = result.scalars().unique().all()
    return rounds

async def get_round(db: AsyncSession, round_id: int) -> Optional[round_model.Round]:
    result: Result = await db.execute(
        select(round_model.Round).filter(round_model.Round.id == round_id)
        )
    round: Optional[Tuple[round_model.Round]] = result.first()
    return round[0] if round is not None else None

async def update_round(
        db:AsyncSession, round_create: round_schema.RoundCreate, original: round_model.Round
) -> round_model.Round:
    original.title = round_create.title
    db.add(original)
    await db.commit()
    await db.refresh(original)
    return original

async def delete_round(db: AsyncSession, original: round_model.Round) -> None:
    await db.delete(original)
    await db.commit()

