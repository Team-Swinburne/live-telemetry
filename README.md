# live-telemetry
A live telemetry application for Team Swinburne Formula SAE

## Running application

```
python -m pip install fastapi "uvicorn[standard]" jinja2
uvicorn main:app --reload
```