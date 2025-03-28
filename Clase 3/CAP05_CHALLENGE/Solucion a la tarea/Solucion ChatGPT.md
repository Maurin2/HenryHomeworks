# 🌐 InternetWhisper

**InternetWhisper** es una innovadora aplicación de **chatbot conversacional** 🤖 que utiliza inteligencia artificial para interactuar con el entorno web en tiempo real. Inspirado en herramientas como **You.com** y **Google Bard**, este chatbot se destaca por su habilidad para buscar, analizar y presentar información actualizada de forma dinámica y eficiente.

---

## 💡 Características Principales

- 🔎 **Búsqueda y análisis en tiempo real** mediante técnicas avanzadas de web scraping y la API de búsqueda de Google.
- 📚 **Base de datos vectorial (Redis Vector DB)** para almacenar resultados previos y reducir consultas repetitivas.
- 🧠 Integración con **OpenAI GPT-3.5 Turbo** para generar respuestas precisas y contextuales.
- ⚡ **Actualizaciones instantáneas** mediante Server-Sent Events (SSE) con FastAPI.
- 🐳 **Contenerización con Docker** para facilitar el despliegue y la escalabilidad.

---

## ⚙️ Arquitectura Técnica

InternetWhisper cuenta con una estructura moderna y escalable compuesta por los siguientes componentes:

### 1. 🚀 **Backend y API Web**
- Creado con **FastAPI**, garantizando rapidez y eficiencia.
- Comunicación en tiempo real utilizando eventos SSE para actualizaciones instantáneas.

### 2. 🤖 **Integración de Inteligencia Artificial**
- Modelo IA: **OpenAI GPT-3.5 Turbo**.
- Embeddings de texto generados con **OpenAIEmbeddings** y **RemoteEmbeddings**, utilizados para evaluar similitudes entre consultas y documentos.

### 3. 📦 **Caché y Recuperación de Datos**
- Sistema de caché mediante **Redis Vector DB** para mejorar el rendimiento.
- Técnica de recuperación (retriever) para búsqueda, procesamiento y presentación efectiva de información extraída con web scraping.

### 4. 🐋 **Contenerización y Despliegue**
- Aplicación lista para desplegarse fácilmente usando **Docker** y **Docker Compose**.

---

## 🛠️ Configuración de Variables de Entorno

Para que la aplicación funcione correctamente, configura estas variables en tu archivo `.env` basándote en el ejemplo `.env.example`:

```env
HEADER_ACCEPT_ENCODING="gzip"
HEADER_USER_AGENT="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, como Gecko) Chrome/116.0.0.0 Safari/537.36 (gzip)"
GOOGLE_API_HOST="https://www.googleapis.com/customsearch/v1?"
GOOGLE_FIELDS="items(title, displayLink, link, snippet, pagemap/cse_thumbnail)"
GOOGLE_API_KEY="<tu_clave_api_google>"
GOOGLE_CX="<tu_id_motor_busqueda_personalizado>"
OPENAI_API_KEY="<tu_clave_api_openai>"
```

⚠️ **Nota:** Recuerda reemplazar los valores entre `<>` por tus claves reales.

---

## 🚦 Cómo Ejecutar Localmente

Sigue estos pasos para correr InternetWhisper en tu entorno local:

### 📥 Instalación de Dependencias

1. Clona el repositorio:
   ```bash
   git clone <url_del_repositorio>
   cd internetwhisper
   ```

2. Configura el archivo `.env` como se explicó previamente.

### 🐳 Construcción y Ejecución con Docker

1. Construye los contenedores:
   ```bash
   docker-compose build
   ```

2. Inicia la aplicación:
   ```bash
   docker-compose up
   ```

🌟 **Puertos activos:**
- Backend ➡️ **Puerto 8000**
- Frontend (interfaz de usuario) ➡️ **Puerto 8501**

### ✅ Acceso y Pruebas

1. Accede a la aplicación mediante tu navegador:
   - **Interfaz:** [http://localhost:8501](http://localhost:8501)

2. Realiza consultas y disfruta de respuestas generadas en tiempo real.

---

## 📖 Documentación OpenAPI

InternetWhisper ofrece documentación interactiva basada en **OpenAPI** para facilitar la comprensión e integración:

- Accede a la documentación en tu navegador:
  - 📌 [http://localhost:8000/docs](http://localhost:8000/docs)

- Explora los endpoints, métodos HTTP y esquemas de solicitudes/respuestas mediante Swagger UI.

---

🎉 **¡Disfruta explorando esta poderosa herramienta de acceso inteligente a la información en Internet!** 🌟