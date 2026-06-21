# 30 Posts de LinkedIn — Dev Fullstack (.NET/C#, React, Next.js, Astro, IA)

> Regras aplicadas (LinkedIn 2026): sem engagement bait, hook curto, voz real,
> contrarian com lastro, sem links no corpo, 3-5 hashtags. Copie/cole direto.
> Cada post traz, logo abaixo, o **Prompt de imagem (GPT Image)** em inglês.
> Todas as artes são em estilo **anime/Ghibli**, com sub-estilos variados
> (OVA 80s, cel 90s, Akira/Otomo, Shinkai, Ghibli, seinen, shoujo, gag, key visual 2020s…).

---

### POST 01 — Contrarian — Cobertura de testes é vaidade

90% de cobertura e mesmo assim quebrou em produção.

Porque cobertura não mede o que você testou. Mede o que você executou.

Dá pra ter 90% rodando getter, setter e construtor — e zero teste no único fluxo que move dinheiro. O número fica verde, o gestor fica feliz, e o bug entra pela porta que ninguém olhou.

Coverage é um mapa de onde você passou, não de onde você prestou atenção.

O que eu olho hoje:
- Os caminhos de erro estão testados, ou só o caminho feliz?
- Existe um teste que falharia se a regra de negócio mudasse errado?
- Se eu deletar essa validação, algum teste fica vermelho?

Um teste que nunca pode falhar não é um teste. É decoração.

Persiga o risco, não a porcentagem.

#testing #softwareengineering #dotnet #qualidadedesoftware #devbr

**Prompt de imagem (GPT Image):**
Anime illustration in the style of late-1990s hand-painted cel animation — grainy OVA frame with visible film grain, slightly desaturated colors and imperfect inked lines. The scene: a young programmer leans back smugly in a worn swivel chair in a dim office at night, arms crossed, smiling at a chunky CRT monitor glowing with a single huge green checkmark. Behind him, completely unnoticed, the rest of the room is quietly catching fire — small orange flames climbing the server towers, papers scattering in the heat, a cat fleeing the edge of the frame.

Limited cel-shading with hard-edged shadows, warm amber firelight clashing against the cold green screen-glow, dust and embers drifting through the light. The composition is split diagonally: smug calm on the left, creeping catastrophe on the right. The mood is ironic, bittersweet, the kind of single nostalgic still that feels pulled from a forgotten anime tape. Square composition, no readable text except maybe a faint glowing check symbol, richly detailed analog background, deliberately human and hand-made — nothing digitally sterile.

---

### POST 02 — Contrarian — Microserviços foram um erro pra 90%

Você não tinha um problema de escala. Tinha um problema de organização.

E resolveu com microsserviços.

Aí trocou uma função que chamava outra função por uma rede inteira entre elas. Agora o bug não está "na linha 40" — está em algum lugar entre seis serviços, três filas e um timeout que ninguém configurou direito.

A maioria dos times que adotou microsserviços não tinha escala do Netflix. Tinha um monolito bagunçado e a esperança de que cortar em pedaços ia organizar a bagunça.

Não organizou. Só distribuiu.

Microsserviço resolve problema organizacional de empresa grande: times independentes fazendo deploy sem pisar no pé um do outro. Se você é um time de cinco pessoas, você não tem esse problema — você tem um monolito modular esperando pra nascer.

Comece junto. Separe quando doer de verdade.

#microservices #arquitetura #softwarearchitecture #dotnet #backend

**Prompt de imagem (GPT Image):**
Hand-painted Studio Ghibli-inspired watercolor scene, lush and warm, rolling green hills under a soft cumulus sky. In the foreground, a small round-faced character in patched overalls cheerfully balances a single neat wooden crate on their back, walking a clear dirt path. The same character is mirrored on the right side of the frame, now buried under a teetering absurd tower of six crates lashed together with countless ropes that crisscross the entire sky like a tangled spiderweb, sweat flying off their face, eyes wide with panic.

Gentle gouache textures with visible brushstrokes, the cozy nostalgic palette of greens, sky-blues and earthy browns of a classic 90s Ghibli still. Soft diffused daylight, tiny lovingly-painted background details — a windmill, grazing sheep, a crooked wooden fence. The mood is whimsical but quietly stressful, a little fable about something simple turning into chaos. Square composition, no text anywhere, deeply human and analog, nothing flat or AI-generic.

---

### POST 03 — Contrarian — Pare de decorar LeetCode

Inverter uma árvore binária no quadro nunca salvou um projeto.

Mas é nisso que a entrevista insiste.

A gente decora 200 problemas de LeetCode pra provar que sabe programar, e no dia a dia o trabalho é entender um requisito mal escrito, ler código que outra pessoa deixou e não quebrar nada no caminho.

Não estou dizendo que algoritmo não importa. Estou dizendo que medir um dev pela velocidade de resolver quebra-cabeça sob pressão é como contratar um chef pela rapidez com que ele descasca batata de olhos vendados.

O que prevê um bom dev na prática:
- Como ele lê um código que não escreveu.
- Como ele reage quando não sabe a resposta.
- Como ele decide o que NÃO construir.

Nada disso cabe num cronômetro de 45 minutos.

A barra está errada. E a gente decorou ela mesmo assim.

#leetcode #carreiradev #entrevista #techinterview #programacao

**Prompt de imagem (GPT Image):**
Surreal 1980s Akira-era cyberpunk anime aesthetic — dense, precise Otomo-style line work, neon-soaked night palette of magenta, electric cyan and deep velvet black. A salaryman in a sharp suit sits at a desk floating in an endless dark void, blindfolded, calmly peeling a giant glowing potato with a tiny knife, while a literal tree — gnarled bark, real leaves, forking branches drawn like an impossible diagram — erupts out of an open laptop beside him.

Heavy cel shading, chromatic reflections shimmering on wet-looking surfaces, motion smear on the falling potato peels, a hazy bokeh of distant city lights bleeding through the dark. The mood is deadpan, dreamlike and faintly dystopian — the visual nonsense of measuring entirely the wrong thing. Vintage film-cel glow and grain over everything. Square composition, no readable text, ultra-detailed retro-futurist atmosphere, intentional and analog.

---

### POST 04 — Contrarian — Framework JS novo não é o problema

Não é fadiga de JavaScript. É fadiga de fundamento.

Toda semana sai um framework novo e todo mundo reclama do cansaço de aprender mais um. Mas observa: quem domina closure, event loop, HTTP e modelo de componente aprende qualquer framework novo num fim de semana.

O cansaço não vem da ferramenta nova. Vem de pular de ferramenta em ferramenta nunca tendo aprendido o que está por baixo de todas elas.

React, Vue, Svelte, Solid, Astro — mudam a sintaxe, não a física. Reatividade, estado, renderização e fronteira cliente/servidor são os mesmos conceitos vestindo roupas diferentes.

Quando você reclama que "tem coisa nova demais", o que costuma estar quebrado é a base, não o ecossistema.

Aprenda o que não muda. O resto vira detalhe.

#javascript #react #frontend #webdev #astro

**Prompt de imagem (GPT Image):**
Makoto Shinkai-inspired key visual: hyper-luminous sky, god-rays piercing dramatic layered clouds, lens flares and that signature painterly realism with impossibly detailed backgrounds. A determined young developer in a hoodie stands rooted on a rooftop at golden hour while a swirling tempest of translucent UI panels, brackets and abstract framework sigils tears past like autumn leaves caught in a typhoon, their hair and jacket snapping violently in the wind.

