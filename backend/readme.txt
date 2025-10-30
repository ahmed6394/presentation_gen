cd project/backend
python -m venv venv

# On Windows:
venv\Scripts\activate

# On Mac/Linux:
source venv/bin/activate
```

You should see `(venv)` at the start of your terminal line.

## Step 2: Create requirements.txt

Create `project/backend/requirements.txt` with this content:
```
fastapi==0.104.1
uvicorn==0.24.0
PyGithub==2.1.1
python-pptx==0.6.23
markdown2==2.4.9
python-dotenv==1.0.0
pydantic==2.5.0
requests==2.31.0