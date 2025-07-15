# AppGen 🚀

A modern project generator CLI for web frameworks. Quickly scaffold projects for Next.js, React, Express, Flask, Django, and more with support for TypeScript, Tailwind CSS, databases, and modern tooling.

## ✨ Features

- **Multiple Frameworks**: Next.js, React, Express, Flask, Django, Svelte
- **Database Support**: MongoDB, PostgreSQL, Supabase, AWS DynamoDB
- **Modern Tooling**: TypeScript, Tailwind CSS, Prisma ORM, shadcn/ui
- **Interactive CLI**: Guided setup with beautiful UI
- **Serverless Ready**: AWS SAM templates for serverless deployment (JavaScript, TypeScript, Python, Go)
- **Fullstack Presets**: MERN stack, Next.js + Prisma, and more
- **Clean Architecture**: Modular, maintainable codebase
- **Cross-Platform**: Works on Windows, macOS, and Linux
- **Smart Dependency Install**: After project creation, choose and auto-detect your preferred package manager (npm, yarn, pnpm, bun)
- **Editor Detection**: Choose your code editor (VS Code, Cursor, Sublime, Atom, Vim, Nano) with installed status shown

## 🏗️ Architecture

AppGen uses a clean, modular architecture for maintainability and extensibility:

```
appgen/
├── __init__.py              # Package initialization
├── cli.py                   # Main CLI orchestration
├── ui_helper.py             # UI operations and styling
├── framework_selector.py    # Framework selection logic
└── project_manager.py       # Project creation and management
```

## 🛠️ Installation

### From PyPI (Recommended)

```bash
pip install appgen
```

### From Source

```bash
# Clone the repository
git clone https://github.com/yourusername/appgen.git
cd appgen

# Create and activate virtual environment (recommended)
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Upgrade pip
pip install --upgrade pip

# Install in development mode
pip install -e .
```

### Verify Installation

```bash
appgen --help
```

You should see the CLI help with all available commands.

## 🚀 Quick Start

### Interactive Mode (Easiest)

```bash
appgen -i
# or
appgen create --interactive
```

This will guide you through:

1. Framework selection with beautiful tables
2. Feature configuration (TypeScript, Tailwind, etc.)
3. Project directory setup
4. Project generation with progress indicators

### Command Line Mode

```bash
# Create a Next.js project with App Router
appgen create --framework nextjs --dir my-app --router app

# Create an Express project with MongoDB
appgen create --framework express --dir my-api --db mongodb

# Create a React project with TypeScript
appgen create --framework reactjs --dir my-react-app --features typescript
```

## 📚 Usage Examples

### Next.js Projects

```bash
# Basic Next.js with App Router
appgen create --framework nextjs --dir my-next-app --router app

# Next.js with TypeScript and Tailwind
appgen create --framework nextjs --dir my-next-app --router app --features typescript,tailwind

# Next.js with Prisma ORM
appgen create --framework nextjs --dir my-next-app --router app --features typescript,prisma

# Next.js with shadcn/ui components
appgen create --framework nextjs --dir my-next-app --router app --features shadcn

# Next.js with t3 stack (TypeScript + Tailwind + tRPC)
appgen create --framework nextjs --dir my-next-app --router app --features t3
```

### Express.js Projects

```bash
# Basic Express server
appgen create --framework express --dir my-api

# Express with MongoDB
appgen create --framework express --dir my-api --db mongodb

# Express with PostgreSQL
appgen create --framework express --dir my-api --db postgresql

# Express with Supabase
appgen create --framework express --dir my-api --db supabase

# Express with AWS Lambda (serverless)
appgen create --framework express --dir my-api --db serverless
```

### React Projects

```bash
# Basic React app
appgen create --framework reactjs --dir my-react-app

# React with TypeScript
appgen create --framework reactjs --dir my-react-app --features typescript

# React with Tailwind CSS
appgen create --framework reactjs --dir my-react-app --features tailwind

# React with both TypeScript and Tailwind
appgen create --framework reactjs --dir my-react-app --features typescript,tailwind
```

