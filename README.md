## Modelo de IA para Deploy em VPS Própria

Objetivo: Criar uma API local para realizar atividades simples, como conversão de PDF para DataFrame e automação de pequenos processos, sem custo de requisição.

---

## Todo List:

### Settar modelo com client API local:

-   [ ] Criar endpoint com POST para input e retorno de resultado + output
-   [ ] Rodar primeira rodada de testes com casos reais em localhost para medir consumo de recursos da máquina

### Deploy do modelo:

-   [ ] Deploy na VPS
-   [ ] Rodar segunda rodada de testes com casos reais em full capacity já em live para testar a performance na VPS

---

## Target de modelo para usar:

**Modelo principal:** Deepseek (caso o host suporte e o preço seja razoável)

**Modelos reserva caso Deepseek seja inviável:**

-   GPT-3.5
-   GPT-4
-   GPT O1-Mini
-   LLaMA

## Modelos para baixar e implementar:

-   [ModelZoo](https://modelzoo.co/)
-   [PyTorch Vision Models](https://pytorch.org/docs/stable/torchvision/models.html)
-   [TensorFlow Hub](https://tfhub.dev/s?subtype=module,placeholder)
-   [AI Model Zoos (GitHub)](https://github.com/collections/ai-model-zoos)
