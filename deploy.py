from flows.hello_world import hello_world_flow

# 建立部署
hello_world_flow.serve(
    name="hello-world-deployment",
    version="1",
    interval=10,
    tags=["hello-world"],
    description="A simple hello world deployment"
)
