# Digit Recognition
Web application that recognize hand-drawn digits

- Python 3.12 used</li>
- CNN model built with keras</li>
- FastAPI used as web framework</li>

# Try it out
Clone the repository
```
git clone https://github.com/Overwhelmed44/DigitRecognition.git
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