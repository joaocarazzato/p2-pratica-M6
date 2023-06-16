# Prova Prática 2 Módulo 6
# Reconhecimento Facial utilizando Haar Cascade
Aplicação do Haar Cascade para detecção de faces em um vídeo.

### Implementação

Para criar e conseguir usufruir desse código, precisamos importar o OpenCV primeiramente, com o seguinte comando:

```python
import cv2 as cv
```

Após isso, necessitamos capturar o vídeo com um comando do OpenCV e capturar suas medidas(altura e largura):

```python
input_video = cv.VideoCapture('./assets/arsene.mp4')
width  = int(input_video.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(input_video.get(cv.CAP_PROP_FRAME_HEIGHT))
```
Dessa forma, o vídeo será aberto da forma correta, utilizando suas próprias medidas a fim de evitar erros. Com isso podemos iniciar a captura de vídeo através do comando VideoWriter, passando o nome e diretório de saída, seu codec, frame e dimensões(as mesmas do vídeo).

Após isso carregamos o modelo que usaremos do HaarCascade através do comando CascadeClassifier, então, podemos iniciar o loop infinito de captura do vídeo e de passagem pelo modelo. Dentro desse loop, capturamos os frames que estão passando pelo vídeo no comando de VideoCapture e aplicamos um filtro de grayscale(aperfeiçoando um pouco o modelo, senti que ele fica um pouco mais correto dessa forma apesar de ainda demonstrar problemas). Quando a imagem tiver seu filtro aplicado, podemos passá-la pelo modelo através do comando detectMultiScale com os parâmetros de escala da imagem e de quantos vizinhos cada retângulo deve ter para ser mantido na imagem.

Quando a imagem passar pelo modelo, podemos aplicar os retângulos encontrados para cada rosto utilizando um for e o comando retangle, passando os parâmetros de coordenada, cor e grossura, assim, finalizamos o código apresentando o vídeo usando o "imshow", escrevendo o vídeo utilizando o write para cada frame, e assim que os frames acabarem, fechando todos os processos do OpenCV de forma correta.
