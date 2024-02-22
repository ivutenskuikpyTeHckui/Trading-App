from typing import Annotated
from sqlalchemy.orm import mapped_column
import datetime
from sqlalchemy import text


intpk = Annotated[int, mapped_column(primary_key=True, nullable=False)]
str_100 = Annotated[str, 100]
created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]