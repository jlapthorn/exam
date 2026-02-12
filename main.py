from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

#test123

app = FastAPI()

# 1. Define the structure of your data
class ExamRecord(BaseModel):
    name: str
    paper: str
    result: float  # or int, depending on your scoring system

# 2. This is your temporary in-memory "database"
exam_database: List[dict] = []

# 3. Create the path to input data
@app.post("/input-exam")
async def add_exam_data(record: ExamRecord):
    # Convert Pydantic model to a standard dictionary
    new_data = record.model_dump() 
    
    # Add to our list
    exam_database.append(new_data)
    
    return {"message": "Data added successfully", "current_count": len(exam_database)}

# 4. (Optional) Path to view the list
@app.get("/view-exams")
async def get_all_exams():
    return exam_database
