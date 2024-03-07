# Pyproxy

## O que é um proxy?

Um Proxy é um intermediário entre o cliente e o servidor, ele pode visualizar, salvar ou filtrar qualquer conteúdo que você estiver acessando.
Normalmente é usado nas redes de empresas, elas usam essa filtragem de conteúdo para proteger os sistemas da empresa de malwares.

## Propsta

Nesse projeto eu crio um proxy que salva toda troca de informações, mas para simplifica-lo eu limitei ele a apenas uma porta do navegador, criando assim o proxy mais simples possível.

## Estrutura

```
PyProxy
├── main.py
└── data
     └── data_exchange.json
```

## Lógica

Em ```main.py``` defino a porta e dentro dela defino que tudo vai passar por uma conexão socket vigiada pelo proxy, que armazena todos os dados coletados no ```data_exchange.json```.
