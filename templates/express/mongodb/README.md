# Express.js with MongoDB

This template provides a complete Express.js setup with MongoDB database integration using Mongoose ODM.

## Features

- ✅ Express.js server with security middleware
- ✅ MongoDB database with Mongoose ODM
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
   # Create .env file with your MongoDB connection string
   echo "MONGODB_URI=mongodb://localhost:27017/express_app" > .env
   ```

3. **Set up MongoDB:**

   ```bash
   # Start MongoDB locally
   mongod

   # Or use MongoDB Atlas (cloud)
   # Update MONGODB_URI in .env with your Atlas connection string
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

The application uses Mongoose ODM with MongoDB. The database connection is configured via the `MONGODB_URI` environment variable.

### Example MONGODB_URI formats:

- Local: `mongodb://localhost:27017/database_name`
- MongoDB Atlas: `mongodb+srv://username:password@cluster.mongodb.net/database_name`
- Docker: `mongodb://mongo:27017/database_name`

## Environment Variables

| Variable      | Description               | Default                                 |
| ------------- | ------------------------- | --------------------------------------- |
| `PORT`        | Server port               | `3000`                                  |
| `MONGODB_URI` | MongoDB connection string | `mongodb://localhost:27017/express_app` |

## Adding New Models

To add new models, create them in the `src/index.js` file or create separate model files:

```javascript
const productSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
  },
  price: {
    type: Number,
    required: true,
  },
  createdAt: {
    type: Date,
    default: Date.now,
  },
});

const Product = mongoose.model("Product", productSchema);
```

## MongoDB Features

- **Document-based**: Store data as JSON-like documents
- **Schema-less**: Flexible data structure
- **Scalable**: Horizontal scaling with sharding
- **Aggregation**: Powerful data processing pipeline
- **Indexing**: Fast query performance

## Deployment

This template is ready for deployment on platforms like:

- Heroku
- Railway
- Render
- DigitalOcean App Platform
- Vercel (with MongoDB Atlas)

Make sure to set the `MONGODB_URI` environment variable in your deployment platform.

## MongoDB Atlas Setup

1. Go to [MongoDB Atlas](https://www.mongodb.com/atlas)
2. Create a free cluster
3. Get your connection string
4. Update your `.env` file:

```env
MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/express_app
```

## Database Operations

The template includes basic CRUD operations:

```javascript
// Create
const user = new User({ name: "John", email: "john@example.com" });
await user.save();

// Read
const users = await User.find();
const user = await User.findById(id);

// Update
await User.findByIdAndUpdate(id, { name: "Jane" });

// Delete
await User.findByIdAndDelete(id);
```
