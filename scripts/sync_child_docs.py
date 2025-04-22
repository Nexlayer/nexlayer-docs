import os
import shutil
import yaml

CHILD_REPOS = {
    "nexlayer-deployment-yaml": {
        "source": "nexlayer-deployment-yaml",
        "destination": "docs/deployment",
        "nav_section": ["Docs", "Deployment"]
    },
    "api-reference": {
        "source": "api-reference",
        "destination": "docs/api-reference",
        "nav_section": ["API & SDK"]
    }
}

MKDOCS_YML = "mkdocs.yml"

def ensure_dirs():
    for repo in CHILD_REPOS.values():
        os.makedirs(repo["destination"], exist_ok=True)

def clean_and_copy():
    for repo in CHILD_REPOS.values():
        # Clean destination
        if os.path.exists(repo["destination"]):
            shutil.rmtree(repo["destination"])
        os.makedirs(repo["destination"], exist_ok=True)

        # Copy .md files
        for root, _, files in os.walk(repo["source"]):
            for file in files:
                if file.endswith(".md"):
                    rel_path = os.path.relpath(os.path.join(root, file), repo["source"])
                    dest_path = os.path.join(repo["destination"], rel_path)
                    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

                    if os.path.basename(file).lower() == "readme.md":
                        dest_path = os.path.join(os.path.dirname(dest_path), "readme.md")

                    shutil.copy2(os.path.join(root, file), dest_path)

def build_nav_for_file(path):
    name = os.path.splitext(os.path.basename(path))[0].replace("-", " ").capitalize()
    return {name: path.replace("\\", "/")}

def load_existing_nav(yml_path):
    with open(yml_path, "r") as f:
        return yaml.load(f, Loader=yaml.FullLoader)

def update_mkdocs_nav(existing):
    original_nav = existing.get("nav", [])
    new_nav = []

    # Filter out existing API & SDK and Deployment sections
    for item in original_nav:
        if isinstance(item, dict):
            key = list(item.keys())[0]
            if key in ["API & SDK"]:
                continue
            if key == "Docs":
                docs_section = item["Docs"]
                filtered_docs = []
                for subitem in docs_section:
                    if isinstance(subitem, dict) and "Deployment" in subitem:
                        continue
                    filtered_docs.append(subitem)
                new_nav.append({"Docs": filtered_docs})
            else:
                new_nav.append(item)
        else:
            new_nav.append(item)

    # Inject Deployment under Docs
    for repo_key, repo in CHILD_REPOS.items():
        child_nav = []
        for root, _, files in os.walk(repo["destination"]):
            for file in sorted(files):
                if file.endswith(".md"):
                    rel_path = os.path.relpath(os.path.join(root, file), "docs")
                    child_nav.append(build_nav_for_file(rel_path))

        # Insert under correct nav structure
        if repo["nav_section"] == ["Docs", "Deployment"]:
            for nav in new_nav:
                if "Docs" in nav:
                    nav["Docs"].append({"Deployment": child_nav})
                    break
        else:
            new_nav.append({repo["nav_section"][0]: child_nav})

    existing["nav"] = new_nav
    return existing

def write_updated_mkdocs(config):
    with open(MKDOCS_YML, "w") as f:
        yaml.dump(config, f, sort_keys=False)

def main():
    ensure_dirs()
    clean_and_copy()

    mkdocs_config = load_existing_nav(MKDOCS_YML)
    updated_config = update_mkdocs_nav(mkdocs_config)
    write_updated_mkdocs(updated_config)

    print("✅ Synced all child repos and updated mkdocs.yml.")

if __name__ == "__main__":
    main()
