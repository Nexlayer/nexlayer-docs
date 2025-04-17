---
title: FAQ
---

# ❓ Frequently Asked Questions

**1. Why doesn't Nexlayer require a login for previews?**  
- **Anti‑Vendor Lock‑In**: We believe shipping should be painless—no vendor accounts, no forms, no barriers. Preview deployments spin up in seconds and live for 2 hours without any login.  
- **Intelligent Integration Layer**: Nexlayer connects your code to everything it needs—compute, storage, networking, DNS, volumes—so you can focus on building, not onboarding.  
- **Developer Experience**: Instant feedback loop with live URLs, perfect for rapid prototyping and team collaboration.  
- **Security First**: Each preview gets a unique, isolated environment with automatic cleanup after expiration.

---

**2. What makes Nexlayer unique compared to other cloud platforms?**  
Nexlayer is the **only** cloud platform that gives **individual developers** and **autonomous agents** the **flexibility**, **control**, and **power** to achieve true **real‑time, production‑grade speed**, **performance**, and **massive scale**—all through a single declarative YAML, CLI, Web UI, or AI‑agent workflow.  
> **No other cloud platform** puts you in control of enterprise‑scale infrastructure—giving you the power, flexibility, and speed of a global container platform, without any of the complexity.

---

**3. I use Vercel/Netlify—why switch to Nexlayer?**  
- **Full‑Stack in One**: Frontend, backend, databases, caches, vector‑DBs, and AI integrations—all in a single config.  
- **Instant Previews & Permanent URLs**: 2 hr preview, then flip `url:` for a live, HTTPS‑enabled domain.  
- **Built for Scale**: Automatic service discovery, resource allocation, and autoscaling—no manual configs.  
- **Advanced Features**: Built‑in support for WebSockets, long‑running processes, and stateful applications.  
- **Cost Effective**: Pay only for what you use with automatic resource optimization.

---

**4. Do you host GPU workloads or custom model weights?**  
⚠️ **Running AI Models on Nexlayer**  
Nexlayer integrates with AI services—it does **not** host or serve custom model weights or GPUs. For inference use:  
- **External APIs**: OpenAI, Claude, Together.ai  
- **Hosted Inference**: Hugging Face Inference, Modal, FireworksAI  

Need dedicated GPU infrastructure? Ask about our **Enterprise Plan**.

---

**5. How do I migrate from Docker‑Compose or Terraform?**  
1. Convert each service to a `pod:` block in your `nexlayer.yaml`.  
2. Remove manual `resources:`—Nexlayer handles CPU, memory, and storage automatically.  
3. Replace hostnames with `<pod-name>.pod`.  
4. Deploy via `nexlayer deploy` or `curl`; see your preview in seconds.  
- **Migration Tools**: Our CLI can auto-convert basic Docker‑Compose setups.

---

**6. How do I extend or claim a preview?**  
Use your `sessionToken` from the deploy response:  
```bash
# Extend another 2 hrs
curl -X POST https://app.nexlayer.io/extendDeployment \
  -H "Content-Type: application/json" \
  -d '{"sessionToken":"<token>","applicationName":"my-app"}'

# Claim as permanent
curl -X POST https://app.nexlayer.io/claimDeployment \
  -H "Content-Type: application/json" \
  -d '{"sessionToken":"<token>","applicationName":"my-app"}'
```

---

**7. What about CI/CD and AI agent integrations?**  
- **GitHub Actions**: One curl step on push triggers your deployment.
- **AI Agents**: Automate via Cursor, Copilot, Claude, Warp, or ChatGPT prompts.
- **CLI Hooks**: Embed nexlayer deploy in any pipeline (GitLab, CircleCI, Jenkins).
- **Advanced Features**: Rollback, approvals, and environment promotions built‑in.

---

**8. How does pricing compare?**  
- **Free Preview**: 2 hr live URL, no login or card needed.
- **Scale Plan**: $49/month/app + usage‑based NXC credits—comparable to a small VM + managed DB.
- **Enterprise**: Custom SLAs, dedicated API endpoints, on‑prem proxies, and volume pricing for large fleets.

---

**9. Which frameworks and services can I use?**  
- **Frontend**: Next.js, Remix, React, Angular, Vue, Svelte
- **Backend**: Express, Node.js, Django, FastAPI, Flask
- **Databases**: PostgreSQL, MySQL, MongoDB, Neon, SQLite
- **Caches**: Redis, Memcached, Valkey, Dragonfly, KeyDB
- **Vector DBs**: Pinecone, Qdrant, Milvus, Chroma, Weaviate
- **AI & LLMs**: OpenAI API, Claude API, Hugging Face Inference API, LangChain, Vertex AI, Ollama, Modal, FireworksAI

---

**10. Need help or want to learn more?**  
- **Docs**: docs.nexlayer.io
- **CLI Repo**: github.com/Nexlayer/nexlayer-cli
- **Community**: Discord & Slack for builders and agent‑developers
- **Support**: support@nexlayer.io or open a GitHub issue
