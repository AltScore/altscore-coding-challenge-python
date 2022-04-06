from fastapi import FastAPI
from starlette.middleware.gzip import GZipMiddleware
from starlette.responses import JSONResponse
from server.api import router as endpoint_router
from starlette.requests import Request
import uvicorn

ALLOWED_ORIGINS = '*'  # or 'foo.com', etc.

app = FastAPI(title="AltScore Challenge", version="1")
app.add_middleware(GZipMiddleware, minimum_size=1000)
app.include_router(endpoint_router)


# set CORS headers
@app.middleware("http")
async def add_CORS_header(request: Request, call_next):
    response = await call_next(request)
    response.headers['Access-Control-Allow-Origin'] = ALLOWED_ORIGINS
    response.headers['Access-Control-Allow-Methods'] = 'POST, GET, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Authorization, Content-Type'
    return response


@app.exception_handler(500)
async def add_CORS_header_500(request: Request, call_next):
    response = JSONResponse(content={"detail": "something went wrong :("}, status_code=500)
    response.headers['Access-Control-Allow-Origin'] = ALLOWED_ORIGINS
    response.headers['Access-Control-Allow-Methods'] = 'POST, GET, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Authorization, Content-Type'
    return response


@app.on_event("startup")  # Code to be run when the server starts.
async def startup_event():
    pass


@app.get("/ping")
async def ping():
    """Home page
    """
    return JSONResponse({"message": "pong"})


if __name__ == "__main__":
    uvicorn.run("server.main:app", log_level="debug", reload=True)
