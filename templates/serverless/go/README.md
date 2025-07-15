# Serverless Go Template

This template provides a starting point for building serverless applications using **Go** on AWS Lambda with the AWS Serverless Application Model (SAM).

## Features

- Go 1.x runtime
- AWS Lambda handler example
- SAM template for deployment
- Example environment file

## Getting Started

### Prerequisites

- [AWS CLI](https://aws.amazon.com/cli/)
- [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
- Go 1.18 or higher

### Setup

1. **Install dependencies**

   ```bash
   cd src
   go mod tidy
   cd ..
   ```

2. **Build the application**

   ```bash
   sam build
   ```

3. **Deploy to AWS**

   ```bash
   sam deploy --guided
   ```

4. **Test locally**

   ```bash
   sam local invoke
   ```

## Project Structure

- `src/main.go` - Main Lambda handler function (Go)
- `template.yaml` - AWS SAM template definition
- `go.mod` - Go module definition
- `env.json` - Example environment variables

## Example Lambda Handler

```
package main

import (
    "context"
    "encoding/json"
    "github.com/aws/aws-lambda-go/lambda"
)

type Response struct {
    StatusCode int    `json:"statusCode"`
    Body       string `json:"body"`
}

func handler(ctx context.Context) (Response, error) {
    body, _ := json.Marshal("Hello from Go Lambda!")
    return Response{
        StatusCode: 200,
        Body:       string(body),
    }, nil
}

func main() {
    lambda.Start(handler)
}
```

## Environment Variables

See `env.json` for an example of how to define environment variables for your Lambda function.

## License

MIT
