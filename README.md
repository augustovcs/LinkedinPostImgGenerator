# 30 Posts de LinkedIn + Imagens (Dev Fullstack)

Pacote pronto para publicar uma série de 30 posts de LinkedIn voltados a construir
autoridade e personal brand para um dev fullstack (.NET/C#, React, Next.js, Astro, IA),
atraindo recruiters e a comunidade tech.

Os posts seguem as boas práticas de alcance do LinkedIn 2026: **sem engagement bait**
(nada de "Concorda?", "Comenta aí", pods), hooks curtos, voz autêntica, opiniões
contrarian com lastro, sem links externos no corpo e 3-5 hashtags.

## Arquivos

| Arquivo | O que é |
|---|---|
| `posts.md` | Os 30 textos prontos pra copiar/colar + o prompt de imagem (inglês) de cada um. |
| `gerar_imagens.py` | Script que gera as 30 imagens via OpenAI (gpt-image-1) e salva em `imagens/`. |
| `imagens/` | Saída: `post_01.png` ... `post_30.png` (criada ao rodar o script). |

## Fluxo de uso

### 1. Configurar a chave da OpenAI (nunca colocada no código)
O script lê a variável de ambiente `OPENAI_API_KEY`.

- **PowerShell (sessão atual):** `$env:OPENAI_API_KEY = "sk-..."`
- **PowerShell (permanente):** `setx OPENAI_API_KEY "sk-..."` (reabra o terminal depois)
- **bash/zsh:** `export OPENAI_API_KEY="sk-..."`

### 2. Instalar a dependência e gerar as imagens
```bash
pip install --upgrade openai
python gerar_imagens.py
```
O script loga o progresso ("Gerando 7/30..."), trata erros com retry, faz pausa entre
chamadas pra respeitar rate limit e **pula imagens já geradas** — então é seguro rodar de
novo pra retentar só o que faltou.

> Custo: a geração de imagem da OpenAI é paga (cobra por imagem). 30 imagens = 30 cobranças.

### 3. Revisar as imagens
Abra `imagens/` e confira cada PNG. Geração de imagem erra spelling, então os prompts
pedem no máximo 1-3 palavras curtas — descarte/regenere qualquer uma com texto estranho
(basta apagar o `post_NN.png` e rodar o script de novo).

### 4. Postar manualmente no LinkedIn
Para cada post: copie o texto correspondente de `posts.md`, anexe a imagem `post_NN.png`
e publique. Sugestões:
- Publique 3-5 por semana, espaçados, em horários de pico (manhã/início de tarde em dias úteis).
- Se algum dia quiser incluir um link, ponha **no primeiro comentário**, não no corpo.
- Acompanhe quais formatos performam melhor (contrarian, história, técnico) e ajuste a mistura.

## Distribuição dos 30 posts
6 contrarian · 5 história pessoal · 5 educacional (erros não-óbvios) · 4 build in public ·
4 hot take de carreira · 3 técnico direto · 3 reflexão curta. Temática visual variada e sem
repetição em sequência (meme técnico, stickman, anime, minimalista, isométrico 3D,
ilustração detalhada, código estilizado, tipografia, cartoon, non-sense).
