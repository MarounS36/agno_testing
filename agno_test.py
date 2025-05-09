from pathlib import Path

from agno.agent import Agent
from agno.media import File
from agno.models.openai.responses import OpenAIResponses
from agno.utils.media import download_file

pdf_path = Path(__file__).parent.joinpath("Nietzsche_Beyond_Good&Evil.pdf")

# Download the file using the download_file function
download_file(
    "https://www.bing.com/search?qs=MT&pq=quran+pd&sk=CSYN1&sc=16-8&pglt=769&q=quran+pdf+download&cvid=8c6a5e2af1c546ac901c7a6d07cb61c8&gs_lcrp=EgRlZGdlKgcIABAAGPkHMgcIABAAGPkHMgYIARBFGDkyBggCEAAYQDIGCAMQABhAMgYIBBAAGEAyBggFEAAYQDIGCAYQABhAMgYIBxAAGEAyBggIEAAYQNIBCDI2NzdqMGoxqAIAsAIA&FORM=ANNTA1&PC=NMTS", str(pdf_path)
)

agent = Agent(
    model=OpenAIResponses(id="gpt-4o-mini",  api_key="sk-proj-SB77YjEyVaquhj4ssqgYT3BlbkFJiqhUJTDrErwRUde2pq48"),
    tools=[{"type": "file_search"}],
    markdown=True,
    add_history_to_messages=True,
)

agent.print_response(
    "Explaint to me paragraph 25",
    files=[File(filepath=pdf_path)],
)
# agent.print_response("Suggest me a recipe from the attached file.")