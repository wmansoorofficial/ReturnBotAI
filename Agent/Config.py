"""
Configuration settings for the RAG Agent.

These settings are used by the various RAG tools.
"""

import os

from dotenv import load_dotenv

load_dotenv()

# Vertex AI settings
PROJECT_ID = os.environ.get("GOOGLE_CLOUD_PROJECT")
LOCATION = os.environ.get("GOOGLE_CLOUD_LOCATION")

# # RAG settings
DEFAULT_TOP_K = 3
DEFAULT_DISTANCE_THRESHOLD = 0.5