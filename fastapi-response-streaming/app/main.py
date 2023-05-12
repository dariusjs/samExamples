from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import asyncio
import os
import openai
import random

app = FastAPI()


async def streamer():
    for i in range(10):
        await asyncio.sleep(1)
        n = random.random()
        s = f"This is streaming from Lambda {n} \n"
        yield bytes(s, encoding="raw_unicode_escape")
    # openai.organization = "org-...."
    # openai.api_key = os.getenv("OPENAI_API_KEY")
    # response = openai.Completion.create(
    #     model="text-davinci-003",
    #     prompt="You: What have you been up to?\nFriend: Watching old movies.\nYou: Did you watch anything interesting?\nFriend:",
    #     temperature=0.5,
    #     max_tokens=60,
    #     top_p=1.0,
    #     frequency_penalty=0.5,
    #     presence_penalty=0.0,
    #     stop=["You:"],
    # )
    # yield response


@app.get("/")
async def index():
    return StreamingResponse(streamer(), media_type="text/plain; charset=utf-8")
