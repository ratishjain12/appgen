# Express.js Serverless with AWS SAM

This template provides a complete Express.js serverless application using AWS SAM (Serverless Application Model) with DynamoDB integration.

## 🚀 Features

- ✅ Express.js server wrapped for AWS Lambda
- ✅ AWS SAM template with complete infrastructure
- ✅ DynamoDB integration with AWS SDK v3
- ✅ API Gateway with CORS support
- ✅ CloudWatch logging
- ✅ Local development with SAM CLI
- ✅ Environment-based configuration
- ✅ Security middleware (Helmet, CORS)
- ✅ Comprehensive error handling
- ✅ Health check endpoints

## 📋 Prerequisites

1. **AWS CLI** - [Install AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
2. **AWS SAM CLI** - [Install SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
3. **Node.js 18+** - [Install Node.js](https://nodejs.org/)
4. **AWS Account** - [Create AWS Account](https://aws.amazon.com/)

## 🛠️ Quick Start

### 1. Install Dependencies

```bash
npm install
```

### 2. Set up Environment Variables

```bash
cp env.example .env
# Edit .env with your AWS credentials
```

### 3. Local Development

```bash
# Start local API Gateway
npm run local

# Or run Express directly
npm run dev
```

### 4. Build and Deploy

```bash
# Build the application
npm run build

# Deploy to AWS (guided mode)
npm run deploy

# Deploy to production
npm run deploy:prod
```

## 🏗️ Infrastructure

The SAM template creates:

- **API Gateway** - REST API with CORS support
- **Lambda Function** - Express.js application
- **DynamoDB Table** - User data storage
- **CloudWatch Logs** - Application logging
- **IAM Roles** - Proper permissions

### Resources Created:

- `ExpressApi` - API Gateway
- `ExpressFunction` - Lambda function
- `UsersTable` - DynamoDB table
- `ExpressFunctionLogGroup` - CloudWatch logs

## 📡 API Endpoints

| Method   | Endpoint         | Description                   |
| -------- | ---------------- | ----------------------------- |
| `GET`    | `/`              | Health check                  |
| `GET`    | `/health`        | Detailed health check with DB |
| `GET`    | `/api/users`     | Get all users                 |
| `POST`   | `/api/users`     | Create a new user             |
| `GET`    | `/api/users/:id` | Get user by ID                |
| `PUT`    | `/api/users/:id` | Update user                   |
| `DELETE` | `/api/users/:id` | Delete user                   |

### Example Requests

**Create User:**

```bash
curl -X POST https://your-api-gateway-url/dev/api/users \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "email": "john@example.com"}'
```

**Get Users:**

```bash
curl https://your-api-gateway-url/dev/api/users
```

## 🔧 Configuration

### Environment Variables

| Variable      | Description         | Default           |
| ------------- | ------------------- | ----------------- |
| `AWS_REGION`  | AWS region          | `us-east-1`       |
| `USERS_TABLE` | DynamoDB table name | `dev-users-table` |
| `ENVIRONMENT` | Environment name    | `dev`             |
| `NODE_ENV`    | Node environment    | `development`     |

### SAM Configuration

The `samconfig.toml` file contains deployment settings:

- Stack name: `express-serverless-app`
- Region: `us-east-1`
- Environment: `dev`

## 🚀 Deployment

### First Deployment

```bash
npm run deploy
```

This will:

1. Build the application
2. Create S3 bucket for artifacts
3. Deploy CloudFormation stack
4. Create all AWS resources

### Subsequent Deployments

```bash
npm run deploy:prod
```

### Environment-Specific Deployments

```bash
# Deploy to staging
sam deploy --parameter-overrides Environment=staging

# Deploy to production
sam deploy --parameter-overrides Environment=prod
```

## 🔍 Monitoring

### View Logs

```bash
npm run logs
```

### CloudWatch Dashboard

- Go to AWS CloudWatch console
- View Lambda function logs
- Monitor API Gateway metrics
- Check DynamoDB performance

## 🧪 Testing

### Local Testing

```bash
# Test with SAM local
npm run local

# Test specific function
npm run invoke
```

### API Testing

```bash
# Health check
curl http://localhost:3000/health

# Create user
curl -X POST http://localhost:3000/api/users \
  -H "Content-Type: application/json" \
  -d '{"name": "Test User", "email": "test@example.com"}'
```

## 🔒 Security

- **Helmet** - Security headers
- **CORS** - Cross-origin resource sharing
- **IAM Roles** - Least privilege access
- **DynamoDB Encryption** - Server-side encryption
- **API Gateway** - Request validation

## 💰 Cost Optimization

- **DynamoDB** - Pay-per-request billing
- **Lambda** - Pay only for execution time
- **API Gateway** - Pay per request
- **CloudWatch** - Basic monitoring included

## 🛠️ Development Workflow

1. **Local Development:**

   ```bash
   npm run dev
   ```

2. **Test with SAM:**

   ```bash
   npm run local
   ```

3. **Build:**

   ```bash
   npm run build
   ```

4. **Deploy:**
   ```bash
   npm run deploy
   ```

## 📚 Additional Resources

- [AWS SAM Documentation](https://docs.aws.amazon.com/serverless-application-model/)
- [DynamoDB Best Practices](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/best-practices.html)
- [Lambda Best Practices](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html)
- [API Gateway Documentation](https://docs.aws.amazon.com/apigateway/)

## 🐛 Troubleshooting

### Common Issues

1. **Permission Denied:**

   - Ensure AWS credentials are configured
   - Check IAM permissions

2. **DynamoDB Connection Error:**

   - Verify table exists
   - Check region configuration

3. **Cold Start Issues:**

   - Use provisioned concurrency
   - Optimize package size

4. **CORS Errors:**
   - Check API Gateway CORS settings
   - Verify frontend origin

### Debug Commands

```bash
# Check SAM version
sam --version

# Validate template
sam validate

# Check AWS credentials
aws sts get-caller-identity
```
