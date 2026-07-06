# CloudFlow SaaS

CloudFlow SaaS é um projeto cloud-native original para a disciplina de Computação em Nuvem.

O sistema simula uma plataforma SaaS para **gestão de fluxos de trabalho, solicitações internas e anexos de equipes**, usando API REST, banco SQL, containers, Kubernetes e serviços AWS.

> Este projeto foi criado como uma nova proposta acadêmica e não reutiliza os dados, nome, entidades ou domínio do projeto de exemplo.

---

## Objetivo

Desenvolver um mini SaaS moderno com arquitetura em nuvem, contendo:

- Cadastro de usuários
- Login simples
- CRUD de fluxos/processos
- Status e prioridade
- Upload de anexos
- API REST documentada
- Persistência em PostgreSQL
- Containerização com Docker
- Deploy em Kubernetes
- Integração planejada com AWS RDS, S3, EKS, IAM e CloudWatch

---

## Tecnologias

- Python 3.12
- FastAPI
- SQLAlchemy
- PostgreSQL
- Docker
- Docker Compose
- Kubernetes
- Amazon RDS
- Amazon S3
- Amazon EKS
- IAM
- GitHub

---

## Arquitetura

```text
Usuário / Internet
        ↓
Load Balancer
        ↓
Kubernetes / EKS
        ↓
Pods com FastAPI
        ↓
PostgreSQL / RDS
        ↓
Amazon S3 para anexos
        ↓
CloudWatch Logs
        ↓
IAM e Security Groups
```

---

## Estrutura do Projeto

```text
cloudflow-saas/
├── app/
│   ├── api/
│   ├── core/
│   ├── models/
│   ├── schemas/
│   └── services/
├── docs/
├── k8s/
├── scripts/
├── tests/
├── .env.example
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## Como executar localmente

### 1. Copiar variáveis de ambiente

```bash
cp .env.example .env
```

### 2. Subir com Docker Compose

```bash
docker compose up --build
```

### 3. Acessar a API

```text
http://localhost:8000
```

Documentação Swagger:

```text
http://localhost:8000/docs
```

---

## Rotas principais

### Usuários

```http
POST /users
GET /users
```

### Autenticação

```http
POST /auth/login
```

### Fluxos de trabalho

```http
POST /workflows
GET /workflows
GET /workflows/{workflow_id}
PUT /workflows/{workflow_id}
DELETE /workflows/{workflow_id}
```

### Uploads

```http
POST /uploads/{workflow_id}
GET /uploads
```

### Saúde da aplicação

```http
GET /health
```

---

## Deploy com Kubernetes

Gerar imagem:

```bash
docker build -t cloudflow-saas:1.0 .
```

Aplicar arquivos Kubernetes:

```bash
kubectl apply -f k8s/configmap.yaml
kubectl apply -f k8s/secret.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/hpa.yaml
```

---

## Deploy em AWS

Para uma entrega completa na AWS, utilize:

- **Amazon EKS** para executar Kubernetes
- **Amazon RDS PostgreSQL** para banco gerenciado
- **Amazon S3** para anexos
- **IAM** para permissões
- **CloudWatch** para logs
- **Security Groups** para controle de acesso

---

## Sugestão de evidências para o relatório

Inclua capturas de tela de:

- API rodando localmente
- Swagger funcionando
- Docker build
- Docker Compose executando
- Pods Kubernetes ativos
- Service Kubernetes exposto
- Banco PostgreSQL conectado
- Bucket S3 criado
- Repositório GitHub
- Deploy em cloud

---

## Licença

MIT
