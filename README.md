# Olá! Eu sou o Théo Alves Nunes 👋

<p align="center">
  <img src="github_contribution_animated.gif" alt="Animação de Contribuição GitHub" width="100%">
</p>

Sou estudante universitário na área de Engenharia/Ciências Exatas e atuo profissionalmente no setor administrativo em Goiás. Tenho forte interesse em otimização de processos, programação, organização de dados e estruturação de novos negócios.

---

## 🚀 Sobre Mim
- 🎓 Estudante de exatas com forte base analítica (Cálculo, Álgebra Linear e Mecânica Vetorial).
- 🏛️ Atuo na área administrativa do setor público (SIC/Goiás), com foco na elaboração, revisão e otimização de ofícios, despachos e fluxos institucionais.
- 📚 Atuo como monitor acadêmico, elaborando relatórios pedagógicos e auxiliando no progresso de turmas.
- 💡 Atualmente estruturando um projeto empreendedor focado em serviços de manutenção multidisciplinar ("Marido de Aluguel").

## 💻 Habilidades e Ferramentas
- **Linguagens e Lógica:** Python (focado em processamento de listas, automação e cálculo de dados).
- **Análise e Gestão de Dados:** Excel Avançado (Tabelas Dinâmicas, extração e consolidação de grandes volumes de dados).
- **Comunicação Institucional:** Redação oficial de alto padrão, revisão de concordância e objetividade.
- **Tecnologia:** Uso de ferramentas de IA (Google AI Studio) para otimização de fluxos de trabalho.

## 📈 Interesses
- 📊 **Criptoeconomia:** Acompanhamento de tendências de mercado, projeções e simulações de investimento, com foco em Ethereum (ETH).
- 🎮 **Gaming:** Jogador de PlayStation (Rainbow Six Siege).
- 🛠️ **Empreendedorismo:** Coordenação de demandas comerciais e parcerias estratégicas.

---

## 🖼️ Geração Criativa da Capa

Para criar a imagem do header acima, imaginei um script Python que funde elementos de Engenharia de Produção e Programação em uma paisagem tecnológica e orgânica. O script abaixo não gera a imagem *exata* (que foi criada por uma IA com base nessa lógica), mas demonstra como eu construiria essa visualização programaticamente usando Python.

### 🐍 `header_generator.py`

```python
import PIL.Image as Image
import PIL.ImageDraw as ImageDraw
import PIL.ImageFont as ImageFont
import math
import random

# Configurações da imagem
W, H = 1920, 600
COLORS = {
    'bg': (10, 15, 30),
    'primary': (0, 200, 255),
    'secondary': (50, 255, 100),
    'accent': (255, 150, 50),
    'code': (150, 200, 255, 180),
    'text': (240, 240, 240)
}

def generate_engineering_fusion_header(output_path="github_header.png"):
    # 1. Cria a tela
    img = Image.new('RGB', (W, H), color=COLORS['bg'])
    draw = ImageDraw.Draw(img)

    # 2. Gera a base de dados (o rio de dados)
    for x in range(0, W, 10):
        for y in range(H - 150, H, 5):
            opacity = random.randint(30, 100)
            draw.point((x, y), fill=(*COLORS['primary'], opacity))

    # 3. Desenha os "Edifícios de Processo" formados por código
    # Fábrica de Otimização (Otimização de Processos)
    draw.rectangle([W//4, H//2, 3*W//4, H-50], fill=(20, 30, 50), outline=COLORS['primary'])
    
    # Inserir código simulado dentro do edifício
    code_lines = [
        "def optimize_process(data):",
        "  workflow = load_data(data)",
        "  bottlenecks = identify(workflow)",
        "  for task in bottlenecks:",
        "    if task.is_critical:",
        "      allocate_resources(task)",
        "  return optimized_workflow"
    ]
    y_offset = H // 2 + 20
    for line in code_lines:
        draw.text((W // 4 + 20, y_offset), line, fill=COLORS['code'])
        y_offset += 15

    # 4. Desenha os Robôs (formados por loops e lógica)
    for i in range(2):
        bx, by = W//2 + i*200 - 100, H-150
        draw.rectangle([bx, by, bx+80, by+100], fill=(30, 45, 75), outline=COLORS['secondary'])
        # Braço robótico articulado
        draw.line([bx+40, by+100, bx+120, by+180], fill=COLORS['secondary'], width=5)

    # 5. Adiciona nuvens de IA e Simulação
    for i in range(3):
        cx, cy = random.randint(100, W-100), random.randint(100, 200)
        draw.ellipse([cx, cy, cx+200, cy+100], fill=(40, 60, 100, 150))
        draw.text((cx+20, cy+20), "SIMULATION & AI", fill=COLORS['text'])

    # 6. Título principal
    try:
        font_title = ImageFont.truetype("arial_bold.ttf", 60)
    except IOError:
        font_title = ImageFont.load_default()
        
    title_text = "ENGINEERING + PROGRAMMING FUSION"
    draw.text((W//2 - 400, 50), title_text, font=font_title, fill=COLORS['text'])

    # Salva a imagem
    img.save(output_path)
    print(f"Header gerado em {output_path}")

if __name__ == "__main__":
    generate_engineering_fusion_header()
