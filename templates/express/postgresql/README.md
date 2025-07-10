# Express.js with PostgreSQL

This template provides a complete Express.js setup with PostgreSQL database integration using Sequelize ORM.

## Features

- ✅ Express.js server with security middleware
- ✅ PostgreSQL database with Sequelize ORM
- ✅ User model with CRUD operations
- ✅ Environment variable configuration
- ✅ CORS enabled
- ✅ Helmet security headers
- ✅ Morgan logging

## Quick Start

1. **Install dependencies:**

   ```bash
   npm install
   ```

2. **Set up environment variables:**

   ```bash
   cp env.example .env
   # Edit .env with your database credentials
   ```

3. **Set up PostgreSQL database:**

   ```bash
   # Create database
   createdb express_app

   # Or use your preferred method to create the database
   ```

4. **Start the server:**

   ```bash
   # Development mode
   npm run dev

   # Production mode
   npm start
   ```

## API Endpoints

- `GET /` - Health check
- `GET /api/users` - Get all users
- `POST /api/users` - Create a new user
- `GET /api/users/:id` - Get user by ID

## Database Configuration

The application uses Sequelize ORM with PostgreSQL. The database connection is configured via the `DATABASE_URL` environment variable.

### Example DATABASE_URL formats:

- Local: `postgresql://username:password@localhost:5432/database_name`
- Heroku: `postgresql://username:password@host:port/database_name`
- Railway: `postgresql://username:password@host:port/database_name`

## Environment Variables

| Variable       | Description                  | Default                                   |
| -------------- | ---------------------------- | ----------------------------------------- |
| `PORT`         | Server port                  | `3000`                                    |
| `DATABASE_URL` | PostgreSQL connection string | `postgresql://localhost:5432/express_app` |

## Adding New Models

To add new models, create them in the `src/index.js` file or create separate model files:

```javascript
const Product = sequelize.define("Product", {
  id: {
    type: Sequelize.INTEGER,
    primaryKey: true,
    autoIncrement: true,
  },
  name: {
    type: Sequelize.STRING,
    allowNull: false,
  },
  price: {
    type: Sequelize.DECIMAL(10, 2),
    allowNull: false,
  },
});
```

## Deployment

This template is ready for deployment on platforms like:

- Heroku
- Railway
- Render
- DigitalOcean App Platform

Make sure to set the `DATABASE_URL` environment variable in your deployment platform.
