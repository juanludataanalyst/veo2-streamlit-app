#!/usr/bin/env python3
"""
Generador de Videos con Veo 2 - Interfaz Web
Aplicación Streamlit para generar videos usando Google Veo 2
"""

import streamlit as st
import time
import os
from google import genai
from google.genai import types

def generate_video(api_key, prompt, config=None):
    """Generar video usando Veo 2"""
    try:
        client = genai.Client(api_key=api_key)
        
        operation = client.models.generate_videos(
            model="veo-2.0-generate-001",
            prompt=prompt,
            config=config
        )
        
        return operation, client
    except Exception as e:
        return None, str(e)

def poll_operation(client, operation):
    """Polling del estado de la operación"""
    while not operation.done:
        time.sleep(10)
        operation = client.operations.get(operation)
    return operation

def main():
    st.set_page_config(
        page_title="Generador de Videos Veo 2",
        page_icon="🎥",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    st.title("🎥 Generador de Videos con Veo 2")
    st.markdown("**Genera videos de alta calidad usando inteligencia artificial**")
    st.markdown("---")
    
    # Sidebar para configuración
    with st.sidebar:
        st.header("🔑 Autenticación")
        api_key = st.text_input(
            "API Key de Google AI",
            type="password",
            help="Obtén tu API key en https://aistudio.google.com/app/apikey"
        )
        
        if not api_key:
            st.warning("⚠️ Necesitas una API key para usar la aplicación")
            st.markdown("""
            **Para obtener tu API key:**
            1. Ve a [Google AI Studio](https://aistudio.google.com/app/apikey)
            2. Inicia sesión con tu cuenta de Google
            3. Crea una nueva API key
            4. Cópiala y pégala arriba
            """)
        
        st.markdown("---")
        
        # Configuración del video
        st.header("⚙️ Configuración del Video")
        
        aspect_ratio = st.selectbox(
            "📐 Proporción de aspecto",
            options=["16:9", "9:16"],
            index=0,
            help="16:9 para horizontal, 9:16 para vertical"
        )
        
        duration = st.selectbox(
            "⏱️ Duración (segundos)",
            options=[5, 6, 7, 8],
            index=0,
            help="Duración del video generado"
        )
        
        person_generation = st.selectbox(
            "👤 Generación de personas",
            options=["allow_adult", "dont_allow"],
            index=0,
            format_func=lambda x: "Permitir adultos" if x == "allow_adult" else "No permitir personas",
            help="Control de seguridad para personas en el video"
        )
        
        st.markdown("---")
        
        # Parámetros avanzados
        with st.expander("🔧 Parámetros Avanzados"):
            enhance_prompt = st.checkbox(
                "✨ Mejorar prompt automáticamente",
                value=True,
                help="El sistema mejorará automáticamente tu prompt"
            )
            
            use_seed = st.checkbox(
                "🎲 Usar semilla para resultados determinísticos",
                value=False,
                help="Genera videos reproducibles con la misma configuración"
            )
            
            seed_value = None
            if use_seed:
                seed_value = st.number_input(
                    "Valor de semilla",
                    min_value=0,
                    max_value=4294967295,
                    value=12345,
                    help="Número para resultados reproducibles"
                )
            
            negative_prompt = st.text_area(
                "🚫 Prompt negativo (opcional)",
                placeholder="cartoon, drawing, low quality, text, watermark",
                help="Describe lo que NO quieres en el video (sin usar 'no' o 'don't')"
            )
        
        st.markdown("---")
        st.markdown("### 📋 Instrucciones")
        st.markdown("""
        1. Introduce tu API key
        2. Configura los parámetros del video
        3. Escribe un prompt descriptivo
        4. Haz clic en 'Generar Video'
        5. Espera la generación (puede tardar varios minutos)
        """)
    
    # Área principal
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("✍️ Prompt del Video")
        prompt = st.text_area(
            "Describe el video que quieres generar:",
            height=150,
            placeholder="Ejemplo: A serene mountain landscape at sunrise, mist rolling over the peaks, gentle camera movement revealing a crystal clear lake below",
            help="Sé descriptivo y específico para obtener mejores resultados. Usa inglés para mejores resultados."
        )
        
        # Ejemplos rápidos
        st.markdown("**Ejemplos rápidos:**")
        col_ex1, col_ex2 = st.columns(2)
        
        with col_ex1:
            if st.button("🌅 Paisaje natural", key="ex1"):
                st.session_state.example_prompt = "A peaceful forest clearing with sunlight filtering through tall trees, gentle breeze moving the leaves, cinematic quality"
        
        with col_ex2:
            if st.button("🏙️ Ciudad nocturna", key="ex2"):
                st.session_state.example_prompt = "Time-lapse of a bustling city at night, car lights creating trails, skyscrapers illuminated against the dark sky"
        
        if 'example_prompt' in st.session_state:
            prompt = st.session_state.example_prompt
            del st.session_state.example_prompt
            st.rerun()
    
    with col2:
        st.header("🎬 Especificaciones Técnicas")
        
        st.info("""
        **Veo 2.0 - Especificaciones:**
        - Resolución: 720p (fijo)
        - Framerate: 24 FPS (fijo)
        - Duración: 5-8 segundos
        - Idioma prompt: Solo inglés
        - Formato: MP4 con audio
        - Límites: 20 requests/minuto
        - Marca de agua: SynthID automática
        """)
        
        if not api_key:
            st.warning("⚠️ Introduce tu API key para continuar")
        elif not prompt.strip():
            st.warning("⚠️ Escribe un prompt para generar el video")
        else:
            st.success("✅ Listo para generar video")
    
    # Botón de generación
    st.markdown("---")
    
    if st.button("🎥 Generar Video", disabled=not (api_key and prompt.strip()), type="primary"):
        if api_key and prompt.strip():
            # Crear configuración
            config = types.GenerateVideosConfig(
                aspect_ratio=aspect_ratio,
                duration_seconds=duration,
                number_of_videos=1,
                enhance_prompt=enhance_prompt,
                person_generation=person_generation
            )
            
            # Añadir parámetros opcionales
            if use_seed and seed_value is not None:
                config.seed = seed_value
            
            if negative_prompt.strip():
                config.negative_prompt = negative_prompt.strip()
            
            with st.spinner("🔄 Iniciando generación del video..."):
                operation, error = generate_video(api_key, prompt, config)
                
                if operation is None:
                    st.error(f"❌ Error al iniciar la generación: {error}")
                else:
                    st.success(f"✅ Generación iniciada. ID: {operation.name}")
                    
                    # Crear cliente para polling
                    client = genai.Client(api_key=api_key)
                    
                    # Progress bar y polling
                    progress_bar = st.progress(0)
                    status_text = st.empty()
                    
                    start_time = time.time()
                    
                    try:
                        while not operation.done:
                            elapsed = time.time() - start_time
                            status_text.text(f"⏳ Generando video... {elapsed:.0f}s transcurridos")
                            
                            # Simular progreso (estimación)
                            estimated_total = 180  # 3 minutos estimados
                            progress = min(elapsed / estimated_total, 0.95)
                            progress_bar.progress(progress)
                            
                            time.sleep(10)
                            operation = client.operations.get(operation)
                        
                        # Video completado
                        progress_bar.progress(1.0)
                        status_text.text("✅ ¡Video generado exitosamente!")
                        
                        # Descargar video
                        generated_video = operation.response.generated_videos[0]
                        video_filename = f"generated_video_{int(time.time())}.mp4"
                        
                        with st.spinner("📥 Descargando video..."):
                            try:
                                # Descargar el archivo del video
                                client.files.download(file=generated_video.video)
                                generated_video.video.save(video_filename)
                                
                                # Verificar que el archivo existe y tiene contenido
                                if os.path.exists(video_filename) and os.path.getsize(video_filename) > 0:
                                    # Leer el video como bytes para mostrarlo y descargarlo
                                    with open(video_filename, 'rb') as video_file:
                                        video_bytes = video_file.read()
                                    
                                    # Mostrar video
                                    st.markdown("---")
                                    st.header("🎬 Video Generado")
                                    st.video(video_bytes)
                                    
                                    # Botón de descarga prominente
                                    col_download1, col_download2, col_download3 = st.columns([1, 2, 1])
                                    with col_download2:
                                        st.download_button(
                                            label="📥 Descargar Video MP4",
                                            data=video_bytes,
                                            file_name=video_filename,
                                            mime="video/mp4",
                                            type="primary"
                                        )
                                    
                                    st.success(f"🎉 Video generado exitosamente! Tamaño: {len(video_bytes)/1024/1024:.1f} MB")
                                    st.info(f"📁 Archivo local: {video_filename}")
                                    
                                    # Limpiar archivo temporal
                                    try:
                                        os.remove(video_filename)
                                    except:
                                        pass
                                    
                                else:
                                    st.error("❌ Error: El video se descargó pero está vacío o corrupto")
                                    
                            except Exception as download_error:
                                st.error(f"❌ Error al descargar el video: {str(download_error)}")
                                st.info("💡 El video se generó correctamente pero hubo un problema en la descarga")
                    
                    except Exception as e:
                        st.error(f"❌ Error durante la generación: {str(e)}")
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666;'>
        <p>🤖 Powered by Google Veo 2 | Desarrollado con Streamlit</p>
        <p>⚠️ Los videos generados incluyen marca de agua SynthID invisible</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()