FROM python:3.12-slim

WORKDIR /app

# Install gateway dependencies
COPY gateway/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy gateway server and default backend config
COPY gateway/server.py .
COPY gateway/backends.json .

# Install dependencies for bundled backend servers
COPY names/requirements.txt /tmp/names-requirements.txt
RUN pip install --no-cache-dir -r /tmp/names-requirements.txt

# Copy bundled backend servers so the gateway can spawn them via stdio
COPY names/server.py /servers/names/server.py

EXPOSE 8000

ENTRYPOINT ["python", "server.py"]
