# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DefendResponse", "Stats"]


class Stats(BaseModel):
    outputs_below_threshold: Optional[int] = None
    """Number of AI outputs that failed the guardrails."""

    outputs_improved: Optional[int] = None
    """Number of AI outputs that were improved."""

    outputs_processed: Optional[int] = None
    """Total number of AI outputs processed by the workflow."""


class DefendResponse(BaseModel):
    automatic_hallucination_tolerance_levels: Optional[Dict[str, Literal["low", "medium", "high"]]] = None
    """Mapping of guardrail metric names to tolerance values.

    Values can be strings (`low`, `medium`, `high`) for automatic tolerance levels.
    """

    created_at: Optional[datetime] = None
    """The time the workflow was created in UTC."""

    custom_hallucination_threshold_values: Optional[object] = None
    """Mapping of guardrail metric names to threshold values.

    Values can be floating point numbers (0.0-1.0) for custom thresholds.
    """

    description: Optional[str] = None
    """
    A description for the workflow, to help you remember what that workflow means to
    your organization.
    """

    improvement_action: Optional[Literal["regen", "fixit", "do_nothing"]] = None
    """
    The action used to improve outputs that fail one or more guardrail metrics for
    the workflow events.
    """

    name: Optional[str] = None
    """
    A human-readable name for the workflow that will correspond to it's workflow ID.
    """

    stats: Optional[Stats] = None

    status: Optional[Literal["inactive", "active"]] = None
    """Status of the selected workflow.

    May be `inactive` or `active`. Inactive workflows will not accept events.
    """

    threshold_type: Optional[Literal["custom", "automatic"]] = None
    """Type of thresholds used to evaluate the event."""

    updated_at: Optional[datetime] = None
    """The most recent time the workflow was updated in UTC."""

    workflow_id: Optional[str] = None
    """A unique workflow ID used to identify the workflow in other endpoints."""
