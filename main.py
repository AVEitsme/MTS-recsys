import uvicorn


if __name__ == "__main__":
    config = uvicorn.Config("app:app", port=5000)
    server = uvicorn.Server(config)
    server.run()