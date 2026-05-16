# serapp-warbler
Avian Field Guide Planner is a Streamlit dashboard built for nature photographers and birders. It utilizes the SerpApi Python SDK to simultaneously aggregate regional web data (recent sightings, forum discussions) and high-quality visual reference images based on a target species and location.

# Avian Field Guide Planner 🪶

A lightweight Streamlit dashboard designed to help nature photographers and birders plan field trips. Built for the PyCon US 2026 SerpApi Hackathon/Raffle.

This application takes a target species and a specific region, then uses the **SerpApi Python SDK** to perform two simultaneous searches:
1. **Google Search API:** Aggregates recent web results, forum posts, and local blogs about recent sightings in the target area.
2. **Google Images API:** Pulls a grid of high-quality visual references of the specimen.

## 📦 Dependencies

This project requires Python 3.x and relies on the following core packages:
* `streamlit` - For the frontend UI and dashboard rendering.
* `serpapi` - The official SerpApi Python SDK for executing search queries.
* `python-dotenv` - For secure local environment variable management.

*A complete list of dependencies is available in the `requirements.txt` file.*

## ⚙️ Setup Instructions

**1. Clone the repository**

git clone [https://github.com/jvigueras/serapp-warbler.git](https://github.com/jvigueras/serapp-warbler.git)
cd serapp-warbler

**2. Create a virtual environment and install dependencies
It is recommended to use uv or pip to install the requirements:
uv venv
uv pip install -r requirements.txt

**3. Configure your API Key
This application requires a free API key from SerpApi.
Create a file named .env in the root directory of the project and add your key:
SERPAPI_API_KEY=your_private_api_key_here
(Note: Ensure .env is included in your .gitignore to prevent leaking your key).

## 🚀 Usage
**1. Start the application
-Run the following command in your terminal:
  streamlit run app.py

**2. Interact with the Dashboard
  - The app will open in your default web browser (usually at http://localhost:8501).
  - Species Input: Enter the target bird you are looking for (e.g., Golden-browed Warbler / Chipe Cejidorado).
  - Region Input: Enter your target photography location (e.g., Hidalgo, Mexico).
  - Click Search to generate the visual reference grid and local sighting reports.

🛠️ Built With
- Streamlit
- SerpApi
- Python
