# DataAugNet
O objetivo deste projeto é desenvolver um pipeline eficiente e flexível para a criação de datasets voltados para redes de segmentação (UNET) e detecção de objetos (YOLO). O pipeline irá incluir diversas opções de augmentação de imagem.

### Ferramentas que serão utilizadas
- Streamlit para fornecer uma interface simples e rápida
- Numpy, pandas, opencv e outras

## Componentes do Projeto:
### Aquisição e Preparação dos Dados:

- Coleta de Imagens: Reunir um conjunto de imagens de diferentes fontes que se alinhem com os requisitos de segmentação e detecção de objetos.
- Anotação: Utilizar ferramentas de anotação como LabelMe (inicialmente vamos focar em uma ferramenta) para criar máscaras para segmentação de objetos.
- Caixas delimitadoras (bounding boxes) para detecção será em otura etapa.
- O pipeline deverá ser capaz de trabalhar com diferentes labels em uma mesma imagem (vamos restringir somente o polígono no momento)
  
### Pipeline de Augmentação:

- Albumentations: as augmentações incluem, mas não estão limitadas a:
- Transformações Geométricas: Rotação, translação, escalonamento, corte, etc.
- Transformações de Cor: Ajustes de brilho, contraste, saturação, etc.
- Ruído e Desfoque: Adição de ruído gaussiano, desfoque por movimento, desfoque gaussiano, etc.
- Transformações Avançadas: Elasticidade, grid distortion, optical distortion, etc.

### Criação de Datasets:

- Divisão de Dados: Dividir o dataset em conjuntos de treinamento, validação e teste, garantindo uma distribuição equilibrada. Aqui deve ser uma etapa opcional, caso o usuário deseje deverá indicar as proporções.
Formato dos Dados:
- UNET: Imagens de entrada e máscaras correspondentes para segmentação.
- YOLO: Imagens de entrada e arquivos de anotação no formato coco.

### Treinamento e Avaliação:
- No primeiro momento essa ação é descartada, mas futuramente a ideia é treinar na própria aplicação.
- Configuração do Treinamento: Definir hiperparâmetros e configurações específicas para treinar modelos UNET e YOLO utilizando os datasets criados.
- Avaliação do Desempenho: Implementar métricas de avaliação como IoU (Intersection over Union) para UNET e mAP (mean Average Precision) para YOLO.

### Resultados Esperados:
- Aumento da Variedade de Dados: Aumentações eficazes que geram maior diversidade nos dados de treinamento, melhorando a robustez e generalização dos modelos.
- Automação e Eficiência: Pipeline automatizado que facilita a criação e augmentação de datasets, economizando tempo e recursos.
- Flexibilidade: Opções configuráveis para augmentações que permitem ajustes finos conforme os requisitos específicos dos projetos de segmentação e detecção.

## Conclusão:
Este projeto visa fornecer uma ferramenta flexível para pesquisadores e engenheiros que trabalham com redes UNET e YOLO, possibilitando a criação de datasets ricos e variados através de técnicas avançadas de augmentação com Albumentations. A documentação e exemplos inclusos vão grantir que o pipeline possa ser facilmente utilizado e adaptado a diferentes necessidades e projetos.
