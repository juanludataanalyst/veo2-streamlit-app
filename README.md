# 🎥 Generador de Videos Veo 2

Aplicación web para generar videos usando Google Veo 2, construida con Streamlit.

## 🚀 Demo en Vivo

[Ver aplicación desplegada en Streamlit Cloud](https://your-app-url.streamlit.app)

## ✨ Características

- **Generación de videos con IA**: Usa Google Veo 2 para crear videos de alta calidad
- **Interfaz intuitiva**: UI moderna y fácil de usar
- **Configuración avanzada**: Control total sobre parámetros de generación
- **Descarga directa**: Descarga videos en formato MP4
- **Seguro**: Sin almacenamiento de API keys

## 🎬 Capacidades

### Configuración del Video
- **Proporción**: 16:9 (horizontal) o 9:16 (vertical)
- **Duración**: 5-8 segundos seleccionables
- **Resolución**: 720p con 24 FPS
- **Audio**: Incluido automáticamente

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
- Usa descripciones detalladas y específicas
- Escribe en inglés para mejores resultados
- Experimenta con diferentes duraciones y proporciones
- Usa el prompt negativo para evitar elementos no deseados

## 📋 Especificaciones Técnicas

- **Modelo**: veo-2.0-generate-001
- **Resolución**: 720p (fijo)
- **Framerate**: 24 FPS (fijo)
- **Duración**: 5-8 segundos
- **Formato**: MP4 con audio
- **Límites**: 20 requests por minuto
- **Marca de agua**: SynthID automática (invisible)

## ⚠️ Limitaciones

- Solo acepta prompts en inglés
- Resolución fija en 720p
- Duración máxima de 8 segundos
- Marca de agua SynthID no removible
- Límite de 20 generaciones por minuto

## 🛠️ Tecnologías

- **Frontend**: Streamlit
- **IA**: Google Veo 2
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

---

🎬 **¡Crea videos increíbles con IA!**