# Main project 
from fastapi import FastAPI, File, UploadFile
import pandas as pd
from io import StringIO
import os , openai ,fastapi, pydantic
from openai import OpenAI
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from prompts.prompts import TEST_PROMPT
from io import BytesIO
import json
from logging_utils.logging_main import logger 
import time
from email_utils.sending_email import send_email

app = FastAPI()
@app.post("/upload/")
def upload_file(email: str, file: UploadFile = File(...)):
    file_content = file.file.read()
    answers=[]
    df = pd.read_excel(BytesIO(file_content), engine='openpyxl')
    sentences = df.iloc[:, 0].tolist()
    logger.info(sentences)
    for i in sentences:
        os.environ["OPENAI_API_KEY"] = #add key
        client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
)
        chat_completion = client.chat.completions.create(
            messages=[
            {
                "role": "user",
                "content": TEST_PROMPT.format(comment=i),
            }
        ],
        response_format= { "type":"json_object" },
        model="gpt-4o",
)
        answers.append(chat_completion.choices[0].message.content)
    logger.info(f"Answers: {answers}")
    sentiments=[]
    reasons=[]
    for answer in answers:
        answer = json.loads(answer)
        sentiments.append(answer["sentiment"])
        reasons.append(answer["reason"])
    df['predicted_sentiment'] = sentiments
    df['predicted_reason']=reasons
    time_id=int(time.time())
    df.to_excel(f"data/output_{time_id}.xlsx", sheet_name='Sheet1', index=False)
    send_email(to_email=email,attachment_file_path=f"data/output_{time_id}.xlsx")
    return answers 