Around the figure radiates a calm warm glow, a bubble of stillness in the chaos, suggesting unshakable fundamentals. Saturated teal-to-amber gradient sky, crisp rim lighting outlining the silhouette, deep atmospheric perspective with distant city skyline and shimmering floating particles. Cinematic, emotional, heroic-yet-serene mood. Square composition, no readable text, breathtakingly detailed and atmospheric, nothing flat or generic.

---

### POST 05 — Contrarian — No-code não vai te substituir

"Programar sem programar" sempre termina programando dentro da ferramenta. Pior.

No-code é incrível pra validar uma ideia rápido. O problema é o que vendem junto: a fantasia de que a complexidade some.

Ela não some. Ela se esconde.

Chega a hora da regra de negócio de verdade — aquele "if" maluco que o cliente pediu, a integração que precisa de retry, o relatório que junta cinco fontes — e você está montando lógica condicional arrastando caixinhas numa tela que não foi feita pra isso. Sem versionamento decente. Sem teste. Sem poder pedir ajuda pro Stack Overflow.

A complexidade essencial do problema não desaparece porque a ferramenta escondeu o código. Alguém ainda precisa entender o fluxo, prever o erro e decidir o trade-off.

No-code muda quem programa e como. Não apaga a necessidade de pensar como engenheiro.

#nocode #lowcode #softwareengineering #automacao #devbr

**Prompt de imagem (GPT Image):**
Vintage 1970s-80s manga aesthetic rendered as a single dramatic panel: heavy halftone screentone dots, bold inked outlines, dense cross-hatching for shadow, a slightly yellowed old-paper texture as if scanned from a worn tankobon. An ocean cross-section: above the waterline, a cheerful simplified control panel of friendly floating blocks bobs in gentle inked waves under a clean sky.

Below the surface — drawn with obsessive ink detail and layered screentone gradients — lurks an enormous tangled iceberg of cables, gears, warning signs and branching condition-logic descending into black water, tiny fish-like error icons darting around it. Strong diagonal composition, theatrical contrast between the innocent surface and the monstrous depth. Monochrome with a single muted-blue spot accent. Square composition, only a tiny short label like "no-code", retro print mood, intricate and unmistakably analog.

---

### POST 06 — Contrarian — Você não precisa de Kubernetes

Kubernetes é resolver um problema de escala que você ainda não tem.

A maioria dos projetos roda perfeitamente — e mais barato — num servidor simples ou num PaaS. Mas a gente sobe um cluster, configura ingress, helm, três YAMLs por serviço e um operador pra cuidar do operador, tudo pra servir 200 usuários por dia.

A conta vem em dois lugares: na fatura da nuvem e nas horas que você gasta operando infraestrutura em vez de construir produto.

K8s faz sentido quando você tem muitos serviços, muitos times e necessidade real de orquestração elástica. Se você consegue listar seus servidores nos dedos de uma mão, você não está nesse cenário — está fazendo cosplay de Big Tech.

Escolha a coisa mais chata que resolve o problema de hoje. Complexidade você adiciona quando a dor chegar. Não antes.

#kubernetes #devops #cloud #arquitetura #infra

**Prompt de imagem (GPT Image):**
Minimalist modern 2020s anime key-visual style — clean confident line work, flat-but-rich color blocking, the restrained elegance of a contemporary streaming-series poster. A lone small figure stands at the very bottom of the frame on an empty pale plain, gazing up at a single absurdly gigantic, ornate orbiting machine of interlocking rings and gears (a helm-wheel motif) hovering uselessly in a vast soft sky, utterly dwarfing them.

Lots of deliberate negative space, a tight limited palette of deep navy, dusty rose and off-white, a subtle gradient sky, one long quiet shadow stretching across the ground. The mood is dry, ironic and a touch melancholic — overwhelming machinery for a tiny need. Refined, editorial, intentional composition like a poster a designer agonized over for weeks. Square composition, at most one or two short words, nothing busy, nothing AI-generic.

---

### POST 07 — História — O bug que me custou um fim de semana

Passei um fim de semana inteiro caçando um bug. A causa era uma linha boba.

Sexta à noite, tudo funcionando local. Em produção, intermitente: às vezes o dado vinha certo, às vezes vinha pela metade. Sem padrão. Sem log claro. O tipo de bug que faz você duvidar da própria sanidade.

Sábado eu culpei o banco. Domingo eu culpei a fila. Reescrevi um pedaço inteiro achando que era concorrência.

No fim, era uma comparação de data sem fuso horário. Em produção o servidor estava em UTC, na minha máquina não. A "metade" dos dados era só a metade que caía do outro lado da meia-noite.

O que aprendi não foi sobre data. Foi sobre mim: passei dois dias consertando o que eu imaginava em vez de medir o que estava acontecendo. Quando finalmente parei de adivinhar e adicionei um log no ponto certo, o bug apareceu em dez minutos.

Hoje minha primeira pergunta em qualquer bug é: o que eu ainda estou supondo sem ter medido?

#debugging #devlife #dotnet #softwareengineering #carreiradev

**Prompt de imagem (GPT Image):**
Makoto Shinkai-style nocturnal interior: a cramped bedroom-office bathed in the cold blue glow of a single monitor, every surface lovingly detailed — scattered energy-drink cans, tangled cables, a hoodie thrown over the chair, rain streaking the window with city bokeh glowing beyond. An exhausted young developer is slumped forward over the keyboard, half-asleep, deep dark circles under their eyes.

Perched mischievously on a floating wall-clock — whose face absurdly shows two contradictory time zones at once — is a tiny translucent glowing "bug" creature, watching them with a sly little grin. Warm desk-lamp amber fights the cold screen-blue, dust motes drift through the light, soft reflections shimmer on the wet glass. Intimate, lonely, bittersweet 3am mood. Hyper-detailed background, cinematic depth of field, painterly realism. Square composition, no readable text, nothing sterile.

---

### POST 08 — História — Como entrei na programação

Não foi paixão à primeira vista. Foi teimosia.

Eu não cresci sonhando em ser programador. Caí na primeira tela preta cheia de erro e quase desisti — parecia que o computador estava decidido a me dizer "isso não é pra você".

A virada foi pequena. Eu queria automatizar uma coisa chata e repetitiva, daquelas que a gente faz no braço todo dia. Escrevi algo feio, cheio de gambiarra, que provavelmente daria vergonha hoje. Mas funcionou. E ver a máquina fazer sozinha o que eu fazia na mão mexeu com algo.

Não foi o código bonito que me fisgou. Foi a sensação de transformar uma ideia em algo que existe e funciona.

Quem está começando agora e se sente burro na frente do erro: esse sentimento não é sinal de que você não serve. É o pedágio de entrada. Todo mundo que você admira já chorou na frente de uma stack trace.

Continua. A teimosia vira habilidade.

#programacao #carreiradev #comecandonaprogramacao #devbr #autodidata

