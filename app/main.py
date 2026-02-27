from fastapi import FastAPI

app = FastAPI(
    title="Intelligent Workflow Automation Engine",
    version="0.1.0",
    description="Event-driven workflow automation backend"
)


@app.get("/")
def root():
    return {"message": "Automation Engine Running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
