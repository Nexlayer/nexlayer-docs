---
# 🔄 Continuous Integration with Nexlayer

You can deploy to Nexlayer from any CI pipeline using a simple `curl` call. There’s no special format required—just build your image, push it to a registry, and post your `nexlayer.yaml` to the deployment endpoint.

> 💡 **Any technology that can be containerized can be deployed on Nexlayer** — from Node.js, Python, and Go, to ML workloads, microservices, or internal tools.

## ✅ Basic CI Flow

```bash
curl -X POST https://app.nexlayer.io/startUserDeployment \
  -H "Content-Type: text/x-yaml" \
  --data-binary @nexlayer.yaml
```

If successful, the response will include a live URL:

```json
{
  "url": "https://yourapp-name.nexlayer.app"
}
```

---

## 🧠 What Your CI Should Do

1. 🐳 **Build your Docker image**
2. ☁️ **Push it to a public or private registry** (recommended: **GitHub Container Registry**)
3. 📄 **Update your `nexlayer.yaml`** with the image reference (e.g., `ghcr.io/your-org/your-app:tag`)
4. 🚀 **Deploy using `POST /startUserDeployment`**

> 📝 **Note on databases**: You can connect to external managed databases (like MongoDB Atlas, Supabase, or Neon). While it works, we recommend deploying your own DB pod on Nexlayer for tighter control, lower latency, and environment isolation.

---

## 🛠 GitHub Actions Example (with GHCR)

```yaml
name: Nexlayer CI/CD

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write

    steps:
      - uses: actions/checkout@v3

      - name: Log in to GitHub Container Registry
        run: echo "${{ secrets.GITHUB_TOKEN }}" | docker login ghcr.io -u ${{ github.actor }} --password-stdin

      - name: Build and push Docker image
        run: |
          docker build -t ghcr.io/${{ github.repository }}:latest .
          docker push ghcr.io/${{ github.repository }}:latest

      - name: Patch nexlayer.yaml with image
        run: |
          sed -i "s|image:.*|image: ghcr.io/${{ github.repository }}:latest|" nexlayer.yaml

      - name: Deploy to Nexlayer
        run: |
          curl -X POST https://app.nexlayer.io/startUserDeployment \
            -H "Content-Type: text/x-yaml" \
            --data-binary @nexlayer.yaml
```

> 💡 Tip: GitHub’s native container registry (GHCR) is a secure and reliable choice for CI/CD deployments.

---

## 🔔 CI Notifications (Optional)

To capture deployment status, capture the response:

```bash
RESPONSE=$(curl -s -X POST https://app.nexlayer.io/startUserDeployment \
  -H "Content-Type: text/x-yaml" \
  --data-binary @nexlayer.yaml)

URL=$(echo "$RESPONSE" | jq -r .url)
echo "✅ Deployed to: $URL"
```

You can then send it to Slack or Discord using a webhook.

---

## 🌐 Endpoints Summary

| Action     | Endpoint                                                |
| ---------- | ------------------------------------------------------- |
| Deploy     | `POST https://app.nexlayer.io/startUserDeployment`      |
| (Optional) | `GET https://app.nexlayer.io/schema` – generate YAML    |
| (Optional) | `POST https://app.nexlayer.io/validate` – validate YAML |

---

## 📦 Notes on Image Hosting

* All images must be hosted on a registry (e.g., Docker Hub, GHCR)
* Local images will not work—Nexlayer must be able to pull the image remotely

---

## 🧪 Common Gotchas

* ❌ Missing `image:` tag or incorrect reference in your YAML
* ❌ Using a local-only Docker image not pushed to a registry
* ❌ Not updating your `nexlayer.yaml` with the image tag you just pushed

---

## ✅ Recap: Full Flow in CI

1. Build your Docker image
2. Push it to GHCR or another registry
3. Update your `nexlayer.yaml`
4. `curl -X POST /startUserDeployment`
5. Parse and post the returned URL if needed

---

This CI flow works across all platforms—GitHub Actions, GitLab CI, CircleCI, etc.—because it’s just HTTP. You bring the image, Nexlayer brings the launchpad.