**Prompt de imagem (GPT Image):**
Studio Ghibli-inspired cozy nostalgia, soft watercolor and gouache, warm golden afternoon light pouring through a dusty window. A small child sits cross-legged on a wooden floor in front of a chunky old beige computer with a blinking green terminal cursor, face lit with wide-eyed wonder, while a single tiny green sprout improbably grows out of the keyboard, reaching toward the light.

The room is full of warm hand-painted detail — a fat tube TV, scattered cassette tapes, a sleeping cat curled on a cushion, curtains gently billowing in a breeze. Muted earthy palette with that signature Ghibli green and honey-gold glow, painterly textures and soft edges everywhere. The mood is tender, hopeful, the quiet beginning of a lifelong love. Square composition, no readable text, deeply nostalgic and human, nothing clean or digital.

---

### POST 09 — História — Aceitei um projeto acima do meu nível

Falei "sim" pra um projeto que eu não sabia fazer.

E foi a melhor decisão de carreira que tomei até hoje.

Na hora bateu pânico. Eu não dominava metade do que o escopo pedia. Meu instinto foi recusar pra não passar vergonha. Aceitei mesmo assim — meio por coragem, meio por inconsequência.

As primeiras semanas foram desconfortáveis de um jeito que eu não sabia que existia. Aprendi de noite o que precisava aplicar de manhã. Errei na frente de gente que sabia mais. Pedi ajuda mais vezes do que meu ego queria.

Mas eu entreguei. E saí do outro lado sendo um dev que o "eu de antes" não reconheceria.

A verdade que ninguém fala: você quase nunca se sente pronto antes de aceitar o desafio. A prontidão é consequência de aceitar, não pré-requisito.

Se você só pega o que já sabe fazer, você só fica bom no que já era.

#carreiradev #crescimento #devlife #softwareengineering #mindset

**Prompt de imagem (GPT Image):**
Surreal, dreamlike anime in the unsettling-yet-beautiful spirit of Satoshi Kon: impossible architecture, perspective that bends, vivid saturated color. A tiny resolute figure stands at the foot of a colossal ladder that twists up into towering cumulus clouds — but the ladder itself is built from floating keyboards, coffee mugs and precariously stacked books, and far, far below the ground is a single gigantic open laptop glowing like a canyon floor.

A vertiginous worm's-eye composition emphasizes scale and vertigo, soft volumetric clouds drifting past, a teal-and-cream palette pierced by one warm orange shaft of light pouring from above. Painterly and slightly hallucinatory, equal parts terrifying and inviting — the exact feeling of saying yes to something far too big. Richly detailed, cinematic, atmospheric. Square composition, no readable text, intentional and analog.

---

### POST 10 — História — Aprendi a dizer "não sei"

A frase que mais me deu respeito profissional foi "eu não sei".

Por anos eu achei que admitir desconhecimento era assinar minha incompetência. Então eu enrolava. Dava respostas vagas, "depende", torcia pra ninguém perguntar de novo.

Numa reunião eu finalmente travei e falei: "não sei, mas até amanhã eu descubro." Esperei o constrangimento. Veio o contrário. A pessoa mais sênior da sala assentiu como quem reconhece alguém confiável.

Demorei pra entender: ninguém confia em quem tem resposta pra tudo. A gente confia em quem sabe a fronteira do próprio conhecimento — porque essa é a pessoa que não vai te empurrar um chute disfarçado de certeza.

"Não sei" não fecha a conversa. Abre. Vira "não sei ainda, e aqui está como vou descobrir".

Senioridade não é nunca errar. É ser honesto sobre o que você não viu ainda.

#carreiradev #lideranca #softskills #devlife #maturidade

**Prompt de imagem (GPT Image):**
Tender 1990s shoujo anime aesthetic — delicate line work, sparkling highlights, a pastel palette of lilac, peach and soft blue, the dreamy gentleness of a classic magical-girl still. A young person stands in a quiet sunlit room, hand to their chest, expression soft and brave, as a single large translucent speech bubble floats beside them — and inside that bubble, drawn like a tiny illustration, is a small wooden door standing ajar with warm light spilling out.

Floral bokeh and drifting flower petals in the background, gentle gradient lighting, the characteristic shoujo shimmer of star-sparkles glittering in the air. The mood is vulnerable, honest and quietly courageous — admitting "I don't know" as an opening, not a defeat. Soft cel shading, romantic and warm, lovingly detailed. Square composition, no readable text, nothing clinical or cold.

---

### POST 11 — História — Migrei de stack e quase me perdi

Troquei minha stack principal e por um tempo me senti júnior de novo.

Eu era produtivo, confortável, rápido no que dominava. Aí decidi ir fundo em outra stack — e de repente cada tarefa simples levava o triplo do tempo. Coisas que eu fazia no automático viraram pesquisa no Google a cada cinco minutos.

A parte difícil não foi a sintaxe nova. Foi a sensação de regressão. Eu sabia o quanto era capaz na stack antiga, e me ver lento na nova mexeu com a identidade, não só com a habilidade.

O que me segurou foi lembrar que o desconforto era o aprendizado acontecendo, não a prova de que eu não dava conta. Conceito não se perde na migração — ele se transfere. O que eu sabia de arquitetura, de banco, de debugar, veio junto. Só o vocabulário mudou.

Três meses depois eu não só estava produtivo na stack nova como entendia a antiga mais fundo, por contraste.

Trocar de stack não te rebaixa. Te dá uma segunda perspectiva sobre o que você já sabia.

#carreiradev #aprendizado #dotnet #react #devlife

**Prompt de imagem (GPT Image):**
Epic 2010s fantasy-anime key visual, the sweeping cinematic look of a high-budget movie poster — dramatic scale, volumetric fog, rich saturated color. A lone traveler with a softly glowing backpack crosses a long swaying rope bridge suspended over a vast misty canyon, connecting two floating islands: the one behind washed in cool twilight blues, the one ahead glowing in warm amber dawn — two different worlds bridged by a single fragile path.

Deep atmospheric perspective with layered clouds, drifting light particles, distant birds wheeling in the gulf below, the traveler's cloak caught mid-wind. The backpack emits a quiet golden aura, suggesting carried knowledge crossing safely from one world to the next. Awe, transition, hope tinged with risk. Painterly detailed backgrounds, cinematic lighting, grand and emotional. Square composition, no readable text, nothing generic.

---

### POST 12 — Educacional — Erros não-óbvios em async/await

`await` dentro de um loop é o erro que mais sangra performance silenciosamente.

Ninguém te avisa porque o código funciona. Só fica lento.

Os tropeços de async que passam batido:

1. await em loop sequencial
Você espera cada item terminar antes de começar o próximo. Se as chamadas são independentes, junte tudo com Promise.all / Task.WhenAll e espere uma vez. Dez chamadas de 1s deixam de levar 10s pra levar 1s.

2. Esquecer o await
A função retorna a Promise, o código segue em frente, e o erro estoura num lugar que não tem nada a ver. Sem await, o try/catch não pega nada.

3. Engolir exceção em fire-and-forget
Disparou sem await e sem tratamento? Se aquilo falhar, falha em silêncio. O usuário nunca sabe, e você também não.

4. Bloquear o thread esperando async (.Result / .Wait())
Em .NET isso é convite a deadlock. Async de cima a baixo, sem misturar com bloqueante.

Async não é "deixa rápido". É "não fica parado esperando". Usar errado faz o oposto das duas coisas.

#async #javascript #dotnet #performance #programacao

