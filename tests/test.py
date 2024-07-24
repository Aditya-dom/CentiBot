import pytest
from fastapi.testclient import TestClient
from app.chat import app

client = TestClient(app)

@pytest.fixture
def test_pdf_file():
    return "path/to/your/test.pdf"

def test_upload_pdf(test_pdf_file):
    with open(test_pdf_file, "rb") as pdf_file:
        response = client.post("/upload/pdf", files={"file": pdf_file})
    assert response.status_code == 200
    assert "filename" in response.json()
    assert "text_length" in response.json()

def test_query_pdf():
    query = {"question": "What is the main topic?"}
    response = client.post("/query/sample.pdf", json=query)
    assert response.status_code == 200
    assert "answer" in response.json()
