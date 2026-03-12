from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello CI/CD"}
@app.get("/sum")
def sum_numbers(a: int, b: int):
    result = a + b
    return {"result": result}