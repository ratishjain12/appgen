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