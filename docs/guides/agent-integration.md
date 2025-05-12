---
# 🤖 Agent Integration: Prompt → Deploy

Nexlayer is built for AI-native workflows. You can prompt any AI coding tool (like Cursor, Claude, or ChatGPT) to generate, build, and deploy your app using three simple API calls:

---

## 🔁 Nexlayer Agent API Flow

```txt
1. GET /schema               → build a valid YAML
2. POST /validate            → check if it’s valid (optional)
3. POST /startUserDeployment → deploy and return a live URL
```

---

## 🧠 Full AI Deployment Prompt

> “Create a Dockerfile for my project.
> Then build the image and push it to Docker Hub, GHCR, or any registry.
> After that, call `GET https://app.nexlayer.io/schema` to generate a `nexlayer.yaml`.
> Update the `nexlayer.yaml` with the image you just pushed, and deploy it by calling `POST https://app.nexlayer.io/startUserDeployment`.
> Show me the live URL.”

This prompt works across all environments and tools — whether you're using Claude, Cursor, ChatGPT, or a custom agent.

---

## 🧩 What the Agent Should Do

1. 🔨 **Create a Dockerfile** based on the user's project
2. 🐳 **Build and tag the image locally**
3. ☁️ **Push the image** to a container registry (Docker Hub, GHCR, etc.)
4. 📄 **Fetch Nexlayer schema** from `GET /schema`
5. 🧩 **Generate and update `nexlayer.yaml`** using the image you just pushed
6. 🚀 **Deploy via `POST /startUserDeployment`**
7. 🔗 **Print the live app URL** from the response

---

## 🐳 Image Hosting Reminder

Every image listed in your `nexlayer.yaml` must be hosted on a registry. Nexlayer cannot use local images.

✅ Valid examples:

```yaml
image: "your-username/my-app:latest"
image: "ghcr.io/your-org/ai-backend:v1.2.0"
```

❌ Invalid examples:

```yaml
image: "./Dockerfile"
image: "local-image"
```

If the image hasn’t been pushed to a public or private registry, the deployment will fail.

---

## 🔗 API Endpoints Summary

| Action   | Endpoint                                           | Description                 |
| -------- | -------------------------------------------------- | --------------------------- |
| Generate | `GET https://app.nexlayer.io/schema`               | Get full YAML schema        |
| Validate | `POST https://app.nexlayer.io/validate`            | Check if your YAML is valid |
| Deploy   | `POST https://app.nexlayer.io/startUserDeployment` | Launch your app live        |

---

Nexlayer was built for agents. You describe the app. Your agent ships it.
