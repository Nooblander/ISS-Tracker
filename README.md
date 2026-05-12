# ISS-Tracker
🛰️ ISS Real-Time Data Pipeline Overview  This project is a Python-based data ingestion pipeline that tracks the International Space Station (ISS). It bridges the gap between real-time orbital mechanics and local data storage by polling live APIs and preserving historical snapshots of the station's location and its international crew.

🛠️ Tech Stack

    Language: Python 3.x

    Libraries: requests (API Interaction), json (Data Serialization), time (Concurrency Control)

    Data Format: JSON
🚀 Key Features

    Multi-Source Integration: Simultaneously fetches live orbital coordinates and current crew manifest.

    Defensive Programming: Implemented robust error handling for HTTP timeouts and connection resets to ensure pipeline stability.

    Time-Series Partitioning: Automatically generates unique, timestamped .json files to prevent data corruption and allow for historical audit trails.

    Human-Centric Logging: Cleanly parses nested API responses into a structured format, separating telemetry from crew metadata.

📈 Future Roadmap (Phase 2)

    Geospatial Visualization: Mapping the captured coordinates using Pandas and Folium.

    Telemetry Analytics: Calculating the orbital velocity between data points.

📖 How to Use

    Clone the repository.

    Install requirements: pip install requests.

    Run iss.py to begin a tracking session.
