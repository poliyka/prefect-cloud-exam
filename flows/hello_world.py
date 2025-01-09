from prefect import flow, task

@task
def say_hello(name: str) -> str:
    message = f"Hello {name}!"
    print(message)
    return message

@flow(name="hello-world-flow", log_prints=True)
def hello_world_flow(name: str = "World"):
    return say_hello(name)

if __name__ == "__main__":
    hello_world_flow()
