# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["FileResponse"]


class FileResponse(BaseModel):
    created_at: Optional[datetime] = None
    """The time the file was created in UTC."""

    file_id: Optional[str] = None
    """A unique file ID."""

    file_name: Optional[str] = None
    """Name of the file."""

    file_path: Optional[str] = None
    """Path to the s3 bucket where the file is stored."""

    updated_at: Optional[datetime] = None
    """The most recent time the file was modified in UTC."""
