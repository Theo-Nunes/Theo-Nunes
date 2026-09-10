"""
Script para gerar header visual de fusão entre Engenharia e Programação.
Combina elementos visuais de otimização de processos, automação e IA.
"""

from PIL import Image, ImageDraw, ImageFont
import random
from pathlib import Path


class EngineeringHeaderGenerator:
    """Gerador de headers personalizados com tema de engenharia e programação."""
    
    def __init__(self, width=1920, height=600):
        self.width = width
        self.height = height
        self.colors = {
            'bg': (10, 15, 30),
            'primary': (0, 200, 255),
            'secondary': (50, 255, 100),
            'accent': (255, 150, 50),
            'code': (150, 200, 255),
            'text': (240, 240, 240),
            'dark_text': (100, 100, 100)
        }
    
    def _draw_data_stream(self, draw):
        """Desenha o rio de dados na base da imagem."""
        for x in range(0, self.width, 10):
            for y in range(self.height - 150, self.height, 5):
                opacity = random.randint(30, 100)
                # Simula fluxo de dados com pontos aleatórios
                draw.point((x, y), fill=self.colors['primary'])
    
    def _draw_optimization_factory(self, draw):
        """Desenha a fábrica de otimização com código."""
        # Estrutura principal
        factory_left = self.width // 4
        factory_top = self.height // 2
        factory_right = 3 * self.width // 4
        factory_bottom = self.height - 50
        
        draw.rectangle(
            [factory_left, factory_top, factory_right, factory_bottom],
            fill=(20, 30, 50),
            outline=self.colors['primary'],
            width=2
        )
        
        # Código da otimização
        code_lines = [
            "def optimize_process(data):",
            "  workflow = load_data(data)",
            "  bottlenecks = identify(workflow)",
            "  for task in bottlenecks:",
            "    if task.is_critical:",
            "      allocate_resources(task)",
            "  return optimized_workflow"
        ]
        
        y_offset = factory_top + 20
        for line in code_lines:
            draw.text(
                (factory_left + 20, y_offset),
                line,
                fill=self.colors['code']
            )
            y_offset += 18
    
    def _draw_robots(self, draw):
        """Desenha robôs inteligentes articulados."""
        robot_y = self.height - 150
        
        for i in range(2):
            robot_x = self.width // 2 + i * 200 - 100
            
            # Corpo do robô
            draw.rectangle(
                [robot_x, robot_y, robot_x + 80, robot_y + 100],
                fill=(30, 45, 75),
                outline=self.colors['secondary'],
                width=2
            )
            
            # Braço robótico
            draw.line(
                [robot_x + 40, robot_y + 100, robot_x + 120, robot_y + 180],
                fill=self.colors['secondary'],
                width=5
            )
            
            # Cabeça do robô
            draw.ellipse(
                [robot_x + 15, robot_y - 30, robot_x + 65, robot_y],
                fill=self.colors['secondary'],
                outline=self.colors['secondary']
            )
    
    def _draw_ai_clouds(self, draw):
        """Desenha nuvens de simulação e IA."""
        cloud_labels = ["⚡ SIMULATION", "🤖 AI", "⚙️ AUTOMATION"]
        
        for i in range(3):
            cloud_x = random.randint(100, self.width - 300)
            cloud_y = random.randint(50, 200)
            
            # Nuvem
            draw.ellipse(
                [cloud_x, cloud_y, cloud_x + 200, cloud_y + 80],
                fill=(40, 60, 100),
                outline=self.colors['accent'],
                width=1
            )
            
            # Label
            try:
                font = ImageFont.truetype("arial.ttf", 12)
            except IOError:
                font = ImageFont.load_default()
            
            draw.text(
                (cloud_x + 15, cloud_y + 30),
                cloud_labels[i],
                fill=self.colors['text'],
                font=font
            )
    
    def _draw_title(self, draw):
        """Desenha o título principal."""
        try:
            font_title = ImageFont.truetype("arial.ttf", 55)
        except IOError:
            font_title = ImageFont.load_default()
        
        title_text = "⚙️ ENGINEERING + PROGRAMMING FUSION 💻"
        bbox = draw.textbbox((0, 0), title_text, font=font_title)
        text_width = bbox[2] - bbox[0]
        
        title_x = (self.width - text_width) // 2
        
        draw.text(
            (title_x, 40),
            title_text,
            fill=self.colors['text'],
            font=font_title
        )
    
    def generate(self, output_path="github_header.png"):
        """Gera a imagem do header completa."""
        # Cria a imagem
        img = Image.new('RGB', (self.width, self.height), color=self.colors['bg'])
        draw = ImageDraw.Draw(img)
        
        # Desenha componentes
        self._draw_data_stream(draw)
        self._draw_optimization_factory(draw)
        self._draw_robots(draw)
        self._draw_ai_clouds(draw)
        self._draw_title(draw)
        
        # Salva
        img.save(output_path)
        print(f"✅ Header gerado com sucesso em: {output_path}")
        return output_path


def main():
    """Função principal."""
    generator = EngineeringHeaderGenerator()
    generator.generate("github_header.png")


if __name__ == "__main__":
    main()
