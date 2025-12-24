# ЛР4. Собственный сервис в Kubernetes

В этой работе развернул сервис в Kubernetes, по аналогии с ЛР2 и ЛР3.

Сервис состоит из двух основных компонентов:

- PostgreSQL (база данных)
- Python-веб-приложение + init-контейнер для первичной инициализации БД

Все файлы работы находятся в папке `lab4/`.

---

## Архитектура

### 1. База данных — `db`

- **Deployment:** `db-deployment.yml`
- **Service:** `db-service.yml`
- **ConfigMap:** `db-configmap.yml`
- **Secret:** `db-secret.yml`

PostgreSQL разворачивается в отдельном Deployment и доступен по сервису `lab4-db-service`
(имя и namespace можно посмотреть через `kubectl get svc`).

В `db-configmap.yml` лежат настройки БД.  
В `db-secret.yml` хранятся креды для подключения.

В Deployment базы:

- контейнер использует публичный образ `postgres:14`;
- описан `volume` для данных БД, который монтируется в `/var/lib/postgresql/data`;
- переменные окружения подтягиваются через:

  ```yaml
  envFrom:
    - configMapRef:
        name: db-configmap
    - secretRef:
        name: db-secret
