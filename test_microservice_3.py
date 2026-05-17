import requests

valid_response = requests.post(
    "http://127.0.0.1:5001/generate_reminder",
    json={
        "task_name": "Submit project report",
        "due_date": "2026-05-18",
        "completed": False
    }
)

print("VALID TASK RESPONSE:")
print(valid_response.json())


completed_response = requests.post(
    "http://127.0.0.1:5001/generate_reminder",
    json={
        "task_name": "Complete old assignment",
        "due_date": "2026-05-17",
        "completed": True
    }
)

print("\nCOMPLETED TASK RESPONSE:")
print(completed_response.json())


missing_data_response = requests.post(
    "http://127.0.0.1:5001/generate_reminder",
    json={
        "task_name": "Missing due date example"
    }
)

print("\nMISSING DATA RESPONSE:")
print(missing_data_response.json())