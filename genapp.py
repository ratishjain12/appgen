#!/usr/bin/env python
import typer
from generator.generate import generate_project

app = typer.Typer()

@app.command()
def create(
    framework: str = typer.Option(..., help="One of: reactjs, nextjs, express, flask, strapi"),
    features: str = typer.Option("", help="Comma-separated features: typescript, tailwind"),
    dir: str = typer.Option(..., help="Target directory to generate project in"),
    router: str = typer.Option("pages", help="Router type for Next.js: app or pages", show_default=True)
):
    feature_list = [f.strip().lower() for f in features.split(",") if f.strip()]
    if framework.lower() == "nextjs":
        if router not in ("app", "pages"):
            typer.echo("[red]Please specify --router app or --router pages for Next.js.[/red]")
            raise typer.Exit()
        feature_list = [router] + feature_list
    generate_project(framework.lower(), feature_list, dir)

if __name__ == "__main__":
    app()