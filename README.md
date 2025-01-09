BrasArg - Imigração do Brasil e da Argentina para o Canadá
Descrição / Description
Português: Este projeto visualiza a imigração do Brasil e da Argentina para o Canadá entre 1980 e 2013. Ele usa o Plotly para criar gráficos interativos animados e Pandas para manipulação de dados. A animação mostra o número de imigrantes de ambos os países ao longo do tempo, permitindo uma comparação visual das tendências de imigração.

English: This project visualizes immigration from Brazil and Argentina to Canada between 1980 and 2013. It uses Plotly to create interactive animated plots and Pandas for data manipulation. The animation shows the number of immigrants from both countries over time, allowing a visual comparison of immigration trends.

Tecnologias Usadas / Technologies Used
Python: Linguagem de programação usada para manipular dados e gerar gráficos interativos.
Plotly: Biblioteca de visualização para criar gráficos interativos e animações.
Pandas: Biblioteca para manipulação de dados, leitura de arquivos CSV e transformação dos dados para o formato desejado.
VS Code: Editor de código usado para desenvolver o projeto.
HTML: A animação final é exportada para um arquivo HTML, permitindo visualização no navegador.
Requisitos / Requirements
Pré-requisitos / Prerequisites:
Python 3.11 ou superior: É necessário ter o Python instalado em sua máquina.
Bibliotecas Python: Pandas e Plotly são necessárias para rodar o script.
Você pode instalar essas bibliotecas utilizando o pip:

bash
Copiar código
pip install pandas plotly
Arquivos Necessários / Required Files:
imigrantes_canada.csv: Um arquivo CSV contendo os dados de imigração, com as colunas para país, continente, região e anos de 1980 a 2013.
BrasileArgentina.html: O arquivo HTML gerado que contém a animação interativa da imigração, que pode ser visualizado em qualquer navegador.
Como Executar / How to Run
1. Clonando o repositório / Clone the repository
Clone o repositório para sua máquina local. No terminal, execute o seguinte comando:

bash
Copiar código
git clone https://github.com/SergioLuiz10/Engenharias.git
Clone the repository to your local machine. Run the following command in the terminal:

bash
Copiar código
git clone https://github.com/SergioLuiz10/Engenharias.git
2. Instalando Dependências / Installing Dependencies
Certifique-se de que você tem as bibliotecas necessárias instaladas. Caso contrário, instale-as com o seguinte comando:

Make sure you have the necessary libraries installed. If not, install them using the following command:

bash
Copiar código
pip install pandas plotly
3. Executando o Script / Running the Script
No VS Code ou terminal, execute o script Python BrasArg.py:

In VS Code or terminal, run the Python script BrasArg.py:

bash
Copiar código
python BrasArg.py
4. Visualizando a Animação / Viewing the Animation
Após rodar o script, um arquivo HTML chamado BrasileArgentina.html será gerado. Abra esse arquivo em seu navegador para visualizar a animação interativa.

After running the script, an HTML file called BrasileArgentina.html will be generated. Open this file in your browser to view the interactive animation.

Imagem do Projeto / Project Image
Exemplo de visualização do gráfico:
Português: Aqui está uma captura de tela de como a animação do gráfico de imigração se parecerá ao ser executada.

English: Here is a screenshot of how the immigration animation plot will look when run.


Explicação do Código / Code Explanation
1. Leitura dos Dados / Data Loading
O arquivo imigrantes_canada.csv é carregado utilizando a biblioteca Pandas, que converte o arquivo CSV em um DataFrame para facilitar a manipulação dos dados.

The imigrantes_canada.csv file is loaded using the Pandas library, which converts the CSV file into a DataFrame for easier data manipulation.

2. Filtro de Dados / Data Filtering
O código filtra os dados para considerar apenas os países Brasil e Argentina, que são os focos da visualização.

The code filters the data to consider only Brazil and Argentina, which are the focus of the visualization.

3. Criação do Gráfico / Plot Creation
O gráfico é criado usando a biblioteca Plotly. Duas linhas são geradas, uma para o Brasil e outra para a Argentina, e os dados são animados para mostrar a evolução da imigração ao longo dos anos.

The plot is created using the Plotly library. Two lines are created, one for Brazil and the other for Argentina, and the data is animated to show the evolution of immigration over the years.

4. Animação / Animation
A animação é configurada para ser controlada pelos botões Play, Pause, Next e Previous. Esses botões permitem avançar, pausar ou navegar manualmente pelos anos da animação.

The animation is set up to be controlled by the Play, Pause, Next, and Previous buttons. These buttons allow advancing, pausing, or manually navigating through the years of the animation.

Contribuindo / Contributing
Se você deseja contribuir para este projeto, sinta-se à vontade para abrir um pull request ou um issue. Fique à vontade para melhorar a visualização ou adicionar novas funcionalidades!

If you want to contribute to this project, feel free to open a pull request or an issue. Feel free to improve the visualization or add new features!

Licença / License
Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.

This project is licensed under the MIT License - see the LICENSE file for more details.
