import typer
from openai import OpenAI

app = typer.Typer()
client = OpenAI()

def chat(user_input: str, history: list[dict]):

    history.append({"role": "user", "content": user_input})

    response = client.responses.create(
        model="gpt-4o-mini",
        input=history,
        store=False
    )

    history += [{"role": el.role, "content": el.content} for el in response.output]

    return response.output_text


@app.command()
def start_chat(system_prompt: str = "You are a helpful assistant."):

    typer.echo("Chat started. Type 'exit' to quit.\n")

    history = [{"role": "developer", "content": system_prompt}]

    while True:
        user_input: str = typer.prompt("You")

        if user_input.lower() == "exit":
            typer.echo("Goodbye!")
            raise typer.Exit()
        
        response = chat(user_input, history)
        typer.echo(f"Assistant: {response}\n")


if __name__ == "__main__":
    app()
