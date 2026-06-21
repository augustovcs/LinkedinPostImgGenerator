# -*- coding: utf-8 -*-
"""
gerar_imagens.py
================
Gera as 30 imagens dos posts de LinkedIn usando o modelo de geração de imagem
mais atual da OpenAI (gpt-image-1), a partir dos prompts em inglês definidos em PROMPTS.

Todas as artes são em estilo ANIME/GHIBLI, com sub-estilos variados (OVA 80s, cel 90s,
Akira/Otomo, Makoto Shinkai, Studio Ghibli, seinen, shoujo, gag-manga, key visual 2020s...).

------------------------------------------------------------------------------
COMO INSTALAR
------------------------------------------------------------------------------
    pip install --upgrade openai

------------------------------------------------------------------------------
COMO CONFIGURAR A CHAVE (NUNCA hardcode a chave no código!)
------------------------------------------------------------------------------
A chave é lida da variável de ambiente OPENAI_API_KEY.

  Windows (PowerShell) - sessao atual:
      $env:OPENAI_API_KEY = "sk-..."

  Windows (PowerShell) - permanente:
      setx OPENAI_API_KEY "sk-..."
      (feche e reabra o terminal depois do setx)

  Linux / macOS (bash/zsh):
      export OPENAI_API_KEY="sk-..."

------------------------------------------------------------------------------
COMO RODAR
------------------------------------------------------------------------------
    python gerar_imagens.py

As imagens sao salvas em ./imagens/post_01.png ... post_30.png
Se um post ja tiver imagem gerada, ele é pulado (permite retomar de onde parou).
IMPORTANTE: se voce mudou os prompts e quer regerar, apague antes os PNGs antigos
em ./imagens/ (ou apenas os post_NN.png que deseja refazer).
"""

import base64
import os
import sys
import time

