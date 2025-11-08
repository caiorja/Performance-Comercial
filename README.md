# Performance Comercial — Dashboard Power BI (PBIP)

Este repositório contém o projeto Power BI em formato PBIP do dashboard "Performance Comercial".
Ele segue o padrão do repositório "Investimentos" para facilitar versionamento, colaboração e reprodução do ambiente.

## Visualização online

Veja o dashboard publicado no Power BI Service:

https://app.powerbi.com/view?r=eyJrIjoiNzk3NDYyMTQtZjgwYi00YmQwLWJlY2UtNGY4MTYxY2E1OTY5IiwidCI6IjA5ZjRiZmNhLTY3Y2QtNGU0Zi05NjNkLWExYzk1MzEyNmMwNCJ9

Observação: acesso e visibilidade dependem das configurações de compartilhamento do relatório no Power BI.

## Imagens do dashboard

Imagens selecionadas (apenas duas):

![Resumo](assets/screenshots/pg01.jpg)
![Visão 2](assets/screenshots/pg02.jpg)

## Como abrir o projeto (PBIP)

1. Instale o Power BI Desktop (2023+ recomendado).
2. Clone este repositório.
3. No Power BI Desktop, abra o arquivo PBIP em `dashboards/Performance-Comercial/Performance Comercial.pbip`.

## Estrutura do repositório

- `dashboards/Performance-Comercial/`
  - `Performance Comercial.pbip`: projeto Power BI do dashboard.
  - `Performance Comercial.Report/`: artefatos do relatório (inclui `report.json`).
  - `Performance Comercial.SemanticModel/`: modelo semântico (`definition/`, `definition.pbism`, `diagramLayout.json`).
  - `METADATA.json`: metadados (páginas, fontes, etc.).
- `assets/screenshots/pg01.jpg` e `assets/screenshots/pg02.jpg`: imagens padrão.
- `README.md`: guia principal de uso e manutenção.
- `LICENSE`: licença do projeto (MIT).

## Boas práticas de versionamento (PBIP)

- Ignorar arquivos locais/cache do Power BI (`**/.pbi/localSettings.json`, `**/.pbi/cache.abf`).
- Utilizar mensagens de commit claras (feat, fix, docs, etc.).
- Em mudanças maiores, utilizar branches e Pull Requests.

## Atualizações e manutenção

1. Faça alterações no Power BI Desktop e salve o PBIP.
2. No Git:
   - `git add -A`
   - `git commit -m "descrição da mudança"`
   - `git push`

## Conexões e dados

Este repositório não inclui credenciais sensíveis. Ajuste `Data Source Settings`
ao abrir o PBIP e valide caminhos/permissões conforme seu ambiente.

## Licença

Este projeto está licenciado sob MIT. Veja o arquivo [LICENSE](LICENSE) para detalhes.
