import typer
from openai import OpenAI
from openai.types.conversations.conversation import Conversation

app = typer.Typer()
client = OpenAI()

def chat(user_input: str, history: list[dict]) -> str:

    history.append({"role": "user", "content": user_input})

    response = client.responses.create(
        model="gpt-4o-mini",
        input=history,
        store=False
    )

    history += [{"role": el.role, "content": el.content} for el in response.output]

    return response.output_text


def chat_with_conversations(user_input: str, conversation: Conversation, system_prompt: str) -> str:

    response = client.responses.create(
        model="gpt-4o-mini",
        input=[{"role": "developer", "content": system_prompt}, 
               {"role": "user", "content": user_input}],
        conversation=conversation.id
    )

    return response.output_text



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
        
        response = chat_with_conversations(user_input, conversation, system_prompt)
        typer.echo(f"Assistant: {response}\n")


if __name__ == "__main__":
    app()
