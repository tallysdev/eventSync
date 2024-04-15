# eventsync_front

<h1 align='center'> Eventy sync front-end</h1>

## Setup de IDE recomendado

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar).

## Type Support for `.vue` Imports in TS

O TypeScript não pode lidar com informações de tipo para importações `.vue` por padrão, então substituímos o CLI `tsc` pelo `vue-tsc` para verificação de tipo. Nos editores, precisamos do[Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) para fazer o serviço de linguagem TypeScript reconhecer os tipos `.vue`.

## Instalação de dependências

```sh
npm install
```

### Compilação e Hot-Reload para desenvolvimento

```sh
npm run dev
```

### Checagem de tipos, compilação e minificação para produção

```sh
npm run build
```

### Executar testes unitários com [Vitest](https://vitest.dev/)

```sh
npm run test:unit
```

### Lint com [ESLint](https://eslint.org/)

```sh
npm run lint
```