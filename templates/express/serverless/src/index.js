const express = require("express");
const cors = require("cors");
const helmet = require("helmet");
const morgan = require("morgan");
const serverless = require("serverless-http");
const { DynamoDBClient } = require("@aws-sdk/client-dynamodb");
const {
  DynamoDBDocumentClient,
  GetCommand,
  PutCommand,
  QueryCommand,
  DeleteCommand,
  ScanCommand,
} = require("@aws-sdk/lib-dynamodb");
const { v4: uuidv4 } = require("uuid");

const app = express();
const PORT = process.env.PORT || 3000;

// DynamoDB Configuration
const dynamoClient = new DynamoDBClient({
  region: process.env.AWS_REGION || "us-east-1",
});

const docClient = DynamoDBDocumentClient.from(dynamoClient);
const USERS_TABLE = process.env.USERS_TABLE || "dev-users-table";

// Middleware
app.use(helmet());
app.use(cors());
app.use(express.json());
app.use(morgan("combined"));

// Health check
app.get("/", (req, res) => {
  res.json({
    message: "Express Serverless API",
    environment: process.env.ENVIRONMENT || "dev",
    timestamp: new Date().toISOString(),
  });
});

// Health check with DynamoDB connection
app.get("/health", async (req, res) => {
  try {
    // Test DynamoDB connection
    await docClient.send(
      new ScanCommand({
        TableName: USERS_TABLE,
        Limit: 1,
      })
    );

    res.json({
      status: "healthy",
      database: "connected",
      environment: process.env.ENVIRONMENT || "dev",
    });
  } catch (error) {
    console.error("Health check failed:", error);
    res.status(500).json({
      status: "unhealthy",
      database: "disconnected",
      error: error.message,
    });
  }
});

// User routes
app.get("/api/users", async (req, res) => {
  try {
    const { Items } = await docClient.send(
      new ScanCommand({
        TableName: USERS_TABLE,
      })
    );

    res.json(Items || []);
  } catch (error) {
    console.error("Error fetching users:", error);
    res.status(500).json({ error: error.message });
  }
});

app.post("/api/users", async (req, res) => {
  try {
    const { name, email } = req.body;

    if (!name || !email) {
      return res.status(400).json({ error: "Name and email are required" });
    }

    const user = {
      id: uuidv4(),
      name,
      email,
      createdAt: new Date().toISOString(),
      updatedAt: new Date().toISOString(),
    };

    await docClient.send(
      new PutCommand({
        TableName: USERS_TABLE,
        Item: user,
      })
    );

    res.status(201).json(user);
  } catch (error) {
    console.error("Error creating user:", error);
    res.status(500).json({ error: error.message });
  }
});

app.get("/api/users/:id", async (req, res) => {
  try {
    const { Item } = await docClient.send(
      new GetCommand({
        TableName: USERS_TABLE,
        Key: { id: req.params.id },
      })
    );

    if (!Item) {
      return res.status(404).json({ error: "User not found" });
    }

    res.json(Item);
  } catch (error) {
    console.error("Error fetching user:", error);
    res.status(500).json({ error: error.message });
  }
});

app.put("/api/users/:id", async (req, res) => {
  try {
    const { name, email } = req.body;

    // Check if user exists
    const { Item } = await docClient.send(
      new GetCommand({
        TableName: USERS_TABLE,
        Key: { id: req.params.id },
      })
    );

    if (!Item) {
      return res.status(404).json({ error: "User not found" });
    }

    const updatedUser = {
      ...Item,
      name: name || Item.name,
      email: email || Item.email,
      updatedAt: new Date().toISOString(),
    };

    await docClient.send(
      new PutCommand({
        TableName: USERS_TABLE,
        Item: updatedUser,
      })
    );

    res.json(updatedUser);
  } catch (error) {
    console.error("Error updating user:", error);
    res.status(500).json({ error: error.message });
  }
});

app.delete("/api/users/:id", async (req, res) => {
  try {
    // Check if user exists
    const { Item } = await docClient.send(
      new GetCommand({
        TableName: USERS_TABLE,
        Key: { id: req.params.id },
      })
    );

    if (!Item) {
      return res.status(404).json({ error: "User not found" });
    }

    await docClient.send(
      new DeleteCommand({
        TableName: USERS_TABLE,
        Key: { id: req.params.id },
      })
    );

    res.json({ message: "User deleted successfully" });
  } catch (error) {
    console.error("Error deleting user:", error);
    res.status(500).json({ error: error.message });
  }
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error("Unhandled error:", err);
  res.status(500).json({ error: "Internal server error" });
});

// 404 handler
app.use((req, res) => {
  res.status(404).json({ error: "Route not found" });
});

// Local development server
if (process.env.NODE_ENV !== "production") {
  app.listen(PORT, () => {
    console.log(`🚀 Server running on port ${PORT}`);
    console.log(`📊 DynamoDB Table: ${USERS_TABLE}`);
    console.log(`🌍 Environment: ${process.env.ENVIRONMENT || "dev"}`);
  });
}

// Export handler for AWS Lambda
module.exports.handler = serverless(app);
