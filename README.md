# Transcrição de Áudio com Python

Este repositório contém um script em Python para transcrever áudio de arquivos `.mp3` utilizando a biblioteca `speechrecognition` e `pydub`.

## 🚀 Como Usar

1. **Clone o repositório**:

    ```bash
    git clone https://github.com/LeoMedeiros72/Transcricao_audio.git
    cd Transcricao_audio
    ```

2. **Instale as dependências**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Faça o upload do seu arquivo de áudio `.mp3`**:

    O script aceita arquivos `.mp3` e os converte internamente para `.wav` para transcrição.

4. **Execute o script**:

    ```bash
    python transcricao_audio.py
    ```

O script irá transcrever o áudio e imprimir o texto transcrito no console.

## 📄 Dependências

- `speechrecognition`
- `pydub`
- `google-colab` (se usar no Google Colab)

## ⚙️ Funcionalidades

- **Normalização de áudio**: Ajuste de volume para melhorar a transcrição.
- **Divisão de áudio**: Divide áudios longos em partes menores (30 segundos).
- **Transcrição**: Usa a API Google Speech Recognition para converter áudio em texto.

## 💡 Contribuindo

Sinta-se à vontade para contribuir com melhorias, bugs ou novas funcionalidades. Crie uma issue ou envie um pull request!

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
