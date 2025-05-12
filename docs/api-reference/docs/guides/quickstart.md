# ⚡️ Nexlayer Quickstart: Launch Your Frontend in 60 Seconds

Want to see your frontend live on the internet? You're 3 steps away.

No infra. No config hell. Just vibes.

---

## ✅ Step 1: Create a `nexlayer.yaml`

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

> Don't have the CLI yet? Install it from [nexlayer.io/docs/cli](https://nexlayer.io/docs/cli)

---

## 🎉 You're Live

You'll get a URL like:

```
https://my-frontend.alpha.nexlayer.ai
```

Your frontend is now deployed to global cloud infrastructure — no servers, no Kubernetes, no headaches.

---

## ➕ What's Next?

* [Add a backend + database pod (MERN style)](./quickstart-mern.md)
* Make it permanent by adding a `url:` to your YAML

But if all you wanted was to vibe and deploy your site — you're done.

---
 