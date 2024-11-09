

### Documentação Detalhada

#### 1. Introdução
Este software é um gerador de PDF que extrai conteúdo de um vídeo e de uma página web, organizando os dados em um arquivo PDF. Faz uso de bibliotecas como `cv2` para manipulação de vídeos, `requests` e `BeautifulSoup` para scraping de sites e `FPDF` para criação de PDFs.

#### 2. Instalação
Para instalar as bibliotecas necessárias, utilize o seguinte comando:
```bash
pip install opencv-python requests beautifulsoup4 fpdf
```

#### 3. Uso
- Altere a variável `video_path` para o caminho do vídeo que deseja processar.
- Altere a variável `url` para o URL da página da qual você quer extrair o conteúdo.
- Execute o script. O PDF resultante será salvo como `Extracted_Content.pdf`.

Exemplo de como rodar o script:
```bash
python script.py
```

#### 4. Referência de API
- **PDFGenerator**: Classe responsável pela criação de PDFs.
  - `__init__(self, title)`: Inicializa o PDF com um título.
  - `add_text(self, text)`: Adiciona texto ao PDF.
  - `save(self, filename)`: Salva o PDF com o nome especificado.

- `extract_video_content(video_path)`: Extrai conteúdo de um vídeo. Retorna uma lista de frames processados.
  - Parâmetro: `video_path` (str): Caminho do arquivo de vídeo.

- `scrape_website(url)`: Extrai textos de parágrafos de uma página web. Retorna uma lista de textos extraídos.
  - Parâmetro: `url` (str): URL da página a ser analisada.

#### 5. Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para fazer fork do repositório e enviar as suas melhorias.

#### 6. Licença
Este projeto é licenciado sob a MIT License. Veja o arquivo LICENSE para mais informações.