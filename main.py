from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root() -> str:
    return 'How are you doing ;-)!'
  
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=10000)