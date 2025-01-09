# Container

* Ensure you installed [Podman](https://podman.io/)

## 1. Build the container

* Build the container on MacOS

```sh
podman build -t chat-demo:0.0.1 -f ./Dockerfile.podman
```

_Note:_ We need to build the container for a `Linux/amd64` environment, when we deploy the container to `IBM Cloud Code Engine`. Therefore we can use the [multi architecture Podman](https://blog.while-true-do.io/podman-multi-arch-images/) functionality for the container in Podman.

Example command:

```sh
podman build --platform linux/amd64 -t chat-demo-linux-amd64:0.0.1 -f ./Dockerfile.podman
```

## 2. Run the container

1. We need to load the environment variables in the terminal with `source .env`, because our container needs these variables to run.

```sh
source .env
```

2. Run the container

```sh
podman container rm chat-demo
podman run -it -p 8080:8080 -e WATSONX_APIKEY=${WATSONX_APIKEY} \
                            -e WATSONX_PROJECT_ID=${WATSONX_PROJECT_ID} \
                            -e WATSONX_REGION=${WATSONX_REGION} \
                            -e APP_USER=${APP_USER} \
                            -e APP_PASSWORD=${APP_PASSWORD} \
                            --name chat-demo \
                            "localhost/chat-demo:0.0.1"
```

## 3. Open the Chat in the browser

```sh
http://localhost:8080
```