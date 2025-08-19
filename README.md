# 🎥 Generador de Videos Veo 2 & 3

Aplicación web para generar videos usando Google Veo 2 y Veo 3, construida con Streamlit.

## 🚀 Demo en Vivo

[Ver aplicación desplegada en Streamlit Cloud](https://your-app-url.streamlit.app)

## ✨ Características

- **Dual Engine**: Soporta tanto Google Veo 2 como Veo 3
- **Audio nativo**: Veo 3 incluye generación automática de audio sincronizado
- **Múltiples resoluciones**: 720p (ambos) y 1080p (solo Veo 3)
- **Interfaz intuitiva**: UI moderna y fácil de usar
- **Configuración avanzada**: Control total sobre parámetros de generación
- **Descarga directa**: Descarga videos en formato MP4
- **Seguro**: Sin almacenamiento de API keys

## 🎬 Capacidades

### Configuración del Video
- **Modelos**: Veo 2 o Veo 3 seleccionables
- **Proporción**: 
  - Veo 2: 16:9 (horizontal) o 9:16 (vertical)
  - Veo 3: 16:9 únicamente
- **Duración**: 
  - Veo 2: 5-8 segundos seleccionables
  - Veo 3: 8 segundos (fijo)
- **Resolución**: 
  - Veo 2: 720p (fijo)
  - Veo 3: 720p o 1080p seleccionable
- **Audio**: 
  - Veo 2: Sin audio nativo
  - Veo 3: Audio sincronizado automáticamente

### Controles Avanzados
- **Mejora de prompt**: Optimización automática del texto
- **Control de personas**: Permite o prohíbe personas en el video
- **Prompt negativo**: Especifica qué evitar en el video
- **Semilla determinística**: Para resultados reproducibles

## 🔧 Instalación Local

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/veo2-streamlit-app.git
   cd veo2-streamlit-app
   ```

2. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar la aplicación**:
   ```bash
   streamlit run app.py
   ```

## 🔑 Configuración de API Key

1. Ve a [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Inicia sesión con tu cuenta de Google
3. Crea una nueva API key
4. Cópiala y úsala en la aplicación

## 📱 Desplegar en Streamlit Cloud

1. **Fork este repositorio** en GitHub
2. **Conecta tu cuenta** en [Streamlit Cloud](https://share.streamlit.io)
3. **Despliega** seleccionando tu repositorio
4. **Configura** el archivo principal como `app.py`

### Configuración del despliegue:
```
Repository: tu-usuario/veo2-streamlit-app
Branch: main
Main file path: app.py
```

## 🎯 Uso

1. **Introduce tu API key** en el campo correspondiente
2. **Configura los parámetros** del video (duración, proporción, etc.)
3. **Escribe un prompt descriptivo** en inglés
4. **Genera el video** y espera unos minutos
5. **Descarga** el resultado en MP4

### Consejos para mejores resultados:

#### General (ambos modelos)
- Usa descripciones detalladas y específicas
- Escribe en inglés para mejores resultados
- Experimenta con diferentes duraciones y proporciones
- Usa el prompt negativo para evitar elementos no deseados

#### Específico para Veo 3
- Incluye descripciones de audio en tu prompt (sonidos, música, diálogos)
- Aprovecha la mayor resolución seleccionando 1080p
- Considera que el video será siempre de 8 segundos
- El audio se genera automáticamente basado en las descripciones visuales

## 📋 Especificaciones Técnicas

### Veo 2
- **Modelo**: veo-2.0-generate-001
- **Resolución**: 720p (fijo)
- **Framerate**: 24 FPS (fijo)
- **Duración**: 5-8 segundos
- **Formato**: MP4 (sin audio nativo)
- **Límites**: 20 requests por minuto
- **Marca de agua**: SynthID automática (invisible)

### Veo 3
- **Modelo**: veo-3.0-generate-preview
- **Resolución**: 720p o 1080p seleccionable
- **Framerate**: 24 FPS (fijo)
- **Duración**: 8 segundos (fijo)
- **Proporción**: 16:9 únicamente
- **Formato**: MP4 con audio sincronizado
- **Límites**: 10 requests por minuto
- **Marca de agua**: SynthID automática (invisible)
- **Audio**: Generación nativa de sonidos, música y diálogos

## ⚠️ Limitaciones

### Ambos modelos
- Solo acepta prompts en inglés
- Marca de agua SynthID no removible

### Veo 2
- Resolución fija en 720p
- Sin audio nativo
- Límite de 20 generaciones por minuto

### Veo 3
- Duración fija de 8 segundos
- Límite de 10 generaciones por minuto
- Modelo en preview (puede tener limitaciones)

## 🛠️ Tecnologías

- **Frontend**: Streamlit
- **IA**: Google Veo 2 & 3
- **Backend**: Python
- **Deploy**: Streamlit Cloud

## 📄 Licencia

MIT License - ve el archivo [LICENSE](LICENSE) para más detalles.

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature
3. Commit tus cambios
4. Push a la rama
5. Abre un Pull Request

## 📞 Soporte

Si tienes problemas o preguntas:
- Abre un [issue](https://github.com/tu-usuario/veo2-streamlit-app/issues)
- Revisa la [documentación de Veo 2](https://cloud.google.com/vertex-ai/generative-ai/docs/models/veo)
- Revisa la [documentación de Veo 3](https://cloud.google.com/vertex-ai/generative-ai/docs/models/veo/3-0-generate-preview)

---

🎬 **¡Crea videos increíbles con IA!**