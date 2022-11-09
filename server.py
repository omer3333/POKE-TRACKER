from fastapi import FastAPI
from Routes import pokemon_routes
from Routes import trainer_routes
from Routes import evolve_routes
import uvicorn



app = FastAPI()
app.include_router(pokemon_routes.router)
app.include_router(trainer_routes.router)
app.include_router(evolve_routes.router)

#
if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
