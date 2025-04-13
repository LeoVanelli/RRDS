
# Registro Rural Data Scraper v1.2.1

Este guia descreve os passos para configurar e executar o projeto corretamente.

## Requisitos

- **Python 3.8+**: Certifique-se de que você tem o Python 3.8 ou superior instalado no seu sistema.

## Passos para Configuração e Execução

### 1. Verificar a versão do Python

Primeiramente, verifique se você tem o Python 3.8 ou superior instalado no seu sistema. Execute o seguinte comando no terminal ou prompt de comando:

```bash
python --version
```

Se a versão exibida for 3.8 ou superior, você pode continuar. Caso contrário, instale a versão mais recente do [Python](https://www.python.org/downloads/).

### 2. Verificar a presença do arquivo `registros_incra.csv`

O próximo passo é garantir que o arquivo `registros_incra.csv` esteja presente no diretório correto.

- O arquivo **deve ser nomeado exatamente como** `registros_incra.csv`.
- Verifique se ele contém uma coluna chamada **`cod_imovel`** e se há registros dentro dele.

### 3. Colocar o arquivo em `batch/queue`

Após verificar a existência e estrutura do arquivo `registros_incra.csv`, coloque-o no diretório:

```
batch/queue
```

Se o diretório `batch/queue` não existir, crie-o manualmente.

### 4. Rodar o arquivo `setup_and_run.bat`

Agora, basta executar o arquivo `setup_and_run.bat` para iniciar o processo.

- **No Windows**, clique duas vezes no arquivo `setup_and_run.bat` para rodar o processo.
- O script irá automaticamente instalar as dependências e iniciar a execução do sistema.

Após seguir esses passos, o sistema estará pronto para processar os registros.

---

**Observações:**

- Certifique-se de que todos os pré-requisitos estão corretamente instalados.
- Se houver qualquer erro ou problema durante o processo, consulte os logs de erro gerados para mais detalhes.
- Caso o arquivo CSV não esteja estruturado corretamente, o processo pode falhar ou não gerar os resultados esperados.

---

Se tiver dúvidas ou precisar de mais informações, estarei a disposição.
