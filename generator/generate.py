import shutil
import json
from pathlib import Path
from rich import print
import os

TEMPLATE_DIR = Path(__file__).parent.parent / "templates"

def copy_template(src: Path, dest: Path):
    if not src.exists():
        print(f"[yellow]⚠️  Skipping missing template: {src}[/yellow]")
        return
    try:
        shutil.copytree(src, dest, dirs_exist_ok=True)
        print(f"[green]✅ Copied:[/green] {src.name}")
    except Exception as e:
        print(f"[red]❌ Failed to copy {src}: {e}[/red]")

def remove_conflicts(target_path: Path, features: list[str]):
    # Remove .js if .ts or .tsx exists, and .jsx if .tsx exists, recursively
    for dirpath, _, filenames in os.walk(target_path):
        files = set(filenames)
        for fname in filenames:
            # Remove .js if .ts or .tsx exists
            if fname.endswith('.ts') or fname.endswith('.tsx'):
                js_equiv = fname.rsplit('.', 1)[0] + '.js'
                if js_equiv in files:
                    js_path = Path(dirpath) / js_equiv
                    print(f"[yellow]🧹 Removing {js_path} because {fname} exists[/yellow]")
                    js_path.unlink()
            # Remove .jsx if .tsx exists
            if fname.endswith('.tsx'):
                jsx_equiv = fname[:-4] + '.jsx'
                if jsx_equiv in files:
                    jsx_path = Path(dirpath) / jsx_equiv
                    print(f"[yellow]🧹 Removing {jsx_path} because {fname} exists[/yellow]")
                    jsx_path.unlink()

def load_json(path: Path):
    if path.exists():
        with path.open() as f:
            return json.load(f)
    return {}

def merge_dicts(base, extra):
    for key, value in extra.items():
        if key not in base:
            base[key] = value
        elif isinstance(base[key], dict) and isinstance(value, dict):
            base[key] = merge_dicts(base[key], value)
    return base

def merge_package_json(framework: str, features: list[str], target_path: Path):
    # Next.js special handling
    if framework == "nextjs" and features:
        router = features[0]
        base_pkg_path = TEMPLATE_DIR / framework / router / "package.json"
        final_pkg = load_json(base_pkg_path)
        for feature in features[1:]:
            feature_pkg_path = TEMPLATE_DIR / framework / f"{router}-{feature}" / "package.json"
            feature_pkg = load_json(feature_pkg_path)
            final_pkg = merge_dicts(final_pkg, feature_pkg)
    elif framework == "express" and features and features[0] in ["mongodb", "postgresql", "supabase", "serverless"]:
        # Express with database - use database-specific package.json
        db_pkg_path = TEMPLATE_DIR / framework / features[0] / "package.json"
        final_pkg = load_json(db_pkg_path)
    else:
        base_pkg_path = TEMPLATE_DIR / framework / "base" / "package.json"
        final_pkg = load_json(base_pkg_path)
        for feature in features:
            feature_pkg_path = TEMPLATE_DIR / framework / feature / "package.json"
            feature_pkg = load_json(feature_pkg_path)
            final_pkg = merge_dicts(final_pkg, feature_pkg)
    with (target_path / "package.json").open("w") as f:
        json.dump(final_pkg, f, indent=2)
    print("[green]📦 Final package.json written[/green]")

def generate_project(framework: str, features: list[str], target_dir: str):
    target_path = Path(target_dir).resolve()
    print(f"\n[bold cyan]🚀 Generating '{framework}' project...[/bold cyan]")
    print(f"[blue]📁 Output directory:[/blue] {target_path}")
    print(f"[magenta]🧩 Features:[/magenta] {features if features else 'None'}")

    if framework == "nextjs":
        if not features:
            print("[red]❌ For Next.js, you must specify a router type as the first feature: 'app' or 'pages'.[/red]")
            return
        router = features[0]
        if router not in ("app", "pages"):
            print(f"[red]❌ Invalid router type '{router}'. Must be 'app' or 'pages'.[/red]")
            return
        # Copy base (app or pages)
        base_path = TEMPLATE_DIR / framework / router
        copy_template(base_path, target_path)
        # Copy features (app-typescript, app-tailwind, etc.)
        for feature in features[1:]:
            feature_path = TEMPLATE_DIR / framework / f"{router}-{feature}"
            if not feature_path.exists():
                print(f"[yellow]⚠️  Skipping missing feature: {feature_path}[/yellow]")
                continue
            copy_template(feature_path, target_path)
    elif framework == "express":
        # Handle Express with database selection
        if features and features[0] in ["mongodb", "postgresql", "supabase", "serverless"]:
            # Copy database-specific template
            db_template_path = TEMPLATE_DIR / framework / features[0]
            copy_template(db_template_path, target_path)
            print(f"[green]✅ Using {features[0]} database template[/green]")
        else:
            # Copy base Express template (no database)
            base_path = TEMPLATE_DIR / framework / "base"
            copy_template(base_path, target_path)
            print(f"[green]✅ Using base Express template (no database)[/green]")
    else:
        # Copy base
        base_path = TEMPLATE_DIR / framework / "base"
        copy_template(base_path, target_path)
        # Copy features
        for feature in features:
            feature_path = TEMPLATE_DIR / framework / feature
            if not feature_path.exists():
                print(f"[yellow]⚠️  Skipping missing feature: {feature_path}[/yellow]")
                continue
            copy_template(feature_path, target_path)

    # Remove JS/JSX if TS/TSX exists
    remove_conflicts(target_path, features)

    # Merge package.json
    merge_package_json(framework, features, target_path)

    print(f"\n[bold green]🎉 Project '{framework}' created successfully at {target_path}![/bold green]")
