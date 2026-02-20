from fastapi import FastAPI
from API.Middlewares.CORS import cors_middlewares
from API.Routes.Reg_Login_API import router_x
from API.Routes.round_1_API import router_1
from API.Routes.round_2_API import router_2
from API.Routes.round_3_API import router_3
from API.Routes.round_4_API import router_4
from API.Routes.round_5_API import router_5 


app = FastAPI() 

cors_middlewares(app)

app.include_router(router_1)
app.include_router(router_2)
app.include_router(router_3)        
app.include_router(router_4)
app.include_router(router_5)
app.include_router(router_x)
