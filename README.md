# Nexlayer Templates
Templates are an easy way to deploy your favorite apps to NexLayer. 

## General Template Structure

`application.template.name`: The name of the application template. This name will be used to identify the template stack.

`application.template.deploymentName`: The name of the deployment. This name will be used as your deployment name in the Nexlayer UI.

`application.template.registryLogin`: The registry login information. This is the login information for the registry where any of your private Docker images are stored.

`application.template.pods`: The `pods` section is an array of objects that define the pods that will be deployed. Each pod object has the following properties:

- `type`: The type of pod to be deployed.  In the current version, this can be one of the following:
  - `database`
  - `llm`
  - `django`
  - `fastapi`
  - `express`
  - `react`
  - `angular`
  - `vue`
  - `nginx`

- `exposeHttp`: A boolean value that determines whether the pod should be exposed via HTTP. If true, the pod will be exposed via HTTP. If false, the pod will not be exposed via HTTP. This is required if true!

- `name`: The name of the pod. This name will be used to identify the pod further.  In the current version, this can be one of the following:
	- For `database` type pods:
		- `postgres`
		- `mysql`
		- `neo4j`
		- `redis`
		- `mongodb`
   - For `llm` type pods:
	- This can be any name you want to give to the pod to describe the llm.  Currently, only one llm may be provisioned per deployment.
   - For remaining pod types:
	- This name must match the name of the pod type.  For example, for a `django` pod, the name must be `django`.

- `tag`: The Docker image to be used for the pod. This can be a public image or a private image stored in a private registry.

- `privateTag`: A boolean value that determines whether the Docker image is stored in a private registry. If true, the Docker image is stored in a private registry.  This is required if true!

- `vars`: The environment variables to be set for the pod. This is an array of objects, where each object has the following properties:
  - `name`: The name of the environment variable.
  - `value`: The value of the environment variable.

## Nexlayer Provided Vars Values

| Variable Value             | Description                                                                                  | Example                                           |
|----------------------------|----------------------------------------------------------------------------------------------|---------------------------------------------------|
| `PROXY_URL`                | The URL of your created Nexlayer site.                                                      | `https://your-site-name.alpha.nexlayer.ai`       |
| `PROXY_DOMAIN`             | The domain of your created Nexlayer site.                                                   | `your-site-name.alpha.nexlayer.ai`              |
| `DATABASE_HOST`            | The hostname of your database.                                                              | -                                                 |
| `NEO4J_URI`                | The URI of your Neo4j database.                                                             | -                                                 |
| `DATABASE_CONNECTION_STRING` | The connection string to connect to your database.                                          | `postgresql://user:password@host:port/dbname`    |
| `FRONTEND_CONNECTION_URL`  | The URL to connect to your frontend. Connects to your `react`, `angular`, or `vue` pod.     | -                                                 |
| `BACKEND_CONNECTION_URL`   | The URL to connect to your backend. Connects to your `django`, `fastapi`, or `express` pod. | -                                                 |
| `LLM_CONNECTION_URL`       | The URL to connect to your LLM. Connects to your `llm` pod.                                 | -                                                 |


## Creating a Github Actions Workflow to Build your Docker Image

Follow the steps below to create a Github Actions workflow to build your Docker image and push it to the Github Container Registry.

1. Create a new file in your repository named `.github/workflows/docker-publish.yml`.
2. Copy and paste the following code into the file:

```yaml
name: Build Docker Image

on:
  push:
	branches:
	  - main

jobs:
  build:
	runs-on: ubuntu-latest

	permissions:
      contents: read
      packages: write

	steps:
	- name: Checkout code
	  uses: actions/checkout@v2

	- name: Log in to GitHub Container Registry
        uses: docker/login-action@v2
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

	- name: Set repository owner lowercase # Necessary for Docker image tagging
        id: owner_lowercase
        run: echo "owner_lowercase=$(echo '${{ github.repository_owner }}' | tr '[:upper:]' '[:lower:]')" >> $GITHUB_ENV

	- name: Build and Push Docker Image
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: ghcr.io/${{ env.owner_lowercase }}/my-image-name:v0.0.1
```

3. Replace `my-image-name` with the name of your Docker image.

This will create a Github Actions workflow that builds your Docker image and pushes it to the Github Container Registry. The workflow will run whenever you push to the `main` branch.

You can set the context of the `Build and Push Docker Image` step to the directory where your Dockerfile is located. If your Dockerfile is located in the root directory of your repository, you can set the context to `.`.

To view an example of a Github Actions workflow that builds and pushes multiple Docker images to the Github Container Registry, see the `.github/workflows/docker-publish.yml` file in any of the stack repositories under the Nexlayer organization.
