# Documentação de Software - QUICKTAG

## 1. Introdução

### 1.1 Visão Geral do Software
O `QUICKTAG` é um aplicativo desenvolvido para gerar e imprimir etiquetas personalizadas com informações sobre produtos para nutriçãoprodução. O software é projetado para facilitar o processo de rotulagem em ambientes internos da Nutrição produção, onde a identificação precisa dos produtos é crucial.

### 1.2 Objetivo e Escopo do Documento
Este documento tem como objetivo fornecer informações detalhadas sobre o `QUICKTAG`, incluindo requisitos, instalação, funcionalidades e suporte. Ele é destinado a desenvolvedores, usuários finais e equipes de suporte.

## 2. Requisitos do Sistema

### 2.1 Requisitos de Hardware e Software
- **Sistema Operacional:** Windows 10 ou superior
- **Memória RAM:** Mínimo de 4 GB
- **Espaço em Disco:** 100 MB livres para instalação e funcionamento
- **Resolução de Tela:** Mínimo de 1024 x 768

### 2.2 Dependências Externas
- **Python 3.7 ou superior**
- Bibliotecas Python:
  - `customtkinter`
  - `PyPDF2`
  - `reportlab`
  - `pyautogui`
- **Adobe Acrobat Reader** (ou similar) para visualização e impressão de PDFs.

## 3. Instalação e Configuração

