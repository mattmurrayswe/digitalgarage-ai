from fastapi import FastAPI

app = FastAPI(title="digitalgarage-ai API")


@app.get('/health')
def health():
    return {'status': 'ok'}