# Os 30 prompts de imagem (estilo anime/ghibli, variados), na MESMA ordem dos posts.
PROMPTS = [
    # 01 - Cobertura de testes e vaidade - 90s cel OVA, cena de incendio ironico
    """Anime illustration in the style of late-1990s hand-painted cel animation - grainy OVA frame with visible film grain, slightly desaturated colors and imperfect inked lines. The scene: a young programmer leans back smugly in a worn swivel chair in a dim office at night, arms crossed, smiling at a chunky CRT monitor glowing with a single huge green checkmark. Behind him, completely unnoticed, the rest of the room is quietly catching fire - small orange flames climbing the server towers, papers scattering in the heat, a cat fleeing the edge of the frame.

Limited cel-shading with hard-edged shadows, warm amber firelight clashing against the cold green screen-glow, dust and embers drifting through the light. The composition is split diagonally: smug calm on the left, creeping catastrophe on the right. The mood is ironic, bittersweet, the kind of single nostalgic still that feels pulled from a forgotten anime tape. Square composition, no readable text except maybe a faint glowing check symbol, richly detailed analog background, deliberately human and hand-made - nothing digitally sterile.""",

    # 02 - Microservicos erro 90% - Ghibli watercolor, simples vs caotico
    """Hand-painted Studio Ghibli-inspired watercolor scene, lush and warm, rolling green hills under a soft cumulus sky. In the foreground, a small round-faced character in patched overalls cheerfully balances a single neat wooden crate on their back, walking a clear dirt path. The same character is mirrored on the right side of the frame, now buried under a teetering absurd tower of six crates lashed together with countless ropes that crisscross the entire sky like a tangled spiderweb, sweat flying off their face, eyes wide with panic.

Gentle gouache textures with visible brushstrokes, the cozy nostalgic palette of greens, sky-blues and earthy browns of a classic 90s Ghibli still. Soft diffused daylight, tiny lovingly-painted background details - a windmill, grazing sheep, a crooked wooden fence. The mood is whimsical but quietly stressful, a little fable about something simple turning into chaos. Square composition, no text anywhere, deeply human and analog, nothing flat or AI-generic.""",

    # 03 - LeetCode decoreba - Akira/Otomo 80s cyberpunk, absurdo
    """Surreal 1980s Akira-era cyberpunk anime aesthetic - dense, precise Otomo-style line work, neon-soaked night palette of magenta, electric cyan and deep velvet black. A salaryman in a sharp suit sits at a desk floating in an endless dark void, blindfolded, calmly peeling a giant glowing potato with a tiny knife, while a literal tree - gnarled bark, real leaves, forking branches drawn like an impossible diagram - erupts out of an open laptop beside him.

Heavy cel shading, chromatic reflections shimmering on wet-looking surfaces, motion smear on the falling potato peels, a hazy bokeh of distant city lights bleeding through the dark. The mood is deadpan, dreamlike and faintly dystopian - the visual nonsense of measuring entirely the wrong thing. Vintage film-cel glow and grain over everything. Square composition, no readable text, ultra-detailed retro-futurist atmosphere, intentional and analog.""",

    # 04 - Framework JS nao e o problema - Makoto Shinkai luminoso
    """Makoto Shinkai-inspired key visual: hyper-luminous sky, god-rays piercing dramatic layered clouds, lens flares and that signature painterly realism with impossibly detailed backgrounds. A determined young developer in a hoodie stands rooted on a rooftop at golden hour while a swirling tempest of translucent UI panels, brackets and abstract framework sigils tears past like autumn leaves caught in a typhoon, their hair and jacket snapping violently in the wind.

Around the figure radiates a calm warm glow, a bubble of stillness in the chaos, suggesting unshakable fundamentals. Saturated teal-to-amber gradient sky, crisp rim lighting outlining the silhouette, deep atmospheric perspective with distant city skyline and shimmering floating particles. Cinematic, emotional, heroic-yet-serene mood. Square composition, no readable text, breathtakingly detailed and atmospheric, nothing flat or generic.""",

    # 05 - No-code nao substitui - manga retro 70s/80s screentone, iceberg
    """Vintage 1970s-80s manga aesthetic rendered as a single dramatic panel: heavy halftone screentone dots, bold inked outlines, dense cross-hatching for shadow, a slightly yellowed old-paper texture as if scanned from a worn tankobon. An ocean cross-section: above the waterline, a cheerful simplified control panel of friendly floating blocks bobs in gentle inked waves under a clean sky.

Below the surface - drawn with obsessive ink detail and layered screentone gradients - lurks an enormous tangled iceberg of cables, gears, warning signs and branching condition-logic descending into black water, tiny fish-like error icons darting around it. Strong diagonal composition, theatrical contrast between the innocent surface and the monstrous depth. Monochrome with a single muted-blue spot accent. Square composition, only a tiny short label like "no-code", retro print mood, intricate and unmistakably analog.""",

    # 06 - Nao precisa de Kubernetes - key visual minimalista 2020s
    """Minimalist modern 2020s anime key-visual style - clean confident line work, flat-but-rich color blocking, the restrained elegance of a contemporary streaming-series poster. A lone small figure stands at the very bottom of the frame on an empty pale plain, gazing up at a single absurdly gigantic, ornate orbiting machine of interlocking rings and gears (a helm-wheel motif) hovering uselessly in a vast soft sky, utterly dwarfing them.

Lots of deliberate negative space, a tight limited palette of deep navy, dusty rose and off-white, a subtle gradient sky, one long quiet shadow stretching across the ground. The mood is dry, ironic and a touch melancholic - overwhelming machinery for a tiny need. Refined, editorial, intentional composition like a poster a designer agonized over for weeks. Square composition, at most one or two short words, nothing busy, nothing AI-generic.""",

    # 07 - Bug fim de semana - Shinkai, quarto noturno melancolico
    """Makoto Shinkai-style nocturnal interior: a cramped bedroom-office bathed in the cold blue glow of a single monitor, every surface lovingly detailed - scattered energy-drink cans, tangled cables, a hoodie thrown over the chair, rain streaking the window with city bokeh glowing beyond. An exhausted young developer is slumped forward over the keyboard, half-asleep, deep dark circles under their eyes.

Perched mischievously on a floating wall-clock - whose face absurdly shows two contradictory time zones at once - is a tiny translucent glowing "bug" creature, watching them with a sly little grin. Warm desk-lamp amber fights the cold screen-blue, dust motes drift through the light, soft reflections shimmer on the wet glass. Intimate, lonely, bittersweet 3am mood. Hyper-detailed background, cinematic depth of field, painterly realism. Square composition, no readable text, nothing sterile.""",

    # 08 - Como entrei na programacao - Ghibli aconchegante nostalgico
    """Studio Ghibli-inspired cozy nostalgia, soft watercolor and gouache, warm golden afternoon light pouring through a dusty window. A small child sits cross-legged on a wooden floor in front of a chunky old beige computer with a blinking green terminal cursor, face lit with wide-eyed wonder, while a single tiny green sprout improbably grows out of the keyboard, reaching toward the light.

The room is full of warm hand-painted detail - a fat tube TV, scattered cassette tapes, a sleeping cat curled on a cushion, curtains gently billowing in a breeze. Muted earthy palette with that signature Ghibli green and honey-gold glow, painterly textures and soft edges everywhere. The mood is tender, hopeful, the quiet beginning of a lifelong love. Square composition, no readable text, deeply nostalgic and human, nothing clean or digital.""",

    # 09 - Projeto acima do nivel - Satoshi Kon surreal, escada nas nuvens
    """Surreal, dreamlike anime in the unsettling-yet-beautiful spirit of Satoshi Kon: impossible architecture, perspective that bends, vivid saturated color. A tiny resolute figure stands at the foot of a colossal ladder that twists up into towering cumulus clouds - but the ladder itself is built from floating keyboards, coffee mugs and precariously stacked books, and far, far below the ground is a single gigantic open laptop glowing like a canyon floor.

A vertiginous worm's-eye composition emphasizes scale and vertigo, soft volumetric clouds drifting past, a teal-and-cream palette pierced by one warm orange shaft of light pouring from above. Painterly and slightly hallucinatory, equal parts terrifying and inviting - the exact feeling of saying yes to something far too big. Richly detailed, cinematic, atmospheric. Square composition, no readable text, intentional and analog.""",

    # 10 - Dizer "nao sei" - shoujo 90s suave, balao com porta
    """Tender 1990s shoujo anime aesthetic - delicate line work, sparkling highlights, a pastel palette of lilac, peach and soft blue, the dreamy gentleness of a classic magical-girl still. A young person stands in a quiet sunlit room, hand to their chest, expression soft and brave, as a single large translucent speech bubble floats beside them - and inside that bubble, drawn like a tiny illustration, is a small wooden door standing ajar with warm light spilling out.

Floral bokeh and drifting flower petals in the background, gentle gradient lighting, the characteristic shoujo shimmer of star-sparkles glittering in the air. The mood is vulnerable, honest and quietly courageous - admitting "I don't know" as an opening, not a defeat. Soft cel shading, romantic and warm, lovingly detailed. Square composition, no readable text, nothing clinical or cold.""",

    # 11 - Migrei de stack - fantasia epica 2010s, ponte entre ilhas
    """Epic 2010s fantasy-anime key visual, the sweeping cinematic look of a high-budget movie poster - dramatic scale, volumetric fog, rich saturated color. A lone traveler with a softly glowing backpack crosses a long swaying rope bridge suspended over a vast misty canyon, connecting two floating islands: the one behind washed in cool twilight blues, the one ahead glowing in warm amber dawn - two different worlds bridged by a single fragile path.

Deep atmospheric perspective with layered clouds, drifting light particles, distant birds wheeling in the gulf below, the traveler's cloak caught mid-wind. The backpack emits a quiet golden aura, suggesting carried knowledge crossing safely from one world to the next. Awe, transition, hope tinged with risk. Painterly detailed backgrounds, cinematic lighting, grand and emotional. Square composition, no readable text, nothing generic.""",

    # 12 - async/await erros - cyber digital 2000s, paineis de codigo
    """Early-2000s digital anime aesthetic with a cyber, Serial-Experiments-Lain flavor - glowing wireframes, faint scanlines, a moody green-on-black data-space, soft CRT bloom and pixel grain. A figure seen from behind floats in a dark void facing two enormous translucent vertical "code stream" panels: the left one bleeding angry red light that drips downward slowly, one drop at a time (sequential, choked); the right one pulsing calm green with many streams flowing in parallel harmony.

Glowing particles and holographic ripples fill the air, and a reflective black floor mirrors the panels like still water. Cool cyber palette of emerald, crimson and inky black, layered with atmospheric haze. Contemplative, slightly retro-futurist, the quiet beauty of concurrency made visible. Highly detailed, immersive, analog-meets-digital texture. Square composition, no readable real text except perhaps one faint glowing keyword. Nothing flat or generic.""",

    # 13 - Portfolio erros - gag-manga chibi comico, recruiter entediado
    """Comedic gag-manga anime style with chibi exaggeration - bouncy rounded characters, big expressive eyes, sweat-drops and emphasis lines, the playful energy of a 4-koma strip. A deadpan, bored chibi recruiter slouches in an office chair lazily thumb-scrolling a glowing phone, and floating out of the screen is a conveyor-belt row of nearly identical tiny "to-do app" boxes, all dull and grey, the recruiter's eyes half-lidded with boredom.

At the very end of the row, one single box glows golden and bursts with little sparkle-stars, and the recruiter's eyes suddenly snap wide and shiny with cartoon interest, a tiny "ping!" spark popping above their head. Bright flat cel colors, bold clean outlines, an off-white studio background with comic speed-lines. Light, funny, self-aware mood. Square composition, only a tiny short label at most, lively and hand-drawn, nothing static.""",

    # 14 - Seguranca junior - seinen sombrio, sala de servidores invadida
    """Dark, moody seinen anime aesthetic - heavy shadows, a muted desaturated palette, the tense atmosphere of a cyber-thriller OVA. A dim server room at night rendered in detailed perspective, towering racks blinking with tiny lights, a single large glowing padlock hovering protectively above a stylized database core that pulses softly blue. But on one side, a heavy door has been left carelessly ajar, hostile warm-red light leaking through the gap, and a small forgotten key glints on the floor right in front of it.

A shadowy silhouette looms just beyond the doorway, unseen by anyone inside. Volumetric haze drifts through the racks, cold blue safety light clashing with the intruding red, a reflective metal floor doubling every glow, fine mechanical detail everywhere. Suspenseful, ominous, cautionary mood. Cinematic seinen lighting, intricate and gritty. Square composition, no readable text, nothing clean or generic.""",

    # 15 - C#/.NET erros - moe 2010s fofo, cobra atras do presente
    """Bright, cute 2010s moe anime style - soft rounded shapes, pastel cheerfulness, sparkly highlights, the disarming charm that hides a trap. A wide-eyed cartoon developer-girl reaches eagerly toward a giant glossy gift box wrapped with an enormous ribbon, sparkles dancing all around it, completely unaware that a friendly-looking pastel snake (a "bug") with a sly little smile is coiled and peeking out from behind the box, tongue flicking.

Vivid candy palette of lavender, mint and bubblegum pink, clean confident cel shading, a soft gradient studio background dotted with floating sparkle-bokeh. The contrast of innocent cuteness and lurking danger is the entire joke. Expressive, charming, gently menacing mood. Square composition, at most a tiny short label like "async void", polished but warm and hand-illustrated, nothing sterile.""",

    # 16 - Aprender a programar erros - shounen 2010s, tunel de tutoriais
    """High-energy 2010s shounen anime key visual - dynamic perspective, glowing effects, intense determined emotion. A young learner is caught inside a swirling tunnel-vortex made of countless floating "play button" screens spiraling around them like a hypnotic whirlpool, dragging them in endless circles - but they strain forward, reaching with an outstretched hand toward a single distant blank editor window at the tunnel's end, from which real warm light pours out.

Saturated purple-to-electric-blue gradient, sharp motion lines and speed blur, glowing particles streaking past, a powerful rim light catching the protagonist's determined face. Dramatic, almost desperate yet hopeful - escaping passive consumption toward real creation. Cinematic, richly detailed, emotionally charged. Square composition, no readable text, vivid and kinetic, nothing flat.""",

    # 17 - Debounce vs throttle - sports-anime 2020s, dois corredores
    """Sleek modern 2020s sports-anime aesthetic, the crisp dynamic style of a contemporary running/athletics series - fluid motion, confident clean lines, vivid but tasteful color grading. Two runners on a stylized track seen in dramatic side profile: one sprints in erratic frantic bursts, multiple ghost-afterimages stacked chaotically behind them (debounce - only the final position counts); the other moves in steady, evenly-spaced strides, regular afterimages at fixed intervals like a metronome (throttle).

Strong horizontal motion composition with speed lines and wind streaks, a sunset-orange and cool-blue split palette dividing the two rhythms, glowing dust kicked up from the track. Energetic, precise, instructional-yet-cool mood - a key visual that makes a technical idea feel epic. Highly detailed motion effects, cinematic lighting. Square composition, no readable text, stylish and intentional.""",

    # 18 - Nomear bem - Ghibli biblioteca silenciosa, dando nomes
    """Quiet, contemplative Studio Ghibli-inspired interior - warm hand-painted watercolor, dust motes floating in shafts of late-afternoon light through tall windows. A cozy, cluttered library-study where a thoughtful character sits at a worn wooden desk, brush-pen in hand, carefully writing a single elegant label on a small wooden name-tag, surrounded by countless little drawers and jars each quietly waiting to be named - the whole room an archive of carefully chosen names.

Soft earthy palette of honeyed browns, deep greens and parchment cream, gouache textures, lovingly detailed clutter: stacked leather books, a steaming teacup, a curious cat watching from a shelf. The mood is calm, craftsmanlike and reverent - the quiet weight of naming things well. Painterly, nostalgic, deeply human. Square composition, no readable text, nothing sterile or digital.""",

    # 19 - Ler stack trace - noir detetive anime, lendo um pergaminho
    """Moody detective-noir anime aesthetic, late-80s/90s mystery OVA vibe - dramatic chiaroscuro shadows, smoky atmosphere, a single hard light source, a muted sepia-and-teal palette. A sharp-eyed developer-detective in a long coat stands beneath a flickering lamp, intently reading an impossibly long paper scroll (a "stack trace") that unfurls from their hands all the way to the floor and curls across the room, a magnifying glass in one hand catching a single highlighted line glowing faintly red.

A rain-streaked window glows behind them, venetian-blind shadows striping the whole scene, faint smoke-haze curling through the light, scattered case-file papers pinned to a corkboard with red string. Tense, analytical, cinematic mood - the trace as a trail of clues, not an accusation. Richly inked detail, film-noir grain. Square composition, no readable text, atmospheric and intentional.""",

    # 20 - Melhor dev nao digita mais rapido - slice-of-life 2010s, time
    """Warm 2010s slice-of-life anime aesthetic, the gentle workplace-drama look - soft natural lighting, a relatable detailed office setting, expressive but understated characters. In an open-plan studio, one developer hammers furiously at a keyboard in a blur of motion lines and flying sparks, surrounded by chaos and crumpled paper; nearby, another developer sits calmly leaning back, eyes closed in thought, a single quiet lightbulb glow hovering above them, a half-finished cup of tea steaming, radiating unhurried clarity.

A cozy muted palette of warm woods, soft greens and afternoon light pouring through big windows, with plants, sticky-notes and mugs detailing the lived-in space. A subtle, sympathetic contrast between frantic speed and calm thinking - neither mocked. Tender, observational, quietly wise mood. Detailed background, painterly cel shading. Square composition, no readable text, human and lived-in.""",

    # 21 - IA nao rouba vaga - Shinkai crepusculo, corredores
    """Makoto Shinkai-style dusk scene - a radiant gradient sky of violet, rose and burning orange, hyper-detailed layered clouds, glowing atmosphere and soft lens flares. Two silhouetted runners race along an elevated train track at twilight: one runs alone, straining; just ahead, the other runs with a small luminous arrow-shaped aura of light trailing from their feet, propelled slightly faster - both rendered as crisp backlit figures against the blazing sky.

Vast cinematic depth, distant city lights just beginning to twinkle below, shimmering particles and warm bloom, long dramatic shadows stretching across the rails. The mood is bittersweet and urgent - not man-versus-machine but human-versus-human-with-leverage. Breathtaking painterly background, emotional and luminous. Square composition, no readable text, awe-inspiring and intentional.""",

    # 22 - 200 vagas vs construir em publico - gag-manga energico
    """Energetic comedic gag-manga style - exaggerated expressions, bold ink, speed-lines, the chaotic fun of a Shonen Jump gag panel. On the left, a frazzled character with crazy spinning eyes hurls a towering stack of paper resumes into a swirling dark void, papers scattering everywhere, none of them landing, sweat flying off their face. On the right, the same character - now serene with a tiny halo - calmly stacks glowing blocks into a small radiant tower while little chibi figures wander toward it on their own, drawn in.

Punchy flat colors with a single green accent on the tower, an off-white background with comic emphasis lines and a few sparkle-stars, a dynamic split composition. Funny, self-deprecating, clever mood. Clean bold cel outlines, lively and hand-drawn. Square composition, at most a tiny short label, nothing static or generic.""",

    # 23 - Startups IA wrapper - Akira neon, presente oco revelado
    """Detailed 80s Akira/Otomo-inspired cyberpunk anime - dense line work, a neon-noir palette of hot magenta, acid green and deep black, wet reflective surfaces, glowing signage haze. A flashy gift box wrapped in shimmering holographic "AI" foil sits center-frame, but a hand is peeling back the wrapping to reveal it is hollow inside - empty except for a single thin glowing tube snaking out the back, tethering it to a colossal distant corporate server-tower looming in the smoggy cityscape, owned by someone else.

A dramatic low-angle composition, volumetric neon light shafts cutting through the haze, chromatic glow, drifting rain particles, that gritty retro-future film grain. Ironic, revealing, faintly cynical mood - the illusion of substance exposed. Ultra-detailed, cinematic, with analog cel texture. Square composition, no readable text, richly atmospheric.""",

    # 24 - Certificacao nao impressiona - shounen heroico, trofeu
    """Triumphant shounen anime key visual - bold heroic lighting, a dynamic low angle, a glowing power-aura, the proud climax-of-the-arc energy. A confident young developer holds aloft a single glowing "working app" like a radiant trophy, light bursting from it, eyes shining with earned pride. Behind them, slightly out of focus and unstable, a ridiculous teetering tower of identical certificate-medals wobbles and begins to topple, completely ignored.

A saturated gold-and-blue palette, dramatic god-rays and sparkle particles, a wind-swept jacket flaring like a cape, speed lines radiating outward from the trophy. Crisp modern cel shading with cinematic bloom. Empowering, a little cheeky, victorious mood - substance over collection. Detailed, kinetic, emotionally charged. Square composition, no readable text, vivid and intentional.""",

    # 25 - Race condition - thriller psicologico, colisao de setas
    """Tense psychological-thriller anime aesthetic, the razor-sharp stillness of a Death-Note-style standoff - extreme close framing, a dramatic spotlight, deep black negative space, a sliver of cold blue and one stab of warning red. Two identical glowing arrows reach in from opposite edges of the frame toward a single small data-block at the exact center at the very same instant, frozen a heartbeat before collision, a tiny crackling spark igniting where they are about to clash.

High-contrast lighting, faint motion blur on the converging arrows, an oppressive sense of timing and inevitability hanging in the air. Muted near-monochrome with that single red collision accent, cinematic and claustrophobic. Suspenseful, precise, ominous mood - the silent danger of concurrency made visible. Ultra-detailed, theatrical. Square composition, no readable text, nothing flat.""",

    # 26 - Idempotencia - sonho surreal Satoshi Kon, entregas repetidas
    """Whimsical surreal dream-anime, the gently impossible logic of a Satoshi Kon dream sequence - a soft pastel palette, floaty lighting, reality bending kindly. A delivery courier hands the exact same glowing parcel to a calm recipient three times in an endless looping motion-trail, the duplicate parcels fading into translucent ghosts as the recipient serenely accepts only the first and lets the copies dissolve into drifting light-petals.

Muted teal, warm coral and cream tones, dreamy bokeh, repeating echo-afterimages curving softly through the air, a quiet surreal stillness despite all the repetition. Painterly soft edges, floating particles, a faintly humorous serenity. Clever, calm, slightly magical mood - sameness made safe. Detailed and atmospheric. Square composition, no readable text, nothing sterile.""",

    # 27 - Timezone/UTC - gag-anime barulhento, panico de relogios
    """Loud comedic gag-anime style - exaggerated panic, popping expressions, chaotic energy, the over-the-top humor of a sitcom anime. A split vertical composition: in the calm top half, a relaxed chibi developer gives a confident thumbs-up, little sparkles of false security around them; in the frenzied bottom half, the very same developer is mid-scream, hair standing on end, comically flailing while a whirlwind of dozens of clocks - each showing a different time - and wildly flipping calendar pages tornadoes around their head.

Bright punchy flat colors, bold black outlines, motion lines, sweat-drops and a few cartoon stars-of-pain, an off-white studio background with emphasis bursts. Hilarious, relatable, kinetic mood - the universal timezone meltdown. Clean expressive cel art with a hand-drawn feel. Square composition, at most a tiny short label like "UTC", nothing flat or generic.""",

    # 28 - Voce nao e seu codigo - Ghibli contemplativo, colina ao amanhecer
    """Serene, contemplative Studio Ghibli-inspired scene - a soft watercolor sky at dawn, a gentle pastel gradient, a single quiet figure in a wide tranquil landscape. A person sits peacefully on a grassy hill at sunrise, knees hugged to their chest, gazing calmly at a separate softly-glowing translucent block of abstract "code" floating gently a little distance away from them - clearly close, but distinctly apart, a small respectful gap of air between self and creation.

A tender palette of misty lavender, pale gold and dewy green, drifting seed-fluff and morning haze, painterly brush textures, a few birds far off in the sky. The mood is calm, healing and gently profound - separating worth from work, ego from output. Lovingly detailed natural background, warm and human. Square composition, no readable text, nothing cold or clinical.""",

    # 29 - Simplicidade feature dificil - seinen artesao, esculpindo cubo
    """Detailed seinen craftsman-anime aesthetic, the focused intensity of a master-artisan series - warm workshop lighting, fine textural detail, reverent realism. A split scene: on the left, a figure effortlessly and carelessly piles up a tall teetering tower of random mismatched blocks, chaos stacking itself for free; on the right, the same figure sweats and strains with chisel and mallet, painstakingly carving a single flawless smooth cube out of a rough heavy block of stone, marble dust drifting through the lamplight.

A warm amber workshop glow set against cool shadow, gritty tactile textures everywhere - wood grain, raw stone, sweat, tool marks - with a single calm blue accent on the finished cube. The composition contrasts effortless mess with hard-won simplicity. Respectful, intense, quietly heroic mood. Richly detailed, painterly cel art. Square composition, no readable text, deeply analog.""",

    # 30 - Constancia vence talento - Shinkai vista epica, escadaria
    """Sweeping Makoto Shinkai-style epic vista - a luminous endless sky of layered clouds glowing gold and rose at the horizon, hyper-detailed and breathtaking. A vast staircase built from countless identical small blocks ascends from the foreground up toward a radiant distant goal-light high in the sky. A tiny steady silhouetted figure climbs one patient step at a time, while lower down, faded translucent figures who sprinted ahead sit slumped and exhausted on the steps, left behind by persistence.

Cinematic scale and deep atmospheric perspective, drifting light particles, soft volumetric god-rays, long gentle shadows running down the stairs, that signature Shinkai bloom and saturation over everything. The mood is quietly triumphant, motivational without being loud - consistency outlasting raw talent. Painterly, emotional, grand. Square composition, no readable text, awe-inspiring and intentional.""",
]

