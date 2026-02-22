from google.adk.agents.llm_agent import Agent
from google.adk.tools.mcp_tool import MCPToolset
from mcp import StdioServerParameters
from Agent.prompts.Prompt import PROMPT
from .tools.RAGQuery import RAG_QUERY
from .tools.FetchPrice import FETCH_PRODUCT_DETAILS

root_agent = Agent(
    model='gemini-2.5-pro',
    name='root_agent',
    description='ReturnBotAI is an AI-powered agent designed to assist in processing customer returns in real time. It integrates seamlessly with the MCP tool server to perform return-related operations such as fetching order details, sending emails, and more.',
    instruction= PROMPT,
    tools=[
        RAG_QUERY,
        FETCH_PRODUCT_DETAILS,
        MCPToolset(
            connection_params=StdioServerParameters(
                command="<JDK_Path>",
                args=["-jar", "<JAR_LOCATION>"]
            )
        ),
    ]
)

