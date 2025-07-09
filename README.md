# appgen

A project generator CLI for web frameworks. Quickly scaffold projects for Next.js, React, Express, Flask, and more, with support for features like TypeScript and Tailwind.

## Features

- Generate projects for multiple frameworks (Next.js, React, Express, Flask, etc.)
- Next.js App Router and Pages Router support
- Optional TypeScript and Tailwind integration
- Prisma ORM integration for Next.js projects
- shadcn/ui component library integration for Next.js (with a Button example)
- MongoDB integration for Express projects
- Fullstack presets (MERN, Next.js + Prisma)
- Interactive CLI mode for guided setup
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

#### Interactive Mode (Recommended)

```sh
appgen create --interactive
```

#### Individual Frameworks

Generate a Next.js App Router project:

```sh
appgen create --framework nextjs --dir my-next-app --router app
```

Generate a Next.js Pages Router project with TypeScript and Tailwind:

```sh
appgen create --framework nextjs --dir my-next-app --router pages --features typescript,tailwind
```

Generate a Next.js project with Prisma ORM:

```sh
appgen create --framework nextjs --dir my-next-app --router app --features typescript,tailwind,prisma
```

Generate a Next.js project with shadcn/ui:

```sh
appgen create --framework nextjs --dir my-next-shadcn-app --router app --features shadcn
```

Generate a React project with TypeScript:

```sh
appgen create --framework reactjs --dir my-react-app --features typescript
```

Generate an Express project with MongoDB:

```sh
appgen create --framework express --dir my-express-app --features mongodb
```

Generate a Django project:

```sh
appgen create --framework django --dir my-django-app
```

#### Fullstack Presets

Generate a MERN stack (MongoDB + Express + React + Node.js):

```sh
appgen preset mern --dir my-mern-app
```

Generate a Next.js fullstack with Prisma:

```sh
appgen preset nextjs-fullstack --dir my-nextjs-app
```

#### Other Commands

List all available frameworks:

```sh
appgen list-frameworks
```

Show current configuration:

```sh
appgen config
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

## Available Frameworks & Features

### Interactive Frameworks

- **Next.js**: App Router & Pages Router, TypeScript, Tailwind CSS, Prisma ORM, shadcn/ui
- **React**: TypeScript, Tailwind CSS

### Simple Frameworks

- **Express.js**: MongoDB integration with Mongoose
- **Flask**: Lightweight Python web framework
- **Django**: Full-featured Python web framework with PostgreSQL support

### Fullstack Presets

- **MERN Stack**: MongoDB + Express + React + Node.js
- **Next.js Fullstack**: Next.js + Prisma + PostgreSQL

## Next Steps / Ideas for More Features

- [x] Add support for more frameworks (Django added)
- [x] Interactive CLI prompts for options
- [x] Environment variable and .env file support
- [x] Fullstack presets (MERN, Next.js + Prisma)
- [ ] Add support for more frameworks (e.g., Vue, Svelte, FastAPI)
- [ ] Add custom template support (user-defined templates)
- [ ] Add linting, formatting, and testing tool integrations (ESLint, Prettier, Jest, etc.)
- [ ] Support for monorepo structures (e.g., TurboRepo, Nx)
- [ ] Add project initialization with git and first commit
- [ ] Add plugin system for community-contributed features
- [ ] Generate README and license files for new projects
- [ ] Add CI/CD configuration templates (GitHub Actions, GitLab CI, etc.)

---

Feel free to contribute or suggest more features!
