# 📉 Hardware Price Tracker

Bot automatizado en Python que rastrea precios de productos en MercadoLibre Argentina para detectar ofertas.

## 🚀 Funcionalidades
- **Scraping Web:** Extrae título y precio en tiempo real.
- **Data Cleaning:** Convierte precios de texto a números enteros.
- **Persistencia:** Guarda un historial de precios en un archivo CSV (`precios.csv`).
- **Alertas:** Notifica en consola si el precio baja de un umbral objetivo.

## 🛠️ Tecnologías
- Python 3
- BeautifulSoup4
- Requests
- CSV Module

## 📦 Instalación
1. Clonar el repositorio.
2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
