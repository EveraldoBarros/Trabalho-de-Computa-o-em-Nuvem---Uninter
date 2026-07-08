# CloudFlow SaaS

CloudFlow SaaS é uma aplicação desenvolvida para a disciplina de **Computação em Nuvem**, com o objetivo de demonstrar a construção de uma solução baseada em arquitetura **cloud-native** utilizando containers, Kubernetes e boas práticas de desenvolvimento de APIs REST.

A aplicação simula uma plataforma SaaS para gerenciamento de fluxos de trabalho, permitindo o cadastro de usuários, autenticação, gerenciamento de processos, definição de prioridades e upload de arquivos.

---

# Objetivos do Projeto

O projeto foi desenvolvido para aplicar, na prática, os principais conceitos estudados na disciplina de Computação em Nuvem, incluindo:

- Desenvolvimento de APIs REST;
- Containerização de aplicações;
- Orquestração utilizando Kubernetes;
- Persistência de dados em banco relacional;
- Versionamento utilizando Git e GitHub;
- Preparação para implantação em ambientes de nuvem.

---

# Funcionalidades

- Cadastro de usuários;
- Autenticação de usuários;
- CRUD de fluxos de trabalho;
- Controle de status e prioridade;
- Upload de anexos;
- Documentação automática da API (Swagger/OpenAPI);
- Persistência em banco PostgreSQL.

---

# Tecnologias Utilizadas

## Linguagem

- Python 3.12

## Framework

- FastAPI

## Banco de Dados

- PostgreSQL 16

## ORM

- SQLAlchemy

## Containers

- Docker
- Docker Compose

## Orquestração

- Kubernetes

## Documentação

- Swagger / OpenAPI

## Controle de versão

- Git
- GitHub

## Preparação para Cloud

- Amazon S3
- Amazon RDS
- Amazon EKS
- AWS IAM

---

# Pré-requisitos

Antes de executar o projeto, instale os seguintes softwares.

## Python

Download:

https://www.python.org/downloads/

Verificar instalação:

```bash
python --version
```

---

## Git

Download:

https://git-scm.com/downloads

Verificar instalação:

```bash
git --version
```

---

## Docker Desktop

Download:

https://www.docker.com/products/docker-desktop/

Após instalar:

```bash
docker --version
docker compose version
```

---

## Kubernetes

Neste projeto foi utilizado o Kubernetes disponibilizado pelo próprio Docker Desktop.

Após habilitar o Kubernetes:

```bash
kubectl version
kubectl get nodes
```

---

# Clonando o Projeto

```bash
git clone https://github.com/EveraldoBarros/Trabalho-de-Computa-o-em-Nuvem---Uninter.git

cd Trabalho-de-Computa-o-em-Nuvem---Uninter
```

---

# Configuração

Copie o arquivo de exemplo:

```bash
cp .env.example .env
```

Caso utilize Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

Ou simplesmente copie o arquivo manualmente.

---

# Executando o Projeto

## Construindo os containers

```bash
docker compose build
```

---

## Iniciando os containers

```bash
docker compose up
```

ou

```bash
docker compose up --build
```

---

## Verificando os containers

```bash
docker ps
```

---

# Acessando a Aplicação

API:

```
http://localhost:8000
```

Swagger:

```
http://localhost:8000/docs
```

OpenAPI:

```
http://localhost:8000/openapi.json
```

---

# Endpoints

## Autenticação

```
POST /auth/login
```

---

## Usuários

```
GET /users
POST /users
```

---

## Workflows

```
GET /workflows
POST /workflows
GET /workflows/{id}
PUT /workflows/{id}
DELETE /workflows/{id}
```

---

## Uploads

```
POST /uploads/{workflow_id}
GET /uploads
```

---

## Health Check

```
GET /health
```

---

# Estrutura do Projeto

```text
cloudflow-saas/

app/
│
├── api/
├── core/
├── models/
├── schemas/
├── services/

docs/

k8s/

scripts/

tests/

uploads/

Dockerfile

docker-compose.yml

requirements.txt

README.md

.env.example
```

---

# Implantação com Kubernetes

Aplicar os manifestos:

```bash
kubectl apply -f k8s/
```

Verificar os recursos:

```bash
kubectl get nodes

kubectl get deployments

kubectl get services

kubectl get configmaps

kubectl get secrets

kubectl get hpa
```

Verificar os Pods:

```bash
kubectl get pods
```

---

# Arquitetura

```text
                 Usuário

                    │

             HTTP / REST API

                    │

              FastAPI (Docker)

                    │

             Kubernetes Cluster

                    │

             PostgreSQL Database

                    │

           Upload de Arquivos
```

---

# Futuras Integrações em Nuvem

A arquitetura foi preparada para futura utilização dos seguintes serviços AWS:

- Amazon S3
- Amazon RDS PostgreSQL
- Amazon EKS
- AWS IAM
- Amazon CloudWatch

---

# Repositório

Projeto disponível em:

https://github.com/EveraldoBarros/Trabalho-de-Computa-o-em-Nuvem---Uninter

---

# Autor

José Everaldo de Barros

RU: 4972245

Disciplina: Computação em Nuvem

Centro Universitário Internacional UNINTER

---

# Licença

MIT License