# Reconhecimento de Gestos Manuais
Este projeto utiliza a biblioteca MediaPipe e OpenCV para reconhecer gestos manuais em tempo real por meio de uma webcam.

## Tecnologias Utilizadas
- Python
- OpenCV
- MediaPipe

## Dependências
Antes de executar o código, certifique-se de instalar as dependências necessárias:

```bash
pip install opencv-python mediapipe numpy
```

## Como Executar
1. Clone o repositório localmente usando o comando:

```bash
git clone https://github.com/devmarangoni/IA-Hand-Gesture-Recognition.git
```

2. Acesse o diretório do projeto:

```bash
cd IA-Hand-Gesture-Recognition
```

3. Certifique-se de que sua webcam está funcionando.
4. Execute o script com o comando:

```bash
python handGestureRecognition.py
```

5. A saída de vídeo será exibida com a detecção de gestos e a contagem de gestos reconhecidos.
6. Pressione `q` para encerrar a execução.

## Mapeamento de Gestos
O código reconhece diferentes gestos baseados nas posições dos dedos. Alguns exemplos incluem:
- **Mão aberta**
- **Punho fechado**
- **Símbolo da paz**
- **Joinha** (Polegar para cima)
- **OK**
- **Chifre do rock**

## Personalização
Caso queira adicionar novos gestos, edite o dicionário `gestureMap` no código e ajuste as condições de reconhecimento.
