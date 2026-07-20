# Solution 14 — Docker

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY app.py .
CMD ["python", "-c", "print('Hello from the image'); import app; app.main()"]
```

The greeting prints before the sum.