### Python Projects

```bash
# Flask application
appgen create --framework flask --dir my-flask-app

# Django application
appgen create --framework django --dir my-django-app
```

### Svelte Projects

```bash
# Svelte application
appgen create --framework svelte --dir my-svelte-app
```

### Fullstack Presets

```bash
# MERN Stack (MongoDB + Express + React + Node.js)
appgen preset mern --dir my-mern-app

# Next.js Fullstack with Prisma
appgen preset nextjs-fullstack --dir my-nextjs-app
```

### Serverless Projects

```bash
# JavaScript (Node.js) serverless
appgen create --framework serverless --language javascript --dir my-serverless-js

# TypeScript serverless
appgen create --framework serverless --language typescript --dir my-serverless-ts

# Python serverless
appgen create --framework serverless --language python --dir my-serverless-py

# Go serverless
appgen create --framework serverless --language go --dir my-serverless-go
```

## 📋 Available Commands

```bash
# List all available frameworks and features
appgen list-frameworks

# Show current configuration
appgen config

# Create a new project
appgen create [OPTIONS]

# Generate from preset
appgen preset [OPTIONS]

# Interactive mode (shortcut)
appgen -i

# Show help for any command
appgen --help
appgen create --help
appgen preset --help
```

## 🎯 Available Frameworks

### Interactive Frameworks

- **Next.js**: App Router & Pages Router, TypeScript, Tailwind, Prisma, shadcn/ui, t3
- **React**: TypeScript, Tailwind CSS

### Simple Frameworks

- **Express.js**: MongoDB, PostgreSQL, Supabase, AWS Lambda (serverless)
- **Flask**: Lightweight Python web framework
- **Django**: Full-featured Python web framework
- **Svelte**: Cybernetically enhanced web apps

## 🗄️ Database Support

### Express.js Databases

- **MongoDB**: NoSQL database with Mongoose ODM
- **PostgreSQL**: Relational database with Sequelize ORM
- **Supabase**: Open-source Firebase alternative
- **AWS DynamoDB**: Serverless NoSQL database (with SAM template)

## 🎨 Features & Integrations

### Next.js Features

- **App Router**: Next.js 13+ App Router
- **Pages Router**: Traditional Pages Router
- **TypeScript**: Full TypeScript support
- **Tailwind CSS**: Utility-first CSS framework
- **Prisma**: Modern database toolkit
- **shadcn/ui**: Re-usable component library
- **t3**: Type-safe full-stack development with tRPC

### React Features

- **TypeScript**: Type-safe development
- **Tailwind CSS**: Utility-first styling
- **Vite**: Fast build tool

## 🏗️ Generated Project Structure

After generation, your project will include:

```
my-project/
├── README.md           # Project documentation
├── package.json        # Dependencies and scripts
├── .env.example        # Environment variables template
├── .gitignore          # Git ignore rules
├── tsconfig.json       # TypeScript config (if applicable)
├── tailwind.config.js  # Tailwind config (if applicable)
└── src/                # Source code
    ├── components/     # Reusable components
    ├── pages/          # Pages (Next.js Pages Router)
    ├── app/            # App directory (Next.js App Router)
    ├── lib/            # Utility functions
    └── ...
```

## 🚀 Next Steps

After creating your project:

```bash
cd my-project
# For JS/TS: You will be prompted to install dependencies interactively with your choice of npm, yarn, pnpm, or bun (auto-detected)
# For Python: pip install -r requirements.txt
# For Go: go mod tidy
npm run dev  # or python run.py for Python projects
```

## 🖥️ Editor and Package Manager Selection

After project generation (in interactive mode):

