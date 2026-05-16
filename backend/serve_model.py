#Learn ai routing from local server and fast api
#this will initialize fast api and load the model


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests



models=["gemma4:31b-cloud"];
app= FastAPI(
    title="Trial chat application using local models",
);
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)

@app.get("/")
def read():
    return {"message":"Hello World"};


#use curl -X POST -H "Content-Type: application/json" "http://127.0.0.1:8000/print?string=hello" to test print

@app.post("/print")
#same issue of name shadowing so change endpoint nane to handle_print instead of print
def hanlde_print(string:str):
    return {"message":string};
#get caught in name shadowing my models list and models function name is same so it returns {} as empty json object instead of global models list
@app.get("/models")
def get_models():
    # console.log(models); logging not used right now
    return models;

#use curl -X POST -H "Content-Type: application/json" "http://127.0.0.1:8000/chat?message=hello" to test chat endpoint
@app.post("/generate")
def chat(message:str):
    response=requests.post(
        "http://localhost:11434/api/generate", 
            json={
                "model":"gemma4:31b-cloud",
                "prompt":message,
                "stream":False
            }
        )
    data=response.json()
    print(data)
    return {"response": data["response"]};
