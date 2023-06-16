import cv2 as cv

# Abre o arquivo de video
input_video = cv.VideoCapture('./assets/arsene.mp4')

# Checa se foi possivel abrir o arquivo
if not input_video.isOpened():
    print("Error opening video file")
    exit(1)

# Como foi possível abrir o video de entrada, vamos agora utilizar 
# essa captura para definir o tamanho do video de saida
width  = int(input_video.get(cv.CAP_PROP_FRAME_WIDTH))   # float `width`
height = int(input_video.get(cv.CAP_PROP_FRAME_HEIGHT))

# Cria a estrutura do video de saida
# Com formato e local do arquivo de saida
# Codec utilizado
# FPS do video e
# Tamanho do video
output_video = cv.VideoWriter( './saida/out.mp4',cv.VideoWriter_fourcc(*'mp4v'), 20, (width, height))

# Loop de leitura frame por frame

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    # Le um frame do video e, guarda o resultado da leitura
    # Se nao houver mais frames disponiveis, ret sera falso
    ret, frame = input_video.read()
    # Se nao conseguiu ler o frame, para o laco
    if not ret:
        break


    grayscale = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(image=grayscale, scaleFactor=1.1, minNeighbors=3)

    for (x, y, w, h) in faces:
        cv.rectangle(
            img=frame,
            pt1=(x, y), # coords cima retangulo
            pt2=(x + w, y + h), # coors baixo retangulo
            color=(0, 0, 255), # Cor do retangulo BGR
            thickness=2  # grossura retangulo
        )

    # Exibe o frame
    cv.imshow('Video Playback', frame)
    
    # Escreve o frame no output
    output_video.write(frame)

    if cv.waitKey(30) & 0xFF == ord('q'):
        break
    
# Fecha tudo
output_video.release()
input_video.release()
cv.destroyAllWindows()