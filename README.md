# Numbers Recognition
Web application that recognize hand-drawn numbers

- Python 3.12 used
- CNN model built with keras
- FastAPI used as web framework

# Try it out
Clone the repository
```
git clone https://github.com/Overwhelmed44/DigitRecognition.git
```
Install all required packages
```
pip install -r requirements.txt
```
Run the app with an ASGI server
```python
from uvicorn import run
from app import app

def main():
    run(app)

if __name__ == '__main__':
    main()
```
