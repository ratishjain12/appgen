# Contributing to AppGen 🚀

Thank you for your interest in contributing to AppGen! This document provides guidelines and information for contributors.

## 🤝 How to Contribute

### 1. Fork and Clone

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/yourusername/appgen.git
   cd appgen
   ```

### 2. Set Up Development Environment

```bash
# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install development dependencies
make install-dev
```

### 3. Make Your Changes

1. Create a feature branch:

   ```bash
   git checkout -b feature/amazing-feature
   ```

2. Make your changes following the coding standards below

3. Test your changes:
   ```bash
   make test
   make lint
   ```

### 4. Commit Your Changes

We use [Conventional Commits](https://www.conventionalcommits.org/) for commit messages:

```bash
# Examples of good commit messages:
feat: add support for Vue.js framework
fix: resolve issue with Express MongoDB template
docs: update README with new installation instructions
test: add tests for framework selector
refactor: improve CLI error handling
```

### 5. Push and Create Pull Request

```bash
git push origin feature/amazing-feature
```

Then create a Pull Request on GitHub.

## 🛠️ Development Setup

### Prerequisites

- Python 3.8 or higher
- Git
- Make (optional, for using Makefile commands)

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/appgen.git
cd appgen

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install in development mode
make install-dev
```

### Available Commands

```bash
make help              # Show all available commands
make install           # Install package in development mode
make install-dev       # Install development dependencies
make test              # Run tests
make lint              # Run linting checks
make format            # Format code
make security          # Run security checks
make clean             # Clean build artifacts
make build             # Build package
make ci                # Run all CI checks locally
```

## 📋 Coding Standards

### Code Style

We use several tools to maintain code quality:

- **Black**: Code formatting
- **isort**: Import sorting
- **flake8**: Linting
- **mypy**: Type checking
- **bandit**: Security checks

### Pre-commit Hooks

Pre-commit hooks are automatically installed with `make install-dev`. They run:

- Code formatting (Black)
- Import sorting (isort)
- Linting (flake8)
- Type checking (mypy)
- Security checks (bandit)
- YAML/Markdown formatting (Prettier)

### Running Checks Manually

```bash
# Format code
make format

# Check code style
make lint

# Run tests
make test

# Run all checks
make ci
```

## 🧪 Testing

### Running Tests

```bash
# Run all tests
make test

# Run tests with coverage
pytest tests/ --cov=appgen --cov-report=html

# Run specific test file
pytest tests/test_cli.py

# Run tests in watch mode
make test-watch
```

### Writing Tests

- Place tests in the `tests/` directory
- Use descriptive test names
- Test both success and failure cases
- Use fixtures for common setup
- Aim for good test coverage

### Test Structure

```
tests/
├── __init__.py
├── test_cli.py          # CLI functionality tests
├── test_config.py       # Configuration tests
├── test_generator.py    # Project generation tests
└── conftest.py          # Shared fixtures
```

## 🔧 Adding New Features

### Adding a New Framework

1. **Create Template**: Add template files in `templates/framework-name/`
2. **Update Configuration**: Add framework config in `appgen.config.yaml`
3. **Update Generator**: Modify `generator/generate.py` if needed
4. **Add Tests**: Create tests for the new framework
5. **Update Documentation**: Update README and docs

### Adding New Features to Existing Frameworks

1. **Create Feature Template**: Add feature-specific templates
2. **Update Framework Config**: Add feature to framework configuration
3. **Update Generator Logic**: Modify generation logic
4. **Add Tests**: Test the new feature
5. **Update Documentation**: Document the new feature

## 🐛 Bug Reports

When reporting bugs, please include:

1. **Environment**: OS, Python version, AppGen version
2. **Steps to Reproduce**: Clear, step-by-step instructions
3. **Expected Behavior**: What you expected to happen
4. **Actual Behavior**: What actually happened
5. **Error Messages**: Full error messages and stack traces
6. **Additional Context**: Any relevant information

## 💡 Feature Requests

When requesting features, please include:

1. **Description**: Clear description of the feature
2. **Use Case**: Why this feature would be useful
3. **Implementation Ideas**: Any thoughts on implementation
4. **Examples**: Similar features in other tools

## 📝 Pull Request Guidelines

### Before Submitting

1. **Test Your Changes**: Run all tests and checks
2. **Update Documentation**: Update README, docs, and comments
3. **Follow Style Guide**: Ensure code follows our style guidelines
4. **Write Tests**: Add tests for new functionality
5. **Update Version**: Update version if needed

### PR Template

```markdown
## Description

Brief description of changes

## Type of Change

- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing

- [ ] Tests pass
- [ ] Manual testing completed
- [ ] No breaking changes

## Checklist

- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] Tests added/updated
```

## 🚀 Release Process

### For Maintainers

1. **Update Version**: Use commitizen to bump version

   ```bash
   make bump-patch  # or bump-minor, bump-major
   ```

2. **Create Release**: Push tag to trigger GitHub Actions

   ```bash
   git push --tags
   ```

3. **Verify Release**: Check PyPI and GitHub releases

### Version Bumping

- **Patch**: Bug fixes and minor improvements
- **Minor**: New features, backward compatible
- **Major**: Breaking changes

## 📞 Getting Help

- **Issues**: Use GitHub Issues for bugs and feature requests
- **Discussions**: Use GitHub Discussions for questions and ideas
- **Documentation**: Check the README and inline documentation

## 🎉 Recognition

Contributors will be recognized in:

- GitHub contributors list
- Release notes
- Project documentation

Thank you for contributing to AppGen! 🚀
