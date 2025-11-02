from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from .api.routes import router
from .config import settings

# Create FastAPI application
app = FastAPI(
    title=settings.app_name,
    description="AI-powered cover letter generator using Claude and ChatGPT",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(router, prefix="/api", tags=["Cover Letter Generator"])


@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "message": "AI Cover Letter Generator API",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/api/health"
    }


@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """Global exception handler for unhandled errors."""
    return JSONResponse(
        status_code=500,
        content={
            "detail": "An internal error occurred. Please try again later.",
            "error_type": type(exc).__name__
        }
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

