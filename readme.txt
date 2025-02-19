-- selecionar a versão do python
> pyenv local 3.12.7
-- criar o ambiente virtual
> python -m venv .venv
-- entrar no ambiente virtual e exportar as variáveis de ambiente
> source .venv/bin/activate && export $(grep -v '^#' .env | xargs)
-- atualizar o pip
> pip install --upgrade pip
-- instalar requirements-dev
> pip install -r requirements-dev.txt
-- gerar o requirements.txt a partir do requirements.in
> pip-compile requirements.in
-- editar o arquivo MANIFEST.in
-- editar setup.py com o nome do projeto e demais informações
-- editar app.py dentro da pasta do projeto
> pip install -e .

-- DOCKER
-- executar o build do docker
> docker build -f Dockerfile.dev -t jamar:latest .
docker build -f Dockerfile.dev -t $DOCKER_IMAGE_NAME:latest . --build-arg APP_NAME=$PROJETO --build-arg AWS_ID=$ECOBE_AWS_ACCESS_KEY_ID  --secret id=AWS_KEY,env=$AWS_KEY

	- testando:
		> docker run -d --rm -it -v $(pwd):/home/app/api -p 8000:8000 --name api jamar
		- executando a o bash
		> docker exec -it api bash
- executar o docker-compose
	> docker-compose up --force-recreate --remove-orphans
- executar o bash em outro terminal e criar as tabelas com CLI
	OBS: se atentar para o MYSQL_URI em settings.toml
	> docker exec -it api bash
	> jamar --help
	> jamar db
	> jamar db-init
> pre-commit install