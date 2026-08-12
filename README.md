# multi-agent-project

Manifests e estrutura para executar agentes locais.

Estrutura:
- agents/: contain individual agent folders (agent_01..)
- tools/, workflows/, prompts/, knowledge/, config/, tests/, docs/

Veja ./agents para os manifests originais.

Instruções básicas:
1. Instale Python 3.10+
2. Crie um ambiente virtual: python -m venv .venv
3. Ative e instale dependências: .\.venv\Scripts\activate ; pip install -r requirements.txt
4. Edite e execute runner: python runner.py
