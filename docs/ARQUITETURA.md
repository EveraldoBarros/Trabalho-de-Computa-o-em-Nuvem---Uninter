# Arquitetura do CloudFlow SaaS

O CloudFlow SaaS utiliza uma arquitetura cloud-native baseada em containers.

## Camadas

1. Usuário acessa a aplicação pela internet.
2. Load Balancer distribui o tráfego.
3. Kubernetes gerencia os Pods da API.
4. FastAPI processa as requisições.
5. PostgreSQL/RDS persiste os dados.
6. S3 armazena anexos.
7. CloudWatch centraliza logs.
8. IAM controla permissões.

## Conceitos aplicados

- SaaS
- Elasticidade
- Escalabilidade
- Alta disponibilidade
- Containers
- Kubernetes
- Segurança Cloud
- IAM
- Custos Cloud
- Backup
