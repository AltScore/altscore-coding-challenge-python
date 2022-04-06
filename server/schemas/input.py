from pydantic import BaseModel
from typing import Union, List, Dict, Optional, Any


class SourceInputKeys(BaseModel):
    field: str
    required: bool
    atLeastOneRequired: Optional[bool]
    structure: Dict


class SourcesConfigSchema(BaseModel):
    sourceId: str
    enabled: bool
    retryNumber: int
    version: int
    inputKeys: List[SourceInputKeys]


class BatchInputSchema(BaseModel):
    csv_data: str
    sourcesConfig: List[Union[None, SourcesConfigSchema]]


class BatchOutputSchema(BaseModel):
    result: bool
    payload: Optional[List[Dict]]
