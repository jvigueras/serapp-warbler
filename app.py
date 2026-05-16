import os
import streamlit as st
import serpapi
from dotenv import load_dotenv

# Load environment variables securely from .env
load_dotenv()

# Configure Streamlit page layout
st.set_page_config(page_title="Avian Field Guide Planner", page_icon="🪶", layout="wide")

# Initialize the client exactly as requested
try:
    client = serpapi.Client(api_key=os.environ['SERPAPI_API_KEY'])
except KeyError:
    st.error("SERPAPI_API_KEY is not set. Please ensure your .env file is configured correctly.")
    st.stop()

st.title("🪶 Avian Field Guide Planner")
st.markdown("Plan your nature photography trip by gathering reference images and recent sightings.")

# User inputs
col1, col2 = st.columns(2)
with col1:
    bird_species = st.text_input("Bird Species", placeholder="e.g., Golden-browed Warbler")
with col2:
    target_region = st.text_input("Target Region", placeholder="e.g., Hidalgo, Mexico")

if st.button("Generate Field Guide", type="primary"):
    if not bird_species or not target_region:
        st.warning("Please enter both a bird species and a target region.")
    else:
        query = f"{bird_species} {target_region}"
        
        with st.spinner("Scouting for sightings and visual references..."):
            try:
                # 1. Fetch Visual Reference Images (Google Images)
                image_search = client.search(
                    engine="google",
                    q=query,
                    tbm="isch"
                )
                images_results = image_search.get("images_results", [])
                
                # 2. Fetch Recent Web Results & Sightings (Google Web)
                web_search = client.search(
                    engine="google",
                    q=query
                )
                organic_results = web_search.get("organic_results", [])
                
                # --- Display Images ---
                st.header("📸 Visual References")
                if not images_results:
                    st.info("No visual references found.")
                else:
                    # Display a clean grid of images using 4 columns
                    cols = st.columns(4)
                    for index, img in enumerate(images_results[:12]):
                        with cols[index % 4]:
                            # Use original resolution if available, fallback to thumbnail
                            img_url = img.get("original", img.get("thumbnail"))
                            caption = img.get("title", "")
                            # Truncate caption for a cleaner grid UI
                            if len(caption) > 35:
                                caption = caption[:32] + "..."
                            st.image(img_url, caption=caption, use_container_width=True)
                
                st.divider()
                
                # --- Display Web Results ---
                st.header("🌐 Recent Sightings & Information")
                if not organic_results:
                    st.info("No web results found.")
                else:
                    for result in organic_results[:10]:
                        st.markdown(f"#### [{result.get('title', 'No Title')}]({result.get('link', '#')})")
                        st.write(result.get("snippet", "No description available."))
                        
            except Exception as e:
                st.error(f"An error occurred while communicating with SerpApi: {e}")