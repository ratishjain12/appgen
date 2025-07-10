const express = require("express");
const cors = require("cors");
const { Sequelize } = require("sequelize");
const helmet = require("helmet");
const morgan = require("morgan");
require("dotenv").config();

const app = express();
const PORT = process.env.PORT || 3000;

// Database configuration
const DATABASE_URL =
  process.env.DATABASE_URL || "postgresql://localhost:5432/express_app";

// Initialize Sequelize
const sequelize = new Sequelize(DATABASE_URL, {
  dialect: "postgres",
  logging: false, // Set to console.log to see SQL queries
  pool: {
    max: 5,
    min: 0,
    acquire: 30000,
    idle: 10000,
  },
});

// Middleware
app.use(helmet());
app.use(cors());
app.use(express.json());
app.use(morgan("combined"));

// Test database connection
async function testConnection() {
  try {
    await sequelize.authenticate();
    console.log("✅ Connected to PostgreSQL database");
  } catch (error) {
    console.error("❌ PostgreSQL connection error:", error);
  }
}

// Sample User model
const User = sequelize.define("User", {
  id: {
    type: Sequelize.INTEGER,
    primaryKey: true,
    autoIncrement: true,
  },
  name: {
    type: Sequelize.STRING,
    allowNull: false,
  },
  email: {
    type: Sequelize.STRING,
    allowNull: false,
    unique: true,
    validate: {
      isEmail: true,
    },
  },
  createdAt: {
    type: Sequelize.DATE,
    defaultValue: Sequelize.NOW,
  },
  updatedAt: {
    type: Sequelize.DATE,
    defaultValue: Sequelize.NOW,
  },
});

// Sync database (create tables if they don't exist)
sequelize
  .sync({ force: false })
  .then(() => {
    console.log("📊 Database synchronized");
  })
  .catch((error) => {
    console.error("❌ Database sync error:", error);
  });

// Routes
app.get("/", (req, res) => {
  res.json({ message: "Express API with PostgreSQL" });
});

// User routes
app.get("/api/users", async (req, res) => {
  try {
    const users = await User.findAll();
    res.json(users);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

app.post("/api/users", async (req, res) => {
  try {
    const { name, email } = req.body;
    const user = await User.create({ name, email });
    res.status(201).json(user);
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

app.get("/api/users/:id", async (req, res) => {
  try {
    const user = await User.findByPk(req.params.id);
    if (user) {
      res.json(user);
    } else {
      res.status(404).json({ error: "User not found" });
    }
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Start server
app.listen(PORT, async () => {
  await testConnection();
  console.log(`🚀 Server running on port ${PORT}`);
  console.log(`📊 Database URL: ${DATABASE_URL}`);
});
