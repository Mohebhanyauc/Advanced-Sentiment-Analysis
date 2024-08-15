# Testing the model
# Data sent should have an additional coloumn of the actual answers to each sentenses. 
# Accuracy of the model will be tested and errors will be printed (if any). 
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

app = FastAPI()
@app.post("/upload/")
def upload_file(file: UploadFile = File(...)):
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
    predictions=[]
    # Convert JSON string to Python dictionary
    for answer in answers:
        answer = json.loads(answer)
        predictions.append(answer["sentiment"])
    actual=df.iloc[:, 1].tolist()
    correct_predictions = sum(a == b for a, b in zip(predictions, actual))
    accuracy = correct_predictions / len(predictions)
    print(f"Accuracy: {accuracy:%}")
    df['predicted_sentiment'] = predictions
    incorrect_predictions = df[df['Actual Label'] != df['predicted_sentiment']]
    logger.info(f"errors: { incorrect_predictions }")
    return answers 

