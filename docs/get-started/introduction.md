<!-- get-started/introduction.md -->
---
title: Introduction
---

# 🦾 What Is Nexlayer?

Nexlayer is an **AI‑powered cloud** that abstracts away all infrastructure complexity. You decide what to launch, and Nexlayer automatically:

1. **Provisions** compute resources, networking, storage, DNS, and persistent volumes  
2. **Deploys** your app via YAML, our CLI, Web UI, or AI agents  
3. **Auto‑discovers** and wires up all services without manual configuration  
4. **Auto‑scales** with traffic—no manual intervention  
5. **Manages** secrets, resource allocation, and TLS certificates  
6. **Provides** instant previews (2 hr) or permanent custom domains  

---

## ⚡️ Quick Start

1. **Write** a `nexlayer.yaml`:
   ```yaml
   application:
     name: "my-app"
     pods:
       - name: web
         image: your-username/my-app:v1.0.0
         servicePorts: [3000]