**Prompt de imagem (GPT Image):**
Early-2000s digital anime aesthetic with a cyber, Serial-Experiments-Lain flavor — glowing wireframes, faint scanlines, a moody green-on-black data-space, soft CRT bloom and pixel grain. A figure seen from behind floats in a dark void facing two enormous translucent vertical "code stream" panels: the left one bleeding angry red light that drips downward slowly, one drop at a time (sequential, choked); the right one pulsing calm green with many streams flowing in parallel harmony.

Glowing particles and holographic ripples fill the air, and a reflective black floor mirrors the panels like still water. Cool cyber palette of emerald, crimson and inky black, layered with atmospheric haze. Contemplative, slightly retro-futurist, the quiet beauty of concurrency made visible. Highly detailed, immersive, analog-meets-digital texture. Square composition, no readable real text except perhaps one faint glowing keyword. Nothing flat or generic.

---

### POST 13 — Educacional — Erros de portfólio que afastam recruiter

Seu portfólio tem dez to-do apps. O recruiter fechou na terceira.

Não é falta de projeto. É falta de sinal.

O que faz um portfólio ser ignorado:

1. Dez projetos iguais de tutorial
To-do, clone de Netflix, calculadora. Mostram que você seguiu instruções, não que você resolve problema. Um projeto que resolve uma dor real vale mais que dez clones.

2. README vazio
"Como rodar: npm install." E o que isso faz? Que problema resolve? Que decisão você tomou? README é onde você mostra que pensa, não só que digita.

3. Sem deploy
"Tá no GitHub" é metade. Recruiter não vai clonar e subir seu projeto. Um link que abre e funciona vale dez repositórios que ninguém roda.

4. Histórico de um commit só
"first commit" com o projeto inteiro dentro grita que você não trabalha de forma incremental — exatamente o oposto do que um time precisa.

Menos projetos. Mais profundidade. Um app que resolve um problema de verdade conta mais história que uma página cheia de clones.

#portfolio #carreiradev #recrutamento #devbr #primeiroemprego

**Prompt de imagem (GPT Image):**
Comedic gag-manga anime style with chibi exaggeration — bouncy rounded characters, big expressive eyes, sweat-drops and emphasis lines, the playful energy of a 4-koma strip. A deadpan, bored chibi recruiter slouches in an office chair lazily thumb-scrolling a glowing phone, and floating out of the screen is a conveyor-belt row of nearly identical tiny "to-do app" boxes, all dull and grey, the recruiter's eyes half-lidded with boredom.

At the very end of the row, one single box glows golden and bursts with little sparkle-stars, and the recruiter's eyes suddenly snap wide and shiny with cartoon interest, a tiny "ping!" spark popping above their head. Bright flat cel colors, bold clean outlines, an off-white studio background with comic speed-lines. Light, funny, self-aware mood. Square composition, only a tiny short label at most, lively and hand-drawn, nothing static.

---

### POST 14 — Educacional — Erros de segurança que junior comete

A senha estava no código. O código estava no GitHub. O GitHub era público.

Erros de segurança que parecem bobos até virarem incidente:

1. Segredo no repositório
Chave de API, string de conexão, token — commitados "só pra testar". O Git lembra pra sempre, mesmo depois que você apaga. Use variável de ambiente e secret manager desde o primeiro dia.

2. SQL montado com concatenação
"SELECT * FROM user WHERE name = '" + input + "'". É o convite literal pra SQL injection. Sempre parametrize. Sempre.

3. Confiar no front pra validar
Esconder o botão não protege o endpoint. Quem quer atacar não usa sua tela — manda request direto. Validação e autorização moram no servidor.

4. Logar dado sensível
Senha, token e CPF caindo em texto puro no log. O atacante não precisa invadir o banco se o log já entrega tudo.

5. Mensagem de erro que conta demais
Stack trace completa na tela mostra versão, caminho e estrutura interna pra qualquer um. Erro genérico pro usuário, detalhe só no log interno.

Segurança não é um módulo que você adiciona no fim. É um hábito que você carrega em cada linha.

#seguranca #cybersecurity #backend #devsecops #programacao

**Prompt de imagem (GPT Image):**
Dark, moody seinen anime aesthetic — heavy shadows, a muted desaturated palette, the tense atmosphere of a cyber-thriller OVA. A dim server room at night rendered in detailed perspective, towering racks blinking with tiny lights, a single large glowing padlock hovering protectively above a stylized database core that pulses softly blue. But on one side, a heavy door has been left carelessly ajar, hostile warm-red light leaking through the gap, and a small forgotten key glints on the floor right in front of it.

A shadowy silhouette looms just beyond the doorway, unseen by anyone inside. Volumetric haze drifts through the racks, cold blue safety light clashing with the intruding red, a reflective metal floor doubling every glow, fine mechanical detail everywhere. Suspenseful, ominous, cautionary mood. Cinematic seinen lighting, intricate and gritty. Square composition, no readable text, nothing clean or generic.

---

### POST 15 — Educacional — Erros não-óbvios em C#/.NET

`async void` é uma armadilha que compila lindamente e te trai em silêncio.

Erros de C#/.NET que passam no review e voltam pra te assombrar:

1. async void
Exceção dentro dele não pode ser capturada por quem chamou — ela derruba o processo. Use async Task sempre, exceto em event handler de verdade.

2. Não dispor o que é IDisposable
Conexão, stream, HttpClient mal gerenciado. Esqueceu o using? Vazou recurso. Em servidor isso vira degradação lenta que ninguém liga ao culpado certo.

3. Capturar Exception genérica e engolir
catch (Exception) { } esconde o problema real e transforma um bug óbvio numa caça ao tesouro de três dias.

4. DbContext vivendo demais
DbContext é de vida curta. Mantê-lo aberto por muito tempo, ou compartilhar entre threads, gera bug de estado e memória que parece "fantasma".

5. string + string em loop
Concatenar string num laço cria um objeto novo a cada volta. Em volume, é StringBuilder. Parece detalhe até o profiler te mostrar onde o tempo foi.

A maioria desses não dá erro na hora. Dá erro depois, longe, difícil de rastrear. Conhecer a armadilha é metade de não cair nela.

#csharp #dotnet #backend #cleancode #programacao

**Prompt de imagem (GPT Image):**
Bright, cute 2010s moe anime style — soft rounded shapes, pastel cheerfulness, sparkly highlights, the disarming charm that hides a trap. A wide-eyed cartoon developer-girl reaches eagerly toward a giant glossy gift box wrapped with an enormous ribbon, sparkles dancing all around it, completely unaware that a friendly-looking pastel snake (a "bug") with a sly little smile is coiled and peeking out from behind the box, tongue flicking.

Vivid candy palette of lavender, mint and bubblegum pink, clean confident cel shading, a soft gradient studio background dotted with floating sparkle-bokeh. The contrast of innocent cuteness and lurking danger is the entire joke. Expressive, charming, gently menacing mood. Square composition, at most a tiny short label like "async void", polished but warm and hand-illustrated, nothing sterile.

---

### POST 16 — Educacional — Erros ao aprender a programar

O tutorial te dá a ilusão de progresso. Por isso ele vicia.

Erros de quem está aprendendo a programar — e quase ninguém percebe que está cometendo:

