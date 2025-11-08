# Performance Comercial

Projeto PBIP público no padrão do repositório "Investimentos". Este repositório contém o relatório e o modelo semântico versionados, além de metadados e imagens de referência.

Visualização pública (Power BI):
https://app.powerbi.com/view?r=eyJrIjoiNzk3NDYyMTQtZjgwYi00YmQwLWJlY2UtNGY4MTYxY2E1OTY5IiwidCI6IjA5ZjRiZmNhLTY3Y2QtNGU0Zi05NjNkLWExYzk1MzEyNmMwNCJ9

Como abrir no Power BI Desktop (PBIP):
1. Abra o Power BI Desktop atualizado.
2. Vá em Arquivo > Abrir relatório (.pbip).
3. Selecione: `dashboards/Performance-Comercial/Performance Comercial.pbip`.

Estrutura do repositório:
- `dashboards/Performance-Comercial/`
  - `Performance Comercial.pbip`
  - `Performance Comercial.Report/`
    - `report.json`
  - `Performance Comercial.SemanticModel/`
    - `definition/` (model, tables, relationships)
    - `definition.pbism`
    - `diagramLayout.json`
  - `images/` (imagens extraídas do PDF para documentação)
  - `METADATA.json` (descrição e caminhos do projeto)
- `scripts/`
  - `extract_images.py` (reexecuta extração de imagens do PDF para `dashboards/Performance-Comercial/images`)

Regerar imagens do PDF (sem capa):
```bash
python scripts/extract_images.py
```

Observações:
- Arquivos locais do PBIP como `**/.pbi/localSettings.json` e `**/.pbi/cache.abf` estão ignorados via `.gitignore`.
- Não há página estática ou GitHub Pages; o foco é o projeto PBIP e a visualização pública via Power BI.
