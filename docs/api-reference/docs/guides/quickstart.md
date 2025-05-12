# ⚡️ Nexlayer Quickstart: Launch Your Frontend in 60 Seconds

Want to see your frontend live on the internet? You're 3 steps away.

No infra. No config hell. Just vibes.

---

## ✅ Step 1: Create a `nexlayer.yaml`

You can write it yourself or start from our official examples:
👉 [Nexlayer YAML Templates](https://github.com/Nexlayer/nexlayer-deployment-yaml)
👉 [Live Example Apps in the Playground](https://github.com/Nexlayer/playground)

Then in the root of your project, add a file called:

In the root of your project, add a file called:

```
nexlayer.yaml
```

---

## ✏️ Step 2: Paste this starter config

```yaml
application:
  name: "my-frontend" # Change this to your app name
  pods:
    - name: web
      image: "ttl.sh/my-frontend-live:1h" # <- Replace with your actual image
      path: /
      servicePorts:
        - 3000
```

> 🧠 `ttl.sh` is a free, temporary container registry that holds your image for 1 hour. Perfect for quick testing.

---

## 🛠️ Don't Have a Docker Image Yet?

No worries. If you're using **Cursor**, **Windsurf**, **Claude Code**, or **Warp**, just copy/paste this prompt:

```
Create a Dockerfile for my frontend app.
Build it locally and push the Docker image to ttl.sh.
Patch my nexlayer.yaml with the new image URL.
```

You'll get something like:

```yaml
image: "ttl.sh/my-frontend-xyz:1h"
```

Paste that into your YAML, and you're good to go.

> 🔥 Want something permanent? Push to Docker Hub or GHCR instead.

---

## 🚀 Step 3: Deploy It

Pick your vibe:

### Option A: cURL (1-liner)

You can run this directly, or just ask your AI assistant:

```
Generate a curl command that deploys this nexlayer.yaml to Nexlayer.com
```

Then run:

```bash
curl -X POST https://app.nexlayer.io/startUserDeployment \
  -H "Content-Type: text/x-yaml" \
  --data-binary @nexlayer.yaml
```

### Option B: CLI (recommended)

```bash
nexlayer deploy
```

This command works out of the box if your `nexlayer.yaml` and Docker image are ready.

Want Nexlayer to handle the image creation for you?
Try:

```bash
nexlayer init
```

This packages your project, auto-generates a Dockerfile, builds and pushes your image, and patches your YAML.

> 🛠 CLI repo: [github.com/Nexlayer/nexlayer-cli](https://github.com/Nexlayer/nexlayer-cli)

```bash
curl -X POST "https://app.nexlayer.io/extendDeployment" \
  -H "Content-Type: application/json" \
  -d '{
    "applicationName": "My MERN App",
    "sessionToken": "your-session-token"
  }'
```

## Best Practices

1. **Error Handling**
   - Always check response status codes
   - Implement proper error handling
   - Use exponential backoff for retries

2. **Rate Limiting**
   - Respect rate limits (100 requests per minute)
   - Implement request throttling
   - Cache responses when appropriate

3. **Security**
   - Never share your session tokens
   - Use HTTPS for all requests
   - Implement proper token rotation

## Next Steps

- Explore the [full API reference](../api/README.md)
- Check out our [SDK documentation](../sdk/README.md)
- Visit our [GitHub repository](https://github.com/Nexlayer/api-reference) 

## 🎉 You're Live

You'll get a URL like:

```
https://my-frontend.alpha.nexlayer.ai
```

Your frontend is now deployed to global cloud infrastructure — no servers, no Kubernetes, no headaches.

## ➕ What's Next?

* Add a backend pod
* Add a database
* Make it permanent by adding a `url:` to your YAML

But if all you wanted was to vibe and deploy your site — you're done.

---
