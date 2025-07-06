# appgen

A project generator CLI for web frameworks. Quickly scaffold projects for Next.js, React, Express, Flask, and more, with support for features like TypeScript and Tailwind.

## Features

- Generate projects for multiple frameworks (Next.js, React, Express, Flask, etc.)
- Next.js App Router and Pages Router support
- Optional TypeScript and Tailwind integration
- Clean up duplicate JS/TS/JSX/TSX files automatically

## Installation

Install from PyPI:

```sh
pip install appgen
```

Or install locally from source:

```sh
pip install .
```

## Usage

```sh
appgen --help
```

### Example Commands

Generate a Next.js App Router project:

```sh
appgen create --framework nextjs --dir my-next-app --router app
```

Generate a Next.js Pages Router project with TypeScript and Tailwind:

```sh
appgen create --framework nextjs --dir my-next-app --router pages --features typescript,tailwind
```

Generate a React project with TypeScript:

```sh
appgen create --framework reactjs --dir my-react-app --features typescript
```

Generate an Express project:

```sh
appgen create --framework express --dir my-express-app
```

## Development

- To install in editable mode for development:
  ```sh
  pip install -e .
  ```
- To build and upload to PyPI:
  ```sh
  python -m build
  twine upload dist/*
  ```

## Next Steps / Ideas for More Features

- [ ] Add support for more frameworks (e.g., Vue, Svelte, Django, FastAPI)
- [ ] Add custom template support (user-defined templates)
- [ ] Interactive CLI prompts for options instead of command-line flags
- [ ] Add linting, formatting, and testing tool integrations (ESLint, Prettier, Jest, etc.)
- [ ] Support for monorepo structures (e.g., TurboRepo, Nx)
- [ ] Add project initialization with git and first commit
- [ ] Add environment variable and .env file support
- [ ] Add plugin system for community-contributed features
- [ ] Generate README and license files for new projects
- [ ] Add CI/CD configuration templates (GitHub Actions, GitLab CI, etc.)

---

Feel free to contribute or suggest more features!