1. Tutorial hell
Você assiste, acompanha, tudo funciona, sente que aprendeu. Aí abre o editor sozinho e congela. Acompanhar não é saber. Saber é construir do zero, errando.

2. Pular o fundamento pra chegar no framework
Quer fazer site bonito antes de entender como a web funciona. O framework vira mágica que você não controla, e cada erro vira parede.

3. Não ler a mensagem de erro
A resposta geralmente está ali, na linha que você fechou com raiva. O erro não é seu inimigo. É a única coisa te dizendo onde olhar.

4. Nunca ler código dos outros
Você só escreve, nunca lê. Mas 90% do trabalho real é entender código que outra pessoa fez. Leia projeto open source.

5. Estudar passivo, sem construir nada seu
Curso, vídeo, anotação — e nenhum projeto que seja problema seu. O que fixa não é o conteúdo. É a luta de aplicar.

Aprender a programar não é coletar tutoriais. É acumular horas de tela em branco que você teve que preencher sozinho.

#aprenderprogramar #programacao #carreiradev #autodidata #devbr

**Prompt de imagem (GPT Image):**
High-energy 2010s shounen anime key visual — dynamic perspective, glowing effects, intense determined emotion. A young learner is caught inside a swirling tunnel-vortex made of countless floating "play button" screens spiraling around them like a hypnotic whirlpool, dragging them in endless circles — but they strain forward, reaching with an outstretched hand toward a single distant blank editor window at the tunnel's end, from which real warm light pours out.

Saturated purple-to-electric-blue gradient, sharp motion lines and speed blur, glowing particles streaking past, a powerful rim light catching the protagonist's determined face. Dramatic, almost desperate yet hopeful — escaping passive consumption toward real creation. Cinematic, richly detailed, emotionally charged. Square composition, no readable text, vivid and kinetic, nothing flat.

---

### POST 17 — Técnico/Ensinamento — Debounce vs throttle

Debounce e throttle resolvem o mesmo problema. De jeitos opostos.

Os dois existem porque um evento dispara rápido demais: digitar numa busca, redimensionar a tela, rolar a página, clicar feito louco. Sem controle, você dispara cem chamadas por segundo pra fazer um trabalho que precisava acontecer uma vez.

A diferença é quando o trabalho roda.

Debounce espera o silêncio. Ele segura a execução até o evento parar de acontecer por um tempinho. Perfeito pra busca enquanto digita: só dispara quando o usuário para de teclar. Cem teclas viram uma chamada — a última.

Throttle marca o ritmo. Ele deixa rodar no máximo uma vez a cada intervalo, não importa quantos eventos cheguem no meio. Perfeito pra scroll ou redimensionar: você quer atualizar de tempos em tempos, não a cada pixel.

Regra de bolso: se você só liga pro resultado final, debounce. Se você precisa de atualizações regulares durante a ação, throttle.

Parece detalhe de front. Mas é a diferença entre uma interface fluida e uma que trava o navegador sozinha.

#frontend #javascript #react #webperformance #programacao

**Prompt de imagem (GPT Image):**
Sleek modern 2020s sports-anime aesthetic, the crisp dynamic style of a contemporary running/athletics series — fluid motion, confident clean lines, vivid but tasteful color grading. Two runners on a stylized track seen in dramatic side profile: one sprints in erratic frantic bursts, multiple ghost-afterimages stacked chaotically behind them (debounce — only the final position counts); the other moves in steady, evenly-spaced strides, regular afterimages at fixed intervals like a metronome (throttle).

Strong horizontal motion composition with speed lines and wind streaks, a sunset-orange and cool-blue split palette dividing the two rhythms, glowing dust kicked up from the track. Energetic, precise, instructional-yet-cool mood — a key visual that makes a technical idea feel epic. Highly detailed motion effects, cinematic lighting. Square composition, no readable text, stylish and intentional.

---

### POST 18 — Opinião — Nomear bem é metade da engenharia

O código mais difícil de ler não é o complexo. É o mal nomeado.

`data`, `temp`, `valor2`, `handleThing`, `manager`, `process()`. Cada um desses nomes empurra o entendimento pra frente: você precisa abrir a função, ler o corpo inteiro e adivinhar o que ela realmente faz.

Um bom nome economiza essa viagem. Ele diz o que a coisa é antes de você precisar investigar.

Nomear bem é difícil porque te obriga a entender de verdade o que aquilo faz. Quando você não consegue achar o nome, geralmente é porque a função faz coisa demais, ou você ainda não entendeu o problema. Nome ruim costuma ser sintoma, não a doença.

Algumas regras que carrego:
- Nome revela intenção, não implementação. `dueDate`, não `date2`.
- Booleano soa como pergunta de sim/não: `isActive`, `hasPermission`.
- Função é verbo. Coisa é substantivo.
- Se você precisa de um comentário pra explicar a variável, o nome dela já era pra ser esse comentário.

O computador não liga pro nome. Ele roda `x` igualzinho a `valorTotalComDesconto`. Os nomes não são pra máquina. São pra próxima pessoa que abrir o arquivo — e essa pessoa quase sempre é você, daqui a seis meses, sem lembrar de nada.

#cleancode #softwareengineering #boaspraticas #programacao #devbr

**Prompt de imagem (GPT Image):**
Quiet, contemplative Studio Ghibli-inspired interior — warm hand-painted watercolor, dust motes floating in shafts of late-afternoon light through tall windows. A cozy, cluttered library-study where a thoughtful character sits at a worn wooden desk, brush-pen in hand, carefully writing a single elegant label on a small wooden name-tag, surrounded by countless little drawers and jars each quietly waiting to be named — the whole room an archive of carefully chosen names.

Soft earthy palette of honeyed browns, deep greens and parchment cream, gouache textures, lovingly detailed clutter: stacked leather books, a steaming teacup, a curious cat watching from a shelf. The mood is calm, craftsmanlike and reverent — the quiet weight of naming things well. Painterly, nostalgic, deeply human. Square composition, no readable text, nothing sterile or digital.

---

### POST 19 — Técnico/Ensinamento — Como ler uma stack trace

A stack trace não é o erro gritando com você. É o mapa até ele.

Muita gente vê aquela parede vermelha de texto e fecha por reflexo. Mas a stack trace é, literalmente, a coisa mais útil que o sistema te entrega num bug. Ela está te dando o caminho.

Como eu leio:

1. A primeira linha é o quê. O tipo do erro e a mensagem. NullReference, IndexOutOfRange, timeout. Já te diz a categoria do problema.

2. De cima pra baixo é o caminho de volta. O topo é onde estourou; descendo, é a sequência de chamadas que levou até ali. A linha mais valiosa costuma ser a primeira que aponta pro SEU código, não pra biblioteca.

3. Ignore o ruído do framework. Dezenas de linhas internas raramente são a causa. Procure o seu arquivo, sua linha.

4. Leia a mensagem de verdade. "Object reference not set" não é genérico — é o sistema dizendo que algo que você esperava existir estava nulo. A pergunta vira: o que eu achei que estava preenchido e não estava?

Aprender a ler stack trace é o que separa "não sei por que quebrou" de "achei em dois minutos". A resposta quase sempre já estava na tela. Só faltava parar pra ler.

#debugging #programacao #carreiradev #softwareengineering #devbr

