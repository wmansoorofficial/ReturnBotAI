# ReturnBotAI

**ReturnBotAI** is an AI-powered agent designed to assist in processing customer returns in real time. It integrates seamlessly with the **MCP tool server** to perform return-related operations such as fetching order details, sending emails, and more.  

ReturnBotAI is also grounded in an **external knowledge base**, enabling it to leverage return policies effectively and help agents make informed, intelligent decisions.

## Tech Stack

- **Google Agent Development Kit (ADK)**  
- **Python 3.14 or above**  
- **MCP Server** (developed in Java)  
- **Google Vertex AI**  
- **Gemini Model 2.5 Pro**

## Architecture 
<p align="center">
  <img src="https://github.com/user-attachments/assets/fc5669d8-8102-4294-ab98-25c6a17f2efe" width="600"/>
</p>

## Setup Instructions

### Prerequisites

- A Google Cloud account
- Google Cloud CLI installed and configured
- A Google Cloud project created
- Google Vertex AI services enabled
- MCP Server cloned and JAR file built  
  Repo: https://github.com/wmansoorofficial/Order-MCPServer
- Python 3.14 or above installed
- pip installed

---

### Setup Steps

1. Create a Google Cloud Project.
2. Create a Vector Store in Google Vertex AI.
3. Upload the Return Policy to the Google Vertex AI RAG Engine.
4. Replace `PROJECT_NAME` in the `.env` file with your Google Cloud project name.
5. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Set the JDK path in `agent.py`.
7. Set the JAR file path in `agent.py`.

---

### Running the Project

You can run the project using one of the following methods:

#### Option 1 — ADK Built-in UI

```bash
adk web
```

This starts the ADK built-in web interface.

#### Option 2 — API Server with Custom UI

```bash
adk api_server --allow_origins="*"
```

This disables CORS restrictions.

Use the custom UI available here:  
https://github.com/wmansoorofficial/ReturnBotAI-UI

## Demo
[![Screenshot 2026-02-23 155129](https://github.com/user-attachments/assets/7fbae9e7-64fc-491b-a0f9-48704bc38849)](https://drive.google.com/file/d/10vdd_eDjxMQyR0-c1QzlcfU4FnqMnAUP/view?usp=sharing)

