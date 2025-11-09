# ---- Base image ----
FROM python:3.10-slim

# ---- 1) System deps ----
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# ---- 2) Set workdir ----
WORKDIR /app

# ---- 3) Copy project files ----
COPY . /app

# ---- 4) Install pip deps ----
RUN pip install --no-cache-dir -r requirements.txt

# ---- 5) Expose port ----
EXPOSE 8000

# ---- 6) Run API ----
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
