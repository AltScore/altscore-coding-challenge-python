from fastapi import APIRouter
from server.usecase.process_csv import process_batch_from_csv
from server.schemas.input import BatchInputSchema, BatchOutputSchema

challenge_router = APIRouter()


@challenge_router.post("/process-batch-from-csv", response_model=BatchOutputSchema)
def process_csv(input_data: BatchInputSchema):
    processed_payloads = process_batch_from_csv(csv_data=input_data.csv_data, sources_config=input_data.sourcesConfig)
    return processed_payloads
