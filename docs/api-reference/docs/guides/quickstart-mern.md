# 🔁 Nexlayer Quickstart: Add a Backend and Database (MERN Style)

Already launched your frontend? Let's go full stack.

In this guide, we'll add a **Node.js backend API** and a **MongoDB database** to your existing Nexlayer deployment — no infra, no devops.

---

## ✅ Step 1: Add Backend and DB Pods to `nexlayer.yaml`

Here's how to extend your existing config:

```yaml
application:
  name: "my-mern-app"
  pods:
    - name: frontend
      image: "ttl.sh/my-frontend:1h"
      path: /
      servicePorts:
        - 3000
      vars:
        API_URL: "http://backend.pod:4000"

    - name: backend
      image: "ttl.sh/my-backend:1h"
      path: /api
      servicePorts:
        - 4000
      vars:
        MONGO_URL: "mongodb://mongo.pod:27017/mydb"

    - name: mongo
      image: "mongo:6"
      servicePorts:
        - 27017
      volumes:
        - name: mongo-data
          size: "1Gi"
```

> 🧠 Use `.pod` to reference internal services. This avoids hardcoded IPs and works across environments.

---

## 🛠️ Don't Have a Docker Image for Your Backend?

Prompt your AI assistant:

```
Create a Dockerfile for my Node.js Express API.
Build it locally and push the image to ttl.sh.
Patch the nexlayer.yaml with the image URL.
```

You'll get something like:

```yaml
image: "ttl.sh/my-backend-abc123:1h"
```

Paste that into the `backend` pod section.

---

## 🚀 Deploy the Full Stack

If you're using CLI:

```bash
nexlayer deploy
```

Or use cURL:

```bash
curl -X POST https://app.nexlayer.io/startUserDeployment \
  -H "Content-Type: text/x-yaml" \
  --data-binary @nexlayer.yaml
```

---

## 🧪 Test It

You'll get a live app like:

```
https://my-mern-app.alpha.nexlayer.ai
```

Test the backend:

```
https://my-mern-app.alpha.nexlayer.ai/api/health
```

You now have:

* Frontend on `/`
* Node.js API on `/api`
* MongoDB accessible internally at `mongo.pod:27017`

---

## 🔁 What's Next?

* Secure your DB with secrets
* Add persistent volume storage if needed
* Swap to a production Mongo instance
* Set up custom domains

Want help? Just prompt your AI:

```
Help me add auth, secrets, and a production Mongo cluster to my Nexlayer app.
```

--- 