- **Editor Selection**: Choose from Visual Studio Code, Cursor, Sublime Text, Atom, Vim, or Nano. The selection table shows an 'Installed?' column (✅/❌) so you can only select editors that are available on your system.
- **Package Manager Selection**: For JS/TS projects, you are prompted to install dependencies. Choose from npm, yarn, pnpm, or bun. Only installed package managers are shown.

Example editor selection table:

| #   | Editor             | Command | Installed? |
| --- | ------------------ | ------- | ---------- |
| 1   | Visual Studio Code | code    | ✅         |
| 2   | Cursor             | cursor  | ✅         |
| 3   | Sublime Text       | subl    | ❌         |
| 4   | Atom               | atom    | ❌         |
| 5   | Vim                | vim     | ✅         |
| 6   | Nano               | nano    | ✅         |

If you select an editor that is not installed, you will be prompted to choose again.

Example package manager selection:

| #   | Package Manager | Installed? |
| --- | --------------- | ---------- |
| 1   | npm             | ✅         |
| 2   | yarn            | ❌         |
| 3   | pnpm            | ✅         |
| 4   | bun             | ❌         |

Only installed package managers are available for selection.

## 🔧 Development

### Local Development Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/appgen.git
cd appgen

# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Upgrade pip
pip install --upgrade pip

# Install development dependencies (includes pre-commit hooks)
make install-dev

# Test the CLI
appgen --help
appgen list-frameworks
```

### Development Commands

```bash
make help              # Show all available commands
make install           # Install package in development mode
make install-dev       # Install development dependencies
make test              # Run tests with coverage
make lint              # Run linting checks
make format            # Format code
make security          # Run security checks
make clean             # Clean build artifacts
make build             # Build package
make ci                # Run all CI checks locally
make pre-commit        # Run pre-commit hooks on all files
```

### Code Quality Tools

- **Black**: Code formatting
- **isort**: Import sorting
- **flake8**: Linting
- **mypy**: Type checking
- **bandit**: Security checks
- **pre-commit**: Git hooks for code quality
- **commitizen**: Conventional commit messages

### Testing

```bash
# Test project generation
appgen create --framework flask --dir test-flask
appgen create --framework express --dir test-express --db mongodb

# Clean up test projects
rm -rf test-flask test-express
```

### Building for Distribution

```bash
# Build package
python -m build

# Install from local build
pip install dist/appgen-*.whl

# Test installed package
appgen --help
```

### Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for detailed information.

Quick start:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Install development dependencies (`make install-dev`)
4. Make your changes
5. Run tests (`make test`) and linting (`make lint`)
6. Commit using conventional commits (`cz commit`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

### CI/CD Pipeline

We use GitHub Actions for continuous integration:

- **Tests**: Run on Python 3.8-3.12
- **Linting**: Code style and type checking
- **Security**: Automated security scans
- **Integration Tests**: Test all framework generations
- **Build**: Package building and validation
- **Release**: Automated PyPI publishing on tags

See [`.github/workflows/`](.github/workflows/) for workflow details.

## 🐛 Troubleshooting

### Common Issues

**CLI not found after installation:**

```bash
# Reinstall in editable mode
pip uninstall appgen -y
pip install -e .
```

**Virtual environment issues:**

```bash
# Remove and recreate virtual environment
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

**Permission errors:**

```bash
# Use user installation
pip install --user appgen
```

## 📝 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🤝 Support

- 📖 [Documentation](https://github.com/yourusername/appgen#readme)
- 🐛 [Report Issues](https://github.com/yourusername/appgen/issues)
- 💡 [Request Features](https://github.com/yourusername/appgen/issues)
- ⭐ [Star the Project](https://github.com/yourusername/appgen)
- 💬 [Discussions](https://github.com/yourusername/appgen/discussions)

## 🙏 Acknowledgments

- Built with [Typer](https://typer.tiangolo.com/) for CLI
- Beautiful UI with [Rich](https://rich.readthedocs.io/)
- Inspired by modern project generators

---

**Happy coding! 🎉**