# ----------------------------------------------------------------------------
# Configuracoes
# ----------------------------------------------------------------------------
MODEL = "gpt-image-1"      # modelo de geracao de imagem mais atual da OpenAI
SIZE = "1024x1024"          # quadrado, ideal para feed do LinkedIn
OUTPUT_DIR = "imagens"
SLEEP_BETWEEN = 8            # segundos entre chamadas, para respeitar rate limit
MAX_RETRIES = 3             # tentativas por imagem em caso de erro transitorio


def main():
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("ERRO: variavel de ambiente OPENAI_API_KEY nao encontrada.")
        print("Configure a chave antes de rodar (veja o cabecalho deste arquivo).")
        sys.exit(1)

    try:
        from openai import OpenAI
    except ImportError:
        print("ERRO: biblioteca 'openai' nao instalada. Rode: pip install --upgrade openai")
        sys.exit(1)

    client = OpenAI()  # le OPENAI_API_KEY do ambiente automaticamente

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    total = len(PROMPTS)
    print(f"Iniciando geracao de {total} imagens com o modelo '{MODEL}' ({SIZE}).\n")

    sucessos = 0
    falhas = []

    for i, prompt in enumerate(PROMPTS, start=1):
        caminho = os.path.join(OUTPUT_DIR, f"post_{i:02d}.png")

        if os.path.exists(caminho):
            print(f"[{i}/{total}] Ja existe ({caminho}) - pulando.")
            sucessos += 1
            continue

        print(f"[{i}/{total}] Gerando {i}/{total}...", flush=True)

        ok = False
        for tentativa in range(1, MAX_RETRIES + 1):
            try:
                resp = client.images.generate(
                    model=MODEL,
                    prompt=prompt,
                    size=SIZE,
                    n=1,
                )
                b64 = resp.data[0].b64_json
                with open(caminho, "wb") as f:
                    f.write(base64.b64decode(b64))
                print(f"        OK -> {caminho}")
                ok = True
                sucessos += 1
                break
            except Exception as e:
                espera = SLEEP_BETWEEN * tentativa
                print(f"        Erro (tentativa {tentativa}/{MAX_RETRIES}): {e}")
                if tentativa < MAX_RETRIES:
                    print(f"        Aguardando {espera}s antes de tentar de novo...")
                    time.sleep(espera)

        if not ok:
            print(f"        FALHOU apos {MAX_RETRIES} tentativas: post_{i:02d}")
            falhas.append(i)

        # pausa entre chamadas para respeitar rate limit (exceto na ultima)
        if i < total:
            time.sleep(SLEEP_BETWEEN)

    print("\n" + "=" * 50)
    print(f"Concluido. Sucesso: {sucessos}/{total}.")
    if falhas:
        print(f"Falharam os posts: {falhas}")
        print("Rode o script de novo para retentar apenas os que faltam.")
    else:
        print(f"Todas as imagens estao em ./{OUTPUT_DIR}/")
    print("=" * 50)


if __name__ == "__main__":
    main()