**Prompt de imagem (GPT Image):**
Moody detective-noir anime aesthetic, late-80s/90s mystery OVA vibe — dramatic chiaroscuro shadows, smoky atmosphere, a single hard light source, a muted sepia-and-teal palette. A sharp-eyed developer-detective in a long coat stands beneath a flickering lamp, intently reading an impossibly long paper scroll (a "stack trace") that unfurls from their hands all the way to the floor and curls across the room, a magnifying glass in one hand catching a single highlighted line glowing faintly red.

A rain-streaked window glows behind them, venetian-blind shadows striping the whole scene, faint smoke-haze curling through the light, scattered case-file papers pinned to a corkboard with red string. Tense, analytical, cinematic mood — the trace as a trail of clues, not an accusation. Richly inked detail, film-noir grain. Square composition, no readable text, atmospheric and intentional.

---

### POST 20 — Carreira — O melhor dev não é o que digita mais rápido

O melhor dev do time raramente é o que digita mais rápido.

A imagem de programador que vendem é alguém martelando o teclado a 200 palavras por minuto, terminal piscando, código brotando. Na prática, os melhores que eu vi passam um tempo desconfortável só... parados. Pensando.

Porque a parte cara não é escrever o código. É decidir qual código escrever.

Escrever rápido a solução errada só te faz chegar mais cedo no retrabalho. O dev que para dez minutos pra entender o problema de verdade — quem usa, o que pode dar errado, o que NÃO precisa ser construído — entrega menos linhas e resolve mais.

O que eu aprendi a valorizar:
- Quem faz a pergunta que evita uma semana de trabalho inútil.
- Quem deleta código em vez de só adicionar.
- Quem escreve a solução chata e óbvia em vez da esperta e frágil.
- Quem admite que não entendeu o requisito antes de codar em cima da dúvida.

Velocidade de digitação é a métrica mais fácil de ver e a menos importante de todas. O trabalho de verdade acontece antes de a primeira tecla ser pressionada.

Se você é júnior e se sente lento: talvez você só esteja, finalmente, pensando.

#carreiradev #softwareengineering #senioridade #devlife #programacao

**Prompt de imagem (GPT Image):**
Warm 2010s slice-of-life anime aesthetic, the gentle workplace-drama look — soft natural lighting, a relatable detailed office setting, expressive but understated characters. In an open-plan studio, one developer hammers furiously at a keyboard in a blur of motion lines and flying sparks, surrounded by chaos and crumpled paper; nearby, another developer sits calmly leaning back, eyes closed in thought, a single quiet lightbulb glow hovering above them, a half-finished cup of tea steaming, radiating unhurried clarity.

A cozy muted palette of warm woods, soft greens and afternoon light pouring through big windows, with plants, sticky-notes and mugs detailing the lived-in space. A subtle, sympathetic contrast between frantic speed and calm thinking — neither mocked. Tender, observational, quietly wise mood. Detailed background, painterly cel shading. Square composition, no readable text, human and lived-in.

---

### POST 21 — Hot take — IA não rouba sua vaga; outro dev usando IA, sim

A IA não vai pegar sua vaga. Outro dev usando IA melhor que você, talvez.

O medo está apontado pro lugar errado.

O modelo não te entende, não conhece seu domínio, não decide trade-off e não responde pelo resultado. Ele acelera quem sabe pra onde está indo. Sozinho, ele é um estagiário brilhante e amnésico.

O que muda o jogo não é "a IA existir". É a diferença de produtividade entre dois devs do mesmo nível — um que aprendeu a usar IA como alavanca e um que finge que ela não existe.

Esse segundo não vai ser substituído pela máquina. Vai ser ultrapassado pelo colega.

Então a pergunta não é "será que a IA me substitui". É "estou virando o dev que usa essas ferramentas pra entregar mais, ou estou esperando elas passarem como moda?".

Não terceirize seu pensamento pra ela. Mas não finja que dá pra competir ignorando ela.

#ia #carreiradev #futurodotrabalho #produtividade #tech

**Prompt de imagem (GPT Image):**
Makoto Shinkai-style dusk scene — a radiant gradient sky of violet, rose and burning orange, hyper-detailed layered clouds, glowing atmosphere and soft lens flares. Two silhouetted runners race along an elevated train track at twilight: one runs alone, straining; just ahead, the other runs with a small luminous arrow-shaped aura of light trailing from their feet, propelled slightly faster — both rendered as crisp backlit figures against the blazing sky.

Vast cinematic depth, distant city lights just beginning to twinkle below, shimmering particles and warm bloom, long dramatic shadows stretching across the rails. The mood is bittersweet and urgent — not man-versus-machine but human-versus-human-with-leverage. Breathtaking painterly background, emotional and luminous. Square composition, no readable text, awe-inspiring and intentional.

---

### POST 22 — Hot take — Pare de aplicar pra 200 vagas; construa em público

200 candidaturas, 3 respostas. O problema talvez não seja seu currículo.

É a estratégia.

Spray de currículo é um jogo de loteria com expectativa baixa: você compete de igual pra igual com centenas de pessoas num funil onde ninguém te conhece, e torce pra um filtro automático não te descartar antes de um humano ler.

Tem um caminho mais lento e muito mais forte: construir em público. Compartilhar o que você aprende, mostrar projeto resolvendo problema real, deixar rastro do seu raciocínio onde recruiter e dev passam.

A diferença é a direção. Candidatura é você correndo atrás. Presença é você sendo encontrado — já com prova de trabalho na mesa antes da primeira conversa.

Não estou dizendo pra parar de aplicar. Estou dizendo pra parar de apostar tudo no método de menor conversão e nenhuma ficha no que faz as oportunidades virem até você.

Currículo abre uma porta. Reputação faz baterem na sua.

#carreiradev #buildinpublic #recrutamento #personalbranding #devbr

**Prompt de imagem (GPT Image):**
Energetic comedic gag-manga style — exaggerated expressions, bold ink, speed-lines, the chaotic fun of a Shonen Jump gag panel. On the left, a frazzled character with crazy spinning eyes hurls a towering stack of paper résumés into a swirling dark void, papers scattering everywhere, none of them landing, sweat flying off their face. On the right, the same character — now serene with a tiny halo — calmly stacks glowing blocks into a small radiant tower while little chibi figures wander toward it on their own, drawn in.

Punchy flat colors with a single green accent on the tower, an off-white background with comic emphasis lines and a few sparkle-stars, a dynamic split composition. Funny, self-deprecating, clever mood. Clean bold cel outlines, lively and hand-drawn. Square composition, at most a tiny short label, nothing static or generic.

---

### POST 23 — Hot take — 90% das "startups de IA" são wrapper

A maioria das "startups de IA" é um prompt bem-vestido em cima da API de outra empresa.

E isso é um problema de fosso, não de tecnologia.

Se o seu produto é uma caixa de texto que repassa o pedido pro modelo de um terceiro, qualquer pessoa com a mesma API replica em um fim de semana. Não tem barreira. O modelo que te dá superpoder dá o mesmo superpoder pro seu concorrente — e pro fornecedor do modelo, que pode lançar sua feature como botão nativo amanhã.

O valor de verdade quase nunca está no modelo. Está no que só você tem:
- Os dados proprietários que ninguém mais consegue acessar.
- O problema específico que você entende fundo e os outros não.
- O fluxo, a integração e a confiança que cercam a IA.

