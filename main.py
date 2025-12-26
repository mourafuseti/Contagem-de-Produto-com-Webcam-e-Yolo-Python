import cv2
from ultralytics import YOLO
from datetime import datetime
import time

# 1. Configurações Iniciais
model = YOLO('yolov8n.pt')
cap = cv2.VideoCapture(0)

def registrar_log(quantidade):
    """Salva apenas a quantidade no arquivo TXT"""
    if quantidade > 0:
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        with open("contagem_produtos.txt", "a", encoding="utf-8") as f:
            f.write(f"[{data_hora}] Quantidade detectada: {quantidade}\n")

ultima_gravacao = time.time()
intervalo_log = 5 

print("Webcam aberta! Apenas quantidade sendo exibida. Pressione 'q' para sair.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 3. Reconhecimento da IA
    results = model(frame, conf=0.4)
    
    # Pegamos a lista de caixas detectadas
    caixas = results[0].boxes
    qtd = len(caixas)

    for box in caixas:
        # Pegar apenas as coordenadas para desenhar o retângulo
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        
        # Desenha apenas o retângulo (sem o texto do nome)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # 4. Exibir apenas a Quantidade Total no topo
    cv2.putText(frame, f"Quantidade: {qtd}", (20, 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)

    # 5. Salvar no TXT
    tempo_atual = time.time()
    if tempo_atual - ultima_gravacao > intervalo_log:
        registrar_log(qtd)
        ultima_gravacao = tempo_atual

    # 6. Mostrar imagem
    cv2.imshow('Contagem de Produtos', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()