### 3.1 Instruções de Instalação Passo a Passo
1. **Instale o Python:**
   - Baixe e instale o Python a partir do [site oficial](https://www.python.org/).
   - Durante a instalação, marque a opção para adicionar Python ao PATH.

2. **Instale as Dependências:**
   - Abra o prompt de comando e execute:
     ```bash
     pip install customtkinter PyPDF2 reportlab pyautogui
     ```

3. **Baixe o Software:**
   - Baixe o arquivo do `QUICKTAG` e extraia em uma pasta de sua escolha.

4. **Execute o Aplicativo:**
   - Navegue até a pasta onde o aplicativo foi extraído e execute:
     ```bash
     python MainPRD.py  # Para ambiente de produção
     python MainTEST.py  # Para ambiente de teste e homologação
     ```

### 3.2 Configuração Inicial e Requisitos
- Certifique-se de que o diretório `C:\Program Files (x86)\QUICKTAG\Model` contém o arquivo `Nutri_Model.pdf`.
- O diretório `C:\Program Files (x86)\QUICKTAG\Temp` deve ser criado automaticamente pelo aplicativo.

## 4. Arquitetura do Software

### 4.1 Diagrama de Arquitetura
```plaintext
[User Interface] 
        |
   [Main Application]
        |
   [PDF Generation]
        |
   [File System Interaction]
```
### 3.3 Passo a Passo para Instalação Usando o Setup

1. **Baixe o Instalador:**
   - Baixe o arquivo de instalação `QuickTagSetup.exe` fornecido.

2. **Execute o Instalador:**
   - Dê um duplo clique no arquivo `QuickTagSetup.exe` para iniciar o processo de instalação.

3. **Selecione o Diretório de Instalação:**
   - Por padrão, o QuickTag será instalado no diretório `C:\Program Files (x86)\QuickTag`.
   - Clique em **Avançar**.
   ![Passo 1:](<Pictures/Instalação PASSO 1.png>)

4. **Criação de Atalhos:**
   - Escolha se deseja criar atalhos na área de trabalho ou no menu iniciar. Por padrão, ambos os atalhos são criados.
   - Clique em **Avançar**.
   ![Passo 2:](<Pictures/Instalação PASSO 2.png>)

5. **Confirme a Instalação:**
   - Revise as configurações escolhidas e clique em **Instalar** para iniciar a cópia dos arquivos.
   ![Passo 3:](<Pictures/Instalação PASSO 3.png>)

6. **Finalizar a Instalação:**
   - Após a conclusão da instalação, você pode optar por executar o QuickTag automaticamente marcando a opção **Executar QuickTag**.
   - Clique em **Concluir** para encerrar o instalador.

### 4.2 Descrição dos Componentes Principais
- **Interface do Usuário:** Criada com `customtkinter`, permitindo interação fácil e amigável.
- **Geração de PDF:** Usa `reportlab` para criar PDFs com as informações dos produtos.
- **Manipulação de Arquivos:** Utiliza `PyPDF2` para mesclar e salvar os PDFs gerados.

## 5. Funcionalidades

### 5.1 Descrição Detalhada das Funcionalidades
- **Geração de Etiquetas:** Permite ao usuário inserir informações de produtos e gerar etiquetas em PDF.
- **Impressão Direta:** Abre o gerenciador de impressão automaticamente após a geração do PDF.
- **Limpeza de Campos:** Oferece um botão para limpar todos os campos de entrada rapidamente.
- **Formatação de Data:** Formata automaticamente os campos de data conforme o usuário digita.

### 5.2 Exemplos de Uso
1. Preencha os campos de entrada com o nome do produto, datas de validade e fabricação e ingredientes.
2. Clique no botão "Gerar e Imprimir" para criar e enviar a etiqueta para impressão.

## 6. Interface do Usuário

### 6.1 Capturas de Tela da Interface
![Tela Principal do QUICKTAG](Pictures/Tela_Principal.png)
![Tela de Etiqueta Gerada](Pictures/Tela_Etiqueta.png)

### 6.2 Descrição dos Elementos da Interface
- **Campos de Entrada:** Permitem que o usuário insira informações sobre o produto.
- **Botões:** Iniciam a geração da etiqueta e limpam os campos.
- **Menu de Ajuda:** Oferece assistência sobre como usar o aplicativo.

## 7. API e Integrações
Atualmente, o `QUICKTAG` não possui uma API pública. No entanto, as funções podem ser integradas a outros aplicativos Python, conforme necessário.

## 8. Testes

### 8.1 Estratégia de Testes
Os testes são realizados para garantir que todas as funcionalidades principais estejam operando conforme o esperado, incluindo a geração de PDFs e a impressão.

### 8.2 Casos de Teste e Resultados
- **Caso de Teste 1:** Gerar etiqueta com todos os campos preenchidos.
  - **Resultado:** Etiqueta gerada e enviada para impressão com sucesso.
  
- **Caso de Teste 2:** Gerar etiqueta com campos obrigatórios vazios.
  - **Resultado:** Mensagem de aviso exibida ao usuário.

## 9. Manutenção e Suporte

### 9.1 Instruções para Solução de Problemas Comuns
- ![Problema:](<Pictures/ERRO DE PERMISSÃO.png>) - Erro de Permissão. 
  - **Solução:** Verifique se a pasta com a pasta "QuickTag no Program Files (x86) está as devidas permições.
  ![Passo 1:](<Pictures/Correção erro permissão1.png>)
  ![Passo 2:](<Pictures/Correção erro permissão2.png>)
  ![Passo 3:](<Pictures/Correção erro permissão3.png>)
  ![Passo 4:](<Pictures/Correção erro permissão4.png>)
  ![Passo 5:](<Pictures/Correção erro permissão5.png>)
  ![Passo 6:](<Pictures/Correção erro permissão6.png>)

### 9.2 Como Obter Suporte Técnico
Para suporte técnico, entre em contato com o administrador do sistema.

## 10. Glossário
- **PDF:** Portable Document Format, um formato de arquivo usado para representar documentos de maneira independente de software, hardware e sistemas operacionais.
- **GUI:** Graphical User Interface, uma interface que permite ao usuário interagir com o software usando elementos visuais.

## 11. Referências
- [Documentação do Python](https://docs.python.org/3/)
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)

## 13. Criação do Executável com PyInstaller

### 13.1 Instalação do PyInstaller
Para criar um executável do `QUICKTAG`, é necessário ter o PyInstaller instalado. Para instalá-lo, execute o seguinte comando no prompt de comando:

```bash
pip install pyinstaller
```

### 13.2 Criando o Executável
1. **Abra o Prompt de Comando:**
   - Navegue até o diretório onde o arquivo `MainPRD.py` está localizado.

2. **Execute o PyInstaller:**
   - Execute o seguinte comando para criar o executável:
     ```bash
     pyinstaller --onefile --windowed --icon="C:\Users\marcu\Downloads\icone.ico" MainPRD.py
     ```
   - O parâmetro `--onefile` faz com que o PyInstaller crie um único arquivo executável.
   - O parâmetro `--windowed` impede que uma janela de console seja exibida ao executar o aplicativo (opcional, use apenas se a interface não precisa de console).

3. **Localização do Executável:**
   - Após a conclusão do processo, o executável será criado na pasta `dist`, que estará localizada no mesmo diretório onde o `MainPRD.py` está.

### 13.3 Personalizando o Executável
Você pode personalizar o ícone do executável adicionando a opção `--icon` no comando. Para isso, utilize o seguinte comando:

```bash
pyinstaller --onefile --windowed --icon="Pictures/Quicktag.ico" MainPRD.py
```

### 13.4 Resolvendo Problemas Comuns
- **Erro de Importação:** Se ocorrer um erro de importação, verifique se todas as dependências estão instaladas corretamente.
- **Tamanho do Executável:** O executável pode ser grande devido à inclusão de bibliotecas. O uso do parâmetro `--onefile` ajuda a compactá-lo.

## 13. Criação do Instalador com Inno Setup

### 13.1 Script do Inno Setup
Para criar o instalador do `QUICKTAG`, utilize o seguinte script no Inno Setup:

```ini
[Setup]
AppName=QuickTag
AppVersion=1.0
DefaultDirName={pf}\QuickTag
DefaultGroupName=QuickTag
OutputDir=.
OutputBaseFilename=QuickTagSetup
Compression=lzma
SolidCompression=yes
SetupIconFile="QuickTag/Pictures/Quicktag.ico"
UninstallDisplayIcon={app}\Main.exe

[Files]
Source: "QuickTAG\Setup\dist\Main.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "QuickTAG\Model\Nutri_Model.pdf"; DestDir: "{app}\Model"; Flags: ignoreversion

[Icons]
Name: "{group}\QuickTag"; Filename: "{app}\Main.exe"
Name: "{commondesktop}\QuickTag"; Filename: "{app}\Main.exe"  
Name: "{group}\Uninstall QuickTag"; Filename: "{app}\unins000.exe"

[Run]
Filename: "{app}\Main.exe"; Description: "{cm:LaunchProgram,QuickTag}"; Flags: nowait postinstall skipifsilent

[Dirs]
Name: "{pf}\QuickTag\Model"
Name: "{pf}\QuickTag\Temp"
```

### 13.2 Instruções para Compilação
1. Abra o Inno Setup e crie um novo script.
2. Copie e cole o script fornecido acima no editor.
3. Salve o arquivo com um nome apropriado, por exemplo, `QuickTagSetup.iss`.
4. Clique em **Compile** para gerar o instalador.
5. O instalador será salvo no diretório especificado pelo `OutputDir`.

---