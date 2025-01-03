# Solar System AI Agent

This project demonstrates the use of generative AI agents with support for multiple LLM providers. The application is designed to operate in Portuguese (pt-BR) and is intended for educational purposes.

## Features

- **Generative AI Agents**: Implement agents that follow a predefined cycle of thought, action, pause, and observation.
- **Multi-Provider LLM Support**: Utilize LLMs from different providers using the `LLMFactory`.
- **Open Source**: The project is open-source and available for learning and experimentation.

## Usage Instructions

### Prerequisites

- Python 3.8 or higher
- Install required packages:
    ```bash
    pip install -r requirements.txt
    ```

### Configuration

1. Copy the `.env.example` file to `.env` and fill in your API keys:
    ```bash
    cp .env.example .env
    ```

2. Edit the `.env` file to include your API keys:
    ```env
    MISTRAL_AI_KEY=your_mistral_api_key
    GROQ_API_KEY=your_groq_api_key
    ```

### Running the Application

1. Run the main script:
    ```bash
    python main.py
    ```

2. The application will prompt you to enter a question in Portuguese. For example:
    ```plaintext
    Qual é a massa combinada da Terra e de Marte?
    ```

3. The agent will follow the predefined cycle to provide an answer using the available actions.

### Example

```plaintext
Pergunta: Qual é a massa combinada da Terra e de Marte?

Pensamento: Primeiro preciso obter a massa da Terra usando a ação planet_mass.
Ação: planet_mass: Earth
PAUSA

Observação: A Terra tem uma massa de 5.972 × 10^24 kg

Pensamento: Agora preciso da massa de Marte usando a mesma ação.
Ação: planet_mass: Mars
PAUSA

Observação: Marte tem uma massa de 0.64171 × 10^24 kg

Pensamento: Com ambas as massas, posso calcular a soma usando a ação calculate.
Ação: calculate: 5.972 + 0.64171
PAUSA

Observação: 6.61371

Pensamento: Agora tenho todos os dados necessários através das ações disponíveis.
Resposta: A massa combinada da Terra e Marte é 6.61371 × 10^24 kg
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.