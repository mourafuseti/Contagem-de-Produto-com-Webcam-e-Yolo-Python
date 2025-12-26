# 👋🏻 Leonardo de Moura Fuseti

Estudante de Defesa Cibernetica no Polo Estacio Piumhi MG . Formação tecnica em Tecnico em Redes de Computadores no IFMG Bambui MG , intusiasta na programação gostando muito de Python e evoluindo dia a dia .

### Conecte-se comigo

[![Perfil DIO](https://img.shields.io/badge/-Meu%20Perfil%20na%20DIO-30A3DC?style=for-the-badge)](https://www.dio.me/users/mourafuseti)
[![E-mail](https://img.shields.io/badge/-Email-000?style=for-the-badge&logo=microsoft-outlook&logoColor=E94D5F)](mailto:mourafuseti@gmail.com)
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-000?style=for-the-badge&logo=linkedin&logoColor=30A3DC)](https://www.linkedin.com/in/leonardo-moura-fuseti-4052b0359/)

### Habilidades

![HTML](https://img.shields.io/badge/HTML-000?style=for-the-badge&logo=html5&logoColor=30A3DC)
![CSS3](https://img.shields.io/badge/CSS3-000?style=for-the-badge&logo=css3&logoColor=E94D5F)
![JavaScript](https://img.shields.io/badge/JavaScript-000?style=for-the-badge&logo=javascript&logoColor=F0DB4F)
![Sass](https://img.shields.io/badge/SASS-000?style=for-the-badge&logo=sass&logoColor=CD6799)
![Bootstrap](https://img.shields.io/badge/bootstrap-000?style=for-the-badge&logo=bootstrap&logoColor=553C7B)
[![Git](https://img.shields.io/badge/Git-000?style=for-the-badge&logo=git&logoColor=E94D5F)](https://git-scm.com/doc)
[![GitHub](https://img.shields.io/badge/GitHub-000?style=for-the-badge&logo=github&logoColor=30A3DC)](https://docs.github.com/)



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




---

## 🚀 Vamos desenvolver seu projeto de IA?

Se você precisa de uma solução personalizada de Visão Computacional ou Inteligência Artificial para o seu negócio, entre em contato:

📩 **Desenvolvimento de Projetos em IA** 📱 **WhatsApp:** [Clique aqui para falar conosco: (35) 99903-7763](https://wa.me/5535999037763)