"Usar IA" não é estratégia. É commodity. A pergunta que separa produto de wrapper é: o que sobra de defensável se amanhã o modelo virar grátis pra todo mundo?

Se a resposta é "nada", você não tem uma startup de IA. Tem uma demo.

#ia #startup #produto #tech #empreendedorismo

**Prompt de imagem (GPT Image):**
Detailed 80s Akira/Otomo-inspired cyberpunk anime — dense line work, a neon-noir palette of hot magenta, acid green and deep black, wet reflective surfaces, glowing signage haze. A flashy gift box wrapped in shimmering holographic "AI" foil sits center-frame, but a hand is peeling back the wrapping to reveal it is hollow inside — empty except for a single thin glowing tube snaking out the back, tethering it to a colossal distant corporate server-tower looming in the smoggy cityscape, owned by someone else.

A dramatic low-angle composition, volumetric neon light shafts cutting through the haze, chromatic glow, drifting rain particles, that gritty retro-future film grain. Ironic, revealing, faintly cynical mood — the illusion of substance exposed. Ultra-detailed, cinematic, with analog cel texture. Square composition, no readable text, richly atmospheric.

---

### POST 24 — Hot take — Certificação não impressiona quem contrata bem

Pilha de certificado não impressiona quem realmente sabe contratar.

Um projeto que resolve um problema de verdade, sim.

Certificado prova que você passou numa prova. Não prova que você aguenta um requisito ambíguo, lê código alheio sem surtar, ou toma uma decisão de arquitetura sabendo que vai ter que viver com ela.

Quem contrata bem aprendeu a ler entre as linhas: a fila de badges no perfil muitas vezes diz "eu sei estudar pra prova", não "eu sei entregar valor". E entregar valor é a única coisa que a empresa compra.

Não é que certificação seja inútil. Ela ajuda a organizar estudo e, em alguns nichos, é filtro de entrada. O erro é tratar ela como o destino em vez do mapa — colecionar selo achando que isso substitui ter construído algo que funciona e que outra pessoa usa.

Entre dois candidatos, o que mostra um sistema rodando e sabe explicar cada escolha ganha do que mostra dez certificados quase toda vez.

Construa coisas. O certificado é consequência do aprendizado, não prova dele.

#carreiradev #certificacao #recrutamento #devbr #portfolio

**Prompt de imagem (GPT Image):**
Triumphant shounen anime key visual — bold heroic lighting, a dynamic low angle, a glowing power-aura, the proud climax-of-the-arc energy. A confident young developer holds aloft a single glowing "working app" like a radiant trophy, light bursting from it, eyes shining with earned pride. Behind them, slightly out of focus and unstable, a ridiculous teetering tower of identical certificate-medals wobbles and begins to topple, completely ignored.

A saturated gold-and-blue palette, dramatic god-rays and sparkle particles, a wind-swept jacket flaring like a cape, speed lines radiating outward from the trophy. Crisp modern cel shading with cinematic bloom. Empowering, a little cheeky, victorious mood — substance over collection. Detailed, kinetic, emotionally charged. Square composition, no readable text, vivid and intentional.

---

### POST 25 — Técnico — Race condition que só dava em produção

O bug não aparecia na minha máquina. Só em produção. E nunca na mesma hora.

Esse é o pior tipo: o intermitente que some quando você vai olhar.

Local, eu tinha um usuário: eu. Em produção, dezenas de requisições chegavam ao mesmo tempo. Duas delas liam o mesmo registro, decidiam a mesma coisa em paralelo, e gravavam por cima uma da outra. Às vezes batia, às vezes não — pura sorte de timing.

Eu perdi tempo procurando o bug "no código" como se fosse uma linha errada. Não era. Era a ausência de uma garantia: nada impedia dois fluxos de fazerem a mesma operação ao mesmo tempo.

A correção não foi reescrever a lógica. Foi tornar a operação segura sob concorrência — controle de acesso ao recurso e a checagem certa na hora de gravar, pra que a segunda escrita soubesse que a primeira já aconteceu.

A lição que ficou: "funciona na minha máquina" muitas vezes só significa "minha máquina não tem concorrência". Produção tem. Pense em quem mais pode estar tocando o mesmo dado no mesmo instante.

Bug de concorrência não se acha lendo. Se acha pensando em quantas coisas acontecem ao mesmo tempo.

#concorrencia #backend #dotnet #debugging #softwareengineering

**Prompt de imagem (GPT Image):**
Tense psychological-thriller anime aesthetic, the razor-sharp stillness of a Death-Note-style standoff — extreme close framing, a dramatic spotlight, deep black negative space, a sliver of cold blue and one stab of warning red. Two identical glowing arrows reach in from opposite edges of the frame toward a single small data-block at the exact center at the very same instant, frozen a heartbeat before collision, a tiny crackling spark igniting where they are about to clash.

High-contrast lighting, faint motion blur on the converging arrows, an oppressive sense of timing and inevitability hanging in the air. Muted near-monochrome with that single red collision accent, cinematic and claustrophobic. Suspenseful, precise, ominous mood — the silent danger of concurrency made visible. Ultra-detailed, theatrical. Square composition, no readable text, nothing flat.

---

### POST 26 — Técnico — Idempotência salvou minha integração

O cliente foi cobrado duas vezes. O código estava "certo". O problema era a falta de uma palavra: idempotência.

A integração recebia um webhook de pagamento e processava. Funcionava — até o dia em que o provedor reenviou o mesmo evento (porque a primeira resposta demorou e ele achou que falhou). Meu sistema processou de novo, obediente. Cobrança dobrada.

A verdade desconfortável: em sistemas distribuídos, a mesma mensagem chegar mais de uma vez não é exceção. É garantia. Rede falha, timeout acontece, retry existe. Quem assume "vai chegar exatamente uma vez" está construindo em cima de uma mentira.

A solução foi tornar a operação idempotente: cada evento carrega um identificador único, eu registro o que já processei, e se o mesmo id voltar, eu reconheço e ignoro em vez de repetir. Processar duas vezes passa a ter o mesmo efeito que processar uma.

Não mudei o que o código faz. Mudei o que ele faz quando o mundo repete.

Se sua integração assume que cada mensagem chega uma vez só, ela não está pronta pra produção. Está pronta pro dia bom.

#idempotencia #integracao #backend #sistemasdistribuidos #dotnet

**Prompt de imagem (GPT Image):**
Whimsical surreal dream-anime, the gently impossible logic of a Satoshi Kon dream sequence — a soft pastel palette, floaty lighting, reality bending kindly. A delivery courier hands the exact same glowing parcel to a calm recipient three times in an endless looping motion-trail, the duplicate parcels fading into translucent ghosts as the recipient serenely accepts only the first and lets the copies dissolve into drifting light-petals.

Muted teal, warm coral and cream tones, dreamy bokeh, repeating echo-afterimages curving softly through the air, a quiet surreal stillness despite all the repetition. Painterly soft edges, floating particles, a faintly humorous serenity. Clever, calm, slightly magical mood — sameness made safe. Detailed and atmospheric. Square composition, no readable text, nothing sterile.

---

### POST 27 — Técnico — Timezone/UTC: o bug que todo mundo paga

