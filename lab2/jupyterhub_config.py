import os

c = get_config()

c.JupyterHub.ip = "0.0.0.0"
c.JupyterHub.port = 8000

# БД берём из .env
c.JupyterHub.db_url = os.environ["HUB_DB_URL"]
