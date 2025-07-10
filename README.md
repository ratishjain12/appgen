# AppGen 🚀

A modern project generator CLI for web frameworks. Quickly scaffold projects for Next.js, React, Express, Flask, Django, and more with support for TypeScript, Tailwind CSS, databases, and modern tooling.

## ✨ Features

- **Multiple Frameworks**: Next.js, React, Express, Flask, Django, Svelte
- **Database Support**: MongoDB, PostgreSQL, Supabase, AWS DynamoDB
- **Modern Tooling**: TypeScript, Tailwind CSS, Prisma ORM, shadcn/ui
- **Interactive CLI**: Guided setup with beautiful UI
- **Serverless Ready**: AWS SAM templates for serverless deployment
- **Fullstack Presets**: MERN stack, Next.js + Prisma, and more
- **Clean Architecture**: Modular, maintainable codebase

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

# Install in development mode
pip install -e .
```

### Verify Installation

```bash
appgen --help
```

## 🚀 Quick Start

### Interactive Mode (Easiest)

```bash
appgen -i
# or
appgen create --interactive
```

This will guide you through:

1. Framework selection
2. Feature configuration
3. Project directory setup
4. Project generation

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
```

### Python Projects

```bash
# Flask application
appgen create --framework flask --dir my-flask-app

# Django application
appgen create --framework django --dir my-django-app
```

### Fullstack Presets

```bash
# MERN Stack (MongoDB + Express + React + Node.js)
appgen preset mern --dir my-mern-app

# Next.js Fullstack with Prisma
appgen preset nextjs-fullstack --dir my-nextjs-app
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
```

## 🎯 Available Frameworks

### Interactive Frameworks

- **Next.js**: App Router & Pages Router, TypeScript, Tailwind, Prisma, shadcn/ui
- **React**: TypeScript, Tailwind CSS

### Simple Frameworks

- **Express.js**: MongoDB, PostgreSQL, Supabase, AWS Lambda
- **Flask**: Lightweight Python web framework
- **Django**: Full-featured Python web framework
- **Svelte**: Cybernetically enhanced web apps

## 🗄️ Database Support

### Express.js Databases

- **MongoDB**: NoSQL database with Mongoose ODM
- **PostgreSQL**: Relational database with Sequelize ORM
- **Supabase**: Open-source Firebase alternative
- **AWS DynamoDB**: Serverless NoSQL database (with SAM)

## 🎨 Features & Integrations

### Next.js Features

- **App Router**: Next.js 13+ App Router
- **Pages Router**: Traditional Pages Router
- **TypeScript**: Full TypeScript support
- **Tailwind CSS**: Utility-first CSS framework
- **Prisma**: Modern database toolkit
- **shadcn/ui**: Re-usable component library
- **t3**: Type-safe full-stack development

### React Features

- **TypeScript**: Type-safe development
- **Tailwind CSS**: Utility-first styling
- **Vite**: Fast build tool

## 🏗️ Project Structure

After generation, your project will include:

```
my-project/
├── README.md           # Project documentation
├── package.json        # Dependencies and scripts
├── .env.example        # Environment variables template
├── .gitignore          # Git ignore rules
└── src/                # Source code
    ├── components/     # Reusable components
    ├── pages/          # Pages (Next.js Pages Router)
    ├── app/            # App directory (Next.js App Router)
    └── ...
```

## 🚀 Next Steps

After creating your project:

```bash
cd my-project
npm install
npm run dev
```

## 🔧 Development

### Local Development Setup

```bash
# Clone and install
git clone https://github.com/yourusername/appgen.git
cd appgen
pip install -e .

# Run tests
python -m pytest

# Build package
python -m build

# Install from local build
pip install dist/appgen-*.whl
```

### Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📝 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🤝 Support

- 📖 [Documentation](https://github.com/yourusername/appgen#readme)
- 🐛 [Report Issues](https://github.com/yourusername/appgen/issues)
- 💡 [Request Features](https://github.com/yourusername/appgen/issues)
- ⭐ [Star the Project](https://github.com/yourusername/appgen)

---

**Happy coding! 🎉**
