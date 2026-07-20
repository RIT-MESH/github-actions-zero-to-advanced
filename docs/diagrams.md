# Diagrams

GitHub-friendly Mermaid diagrams. These render on GitHub directly.

## CI/CD lifecycle

```mermaid
flowchart LR
    A[Code change] --> B[CI: build]
    B --> C[CI: test]
    C --> D{Tests pass?}
    D -- no --> E[Notify & fix]
    D -- yes --> F[CD: package]
    F --> G[Deploy staging]
    G --> H{Approval?}
    H -- approved --> I[Deploy production]
    H -- rejected --> J[Hold]
```

## Workflow structure

```mermaid
flowchart TD
    WF[Workflow file] --> EV[on: events]
    WF --> JB[jobs:]
    JB --> J1[Job 1]
    JB --> J2[Job 2]
    J1 --> S1[steps]
    S1 --> A1[uses: action]
    S1 --> A2[run: command]
```

## Job dependencies (needs)

```mermaid
flowchart LR
    Build --> Test --> Deploy
```

## Reusable workflow call

```mermaid
flowchart LR
    Caller[Caller workflow] -->|workflow_call| Reusable[Reusable workflow]
    Reusable --> Art[artifact]
    Caller -->|download-artifact| Art
```

## Artifact flow

```mermaid
flowchart LR
    J1[Job A] -->|upload-artifact| Store[GitHub artifact storage]
    Store -->|download-artifact| J2[Job B]
```

## Deployment approval flow

```mermaid
flowchart TD
    Build --> Staging[deploy-staging]
    Staging --> Wait{Environment approval}
    Wait -->|approved| Prod[deploy-production]
```

## Final CI/CD pipeline

```mermaid
flowchart LR
    Lint --> TestMatrix[Test matrix]
    TestMatrix --> DockerBuild[Docker build]
    DockerBuild --> SecScan[Security scan]
    SecScan --> Release[Release on tag]
    Release --> ProdDeploy[Production deploy]
```

## Debugging decision tree

```mermaid
flowchart TD
    Fail[Run failed] --> Open[Open Actions tab]
    Open --> Step[Click failing step]
    Step --> Read[Read last log lines]
    Read --> Cause{Root cause?}
    Cause --> Checkout[Add actions/checkout]
    Cause --> Perm[Add permission]
    Cause --> Deps[Install dependencies]
    Cause --> Debug[Enable debug logging]
```