Todo dev paga o pedágio do fuso horário pelo menos uma vez. Eu paguei caro.

O relatório fechava o dia "errado". Pedidos da noite caíam no dia seguinte. Tudo porque em algum ponto uma data foi salva no fuso do servidor em vez de em UTC — e o servidor e o usuário viviam em fusos diferentes.

A regra que aprendi na marra e nunca mais larguei:

1. Guarde sempre em UTC. O banco não deveria saber em que fuso o usuário está. Ele guarda o instante absoluto.

2. Converta só na borda. Transforme pro fuso local apenas na hora de mostrar pro humano. Entrada e armazenamento ficam em UTC, do começo ao fim.

3. Data não é string. Tratar data como texto "dd/MM" é semear bug de comparação e ordenação. Use o tipo de data/hora certo, com fuso explícito.

4. Cuidado com "agora". DateTime.Now pega o fuso da máquina. Em servidor, quase sempre você quer o equivalente em UTC.

Fuso horário parece detalhe até o relatório financeiro fechar com o número errado e alguém perguntar por quê.

Salve em UTC. Converta na ponta. Durma tranquilo.

#timezone #utc #dotnet #backend #bugs

**Prompt de imagem (GPT Image):**
Loud comedic gag-anime style — exaggerated panic, popping expressions, chaotic energy, the over-the-top humor of a sitcom anime. A split vertical composition: in the calm top half, a relaxed chibi developer gives a confident thumbs-up, little sparkles of false security around them; in the frenzied bottom half, the very same developer is mid-scream, hair standing on end, comically flailing while a whirlwind of dozens of clocks — each showing a different time — and wildly flipping calendar pages tornadoes around their head.

Bright punchy flat colors, bold black outlines, motion lines, sweat-drops and a few cartoon stars-of-pain, an off-white studio background with emphasis bursts. Hilarious, relatable, kinetic mood — the universal timezone meltdown. Clean expressive cel art with a hand-drawn feel. Square composition, at most a tiny short label like "UTC", nothing flat or generic.

---

### POST 28 — Reflexão — Você não é seu código

Crítica ao seu código não é crítica a você. Aprender isso me deixou um dev melhor.

No começo eu defendia cada linha como se fosse minha honra. Code review virava tribunal. Cada sugestão parecia um ataque pessoal, e eu gastava energia provando que estava certo em vez de melhorar o que estava na mesa.

O dia que separei as duas coisas, tudo ficou mais leve. O código é uma tentativa de resolver um problema num momento com a informação que eu tinha. Ele pode estar errado sem que eu seja burro. Pode ser melhorado sem que eu seja diminuído.

Quem revisa apontando uma falha não está dizendo que você não presta. Está te dando, de graça, um par de olhos que enxerga o que os seus não enxergaram.

Desapegar do ego no review não é fraqueza. É o que destrava o aprendizado mais rápido que existe.

Seu valor não está na linha que você escreveu. Está na velocidade com que você melhora ela.

#carreiradev #codereview #softskills #mindset #devlife

**Prompt de imagem (GPT Image):**
Serene, contemplative Studio Ghibli-inspired scene — a soft watercolor sky at dawn, a gentle pastel gradient, a single quiet figure in a wide tranquil landscape. A person sits peacefully on a grassy hill at sunrise, knees hugged to their chest, gazing calmly at a separate softly-glowing translucent block of abstract "code" floating gently a little distance away from them — clearly close, but distinctly apart, a small respectful gap of air between self and creation.

A tender palette of misty lavender, pale gold and dewy green, drifting seed-fluff and morning haze, painterly brush textures, a few birds far off in the sky. The mood is calm, healing and gently profound — separating worth from work, ego from output. Lovingly detailed natural background, warm and human. Square composition, no readable text, nothing cold or clinical.

---

### POST 29 — Reflexão — Simplicidade é a feature mais difícil

Fazer simples dá mais trabalho que fazer complicado. Por isso quase ninguém faz.

Qualquer um adiciona. Mais uma flag, mais uma camada, mais uma abstração "pro caso de". Complexidade é o caminho de menor resistência — você só vai empilhando.

Simplicidade é o oposto. Exige entender o problema fundo o bastante pra saber o que pode sair. Exige a coragem de deletar código que funciona. Exige resistir à tentação de resolver o problema que talvez nunca venha.

O código complicado é o rascunho. O código simples é a versão editada — e editar custa mais que escrever.

Por isso solução simples raramente é sinal de problema fácil. Quase sempre é sinal de alguém que trabalhou dobrado pra esconder a dificuldade de você.

Da próxima vez que algo parecer simples demais, lembre: alguém suou pra que parecesse óbvio.

#simplicidade #cleancode #softwareengineering #arquitetura #devlife

**Prompt de imagem (GPT Image):**
Detailed seinen craftsman-anime aesthetic, the focused intensity of a master-artisan series — warm workshop lighting, fine textural detail, reverent realism. A split scene: on the left, a figure effortlessly and carelessly piles up a tall teetering tower of random mismatched blocks, chaos stacking itself for free; on the right, the same figure sweats and strains with chisel and mallet, painstakingly carving a single flawless smooth cube out of a rough heavy block of stone, marble dust drifting through the lamplight.

A warm amber workshop glow set against cool shadow, gritty tactile textures everywhere — wood grain, raw stone, sweat, tool marks — with a single calm blue accent on the finished cube. The composition contrasts effortless mess with hard-won simplicity. Respectful, intense, quietly heroic mood. Richly detailed, painterly cel art. Square composition, no readable text, deeply analog.

---

### POST 30 — Reflexão — Constância vence talento

Talento te dá vantagem na largada. Constância ganha a corrida.

Eu já vi gente brilhante travar e gente "comum" decolar. A diferença quase nunca foi o teto de cada um. Foi quem apareceu de novo no dia em que não estava com vontade.

Talento é um surto. Resolve o problema bonito de hoje e descansa. Constância é um regime. Resolve o problema feio de hoje, e o de amanhã, e o de depois — e é nessa soma silenciosa que a habilidade de verdade se constrói.

Programar tem muito disso. O salto raramente vem de um insight genial. Vem de mil pequenos problemas enfrentados em sequência, cada um te deixando um pouco menos perdido que o anterior.

Você não precisa ser o mais inteligente da sala. Precisa ser o que ainda está lá quando os mais inteligentes já cansaram.

Apareça amanhã. E no dia seguinte. É menos glamouroso e mais poderoso do que parece.

#constancia #carreiradev #disciplina #mindset #devbr

**Prompt de imagem (GPT Image):**
Sweeping Makoto Shinkai-style epic vista — a luminous endless sky of layered clouds glowing gold and rose at the horizon, hyper-detailed and breathtaking. A vast staircase built from countless identical small blocks ascends from the foreground up toward a radiant distant goal-light high in the sky. A tiny steady silhouetted figure climbs one patient step at a time, while lower down, faded translucent figures who sprinted ahead sit slumped and exhausted on the steps, left behind by persistence.

Cinematic scale and deep atmospheric perspective, drifting light particles, soft volumetric god-rays, long gentle shadows running down the stairs, that signature Shinkai bloom and saturation over everything. The mood is quietly triumphant, motivational without being loud — consistency outlasting raw talent. Painterly, emotional, grand. Square composition, no readable text, awe-inspiring and intentional.
