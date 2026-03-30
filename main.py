import typer
from openai import OpenAI
from openai.types.conversations.conversation import Conversation
from openai.types.responses.response import Response
from openai.types.responses.response_stream_event import ResponseStreamEvent
from rich.markdown import Markdown
from rich.live import Live
from rich.console import Console

app = typer.Typer()
client = OpenAI()
console = Console()

def chat(user_input: str, history: list[dict]) -> str:

    history.append({"role": "user", "content": user_input})

    response: Response = client.responses.create(
        model="gpt-4o-mini",
        input=history,
        store=False
    )

    history += [{"role": el.role, "content": el.content} for el in response.output]

    return response.output_text


def chat_with_conversations(user_input: str, conversation: Conversation, system_prompt: str):

    stream = client.responses.create(
        model="gpt-4o-mini",
        input=[{"role": "developer", "content": system_prompt}, 
               {"role": "user", "content": user_input}],
        conversation=conversation.id,
        stream=True,
    )

    return stream



@app.command()
def start_chat(system_prompt: str = "You are a helpful assistant."):

    typer.echo("Chat started. Type 'exit' to quit.\n")

    history = [{"role": "developer", "content": system_prompt}]
    conversation: Conversation = client.conversations.create()

    while True:
        user_input: str = typer.prompt("You")

        if user_input.lower() == "exit":
            typer.echo("Goodbye!")
            raise typer.Exit()
        
        stream = chat_with_conversations(user_input, conversation, system_prompt)
        output = "Assistant: "
        with Live("", console=console, refresh_per_second=20) as live:
            for chunk in stream:
                if chunk.type == "response.output_text.delta":
                    output += chunk.delta
                    live.update(Markdown(output))


        # typer.echo(f"Assistant: {response}\n")


if __name__ == "__main__":
    app()
