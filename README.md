# 🧠 FinanzasBot – MVP

**Un bot inteligente para gestionar tus finanzas con FastAPI + Python.**
Versión mínima funcional (MVP), ideal para escalar luego.

---

## 📌 ¿Qué es FinanzasBot?

FinanzasBot es un sistema backend que permite:

* Registrar gastos e ingresos mediante una API o mensajes tipo bot (“gaste 500 en transporte”).
* Crear categorías con presupuestos.
* Consultar cuánto queda disponible por categoría.
* Procesar mensajes con lógica automática sin IA (por ahora).
* Preparado para integrarse con OpenAI, Telegram y WhatsApp en futuras versiones.

Este proyecto está pensado para crecer por módulos, empezando simple y escalando con IA después.

---

## 🚀 Tecnologías utilizadas

* **Python 3.10+**
* **FastAPI** – Framework backend rápido y moderno.
* **SQLite** – Base de datos local simple para el MVP.
* **SQLAlchemy** – ORM para manejar los modelos.
* **Pydantic** – Validación de datos.
* **python-dotenv** – Manejo de variables de entorno.
* **Uvicorn** – Servidor ASGI para desarrollo.

---

## 📂 Estructura del proyecto (MVP)

```
FINANCEBOT/
│── env/                # Entorno virtual (IGNORADO)
│── main.py             # Lógica principal del backend
│── .env                # Variables de entorno (IGNORADO)
│── .gitignore          # Archivos/carpeta a ignorar
│── requirements.txt    # Dependencias
│── vercel.json         # Configuración para despliegue
│── README.md           # Este archivo :)
```

---

## 🔐 Variables de entorno (.env)

Este archivo **no se sube al repositorio**. Debes crearlo manualmente:

```
TELEGRAM_BOT_TOKEN=tu_token
OPENAI_API_KEY=tu_api_key
```

En producción (Vercel), debes configurarlas desde:
**Project → Settings → Environment Variables**

---

## ⚙️ Instalación y ejecución local

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/FinanzasBot.git
cd FinanzasBot
```

### 2️⃣ Crear entorno virtual

```bash
python -m venv env
source env/Scripts/activate   # Windows
# o
source env/bin/activate       # Linux/Mac
```

### 3️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4️⃣ Ejecutar el servidor FastAPI

```bash
uvicorn main:app --reload
```

### 5️⃣ Abrir documentación interactiva (Swagger)

```
http://127.0.0.1:8000/docs
```

---

## 📡 Endpoints principales (MVP)

### Categorías

| Método | Endpoint                   | Descripción                     |
| ------ | -------------------------- | ------------------------------- |
| POST   | `/categories`              | Crear categoría con presupuesto |
| GET    | `/categories`              | Listar categorías               |
| GET    | `/categories/{id}/summary` | Ver gasto y restante            |

### Transacciones

| Método | Endpoint        | Descripción               |
| ------ | --------------- | ------------------------- |
| POST   | `/transactions` | Registrar gasto o ingreso |
| GET    | `/transactions` | Listar movimientos        |

### Bot

| Método | Endpoint       | Descripción                                     |
| ------ | -------------- | ----------------------------------------------- |
| POST   | `/bot/message` | Procesar texto estilo “gaste 500 en transporte” |

Ejemplos soportados:

* `gaste 500 en comida`
* `cuanto me queda en transporte`

---

## 📈 Roadmap / Futuras mejoras

* Integración completa con **OpenAI** para interpretar mensajes naturales.
* Conexión con **Telegram Bot API**.
* Sistema de usuarios y autenticación.
* Cálculo de ciclos (de cobro a cobro o mensual).
* Dashboard y reportes financieros.
* Metas de ahorro.
* Notificaciones inteligentes.
* Integración con WhatsApp Cloud API.

---

## 🤝 Contribuciones

Por ahora es un proyecto personal, pero cualquier recomendación o mejora es bienvenida.

---

## 📄 Licencia

Uso personal por ahora.
Se puede adaptar o modificar libremente con créditos.

---

## 👑 Autor

**Rusbel Rodríguez Paulino (Russ)**
Desarrollador Backend / Python / FastAPI
República Dominicana 🇩🇴

