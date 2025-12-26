
```markdown
# 📦 Sistema de Contagem de Produtos com IA (YOLOv8)

Este projeto utiliza Visão Computacional para detectar e contar objetos em tempo real através da webcam ou imagens, utilizando a biblioteca **Ultralytics YOLOv8**. O sistema conta com um filtro de estabilização para evitar oscilações na contagem e gera logs automáticos em arquivo `.txt`.

## 🚀 Funcionalidades

* **Detecção em Tempo Real:** Identificação de objetos via webcam.
* **Estabilização Dinâmica:** Utiliza média móvel (buffer) para evitar que o contador "pule" devido a sombras ou reflexos.
* **Log de Dados:** Gravação automática da quantidade detectada com data e hora.
* **Interface Limpa:** Exibe apenas os retângulos de detecção e a quantidade total na tela.

## 🛠️ Pré-requisitos

Antes de rodar o projeto, você precisa ter o Python instalado. Recomenda-se a versão 3.10 ou superior.

### Instalação das dependências:
Abra o seu terminal e execute:
```bash
pip install ultralytics opencv-python

```

## 💻 Como Usar

1. Clone este repositório ou copie o arquivo `main.py`.
2. Conecte sua webcam.
3. Execute o script:
```bash
python main.py

```


4. Pressione a tecla **'q'** para encerrar o programa.

## 📂 Estrutura de Arquivos

* `main.py`: Código principal do sistema.
* `yolov8n.pt`: Modelo de IA (baixado automaticamente no primeiro uso).
* `contagem_estabilizada.txt`: Log gerado com o histórico de contagens.

## ⚙️ Ajustes de Sensibilidade

Caso a contagem ainda apresente pequenas oscilações, você pode ajustar as seguintes variáveis no código:

* `conf=0.4`: Aumente para tornar a IA mais rigorosa ou diminua para detectar objetos mais difíceis.
* `tamanho_buffer = 10`: Aumente para uma contagem mais travada/estável, ou diminua para uma resposta mais rápida a mudanças.

## 📝 Licença

Este projeto é para fins educacionais e de estudo em Visão Computacional.

```

---



```
