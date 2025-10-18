# LangChain Runnables

A comprehensive demonstration project showcasing custom implementations of LangChain's Runnable interface and best practices for building modular AI applications.

## 📋 Overview

This project demonstrates how to create custom runnable components from scratch, implementing the LangChain Runnable interface to build modular and chainable AI components. It includes examples of prompt templates, language models, and proper deprecation handling for evolving APIs.

## 🚀 Features

- **Custom Runnable Implementation**: Build your own runnable components that integrate seamlessly with LangChain
- **Prompt Template Management**: Custom prompt templates with variable substitution
- **Deprecation Handling**: Proper implementation of deprecation warnings for API evolution
- **Modular Architecture**: Clean, extensible design following LangChain patterns
- **Type Safety**: Built with Python type hints and abstract base classes

## 🛠️ Installation

### Prerequisites

- Python >= 3.12
- Virtual environment (recommended)

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Langchain_Runnables
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv .venv
   # On Windows
   .venv\Scripts\activate
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 📦 Dependencies

This project includes the following key dependencies:

- **LangChain Core**: `langchain-core>=0.3.76` - Core LangChain functionality
- **LangChain**: `langchain>=0.3.27` - Main LangChain library
- **LangChain Integrations**:
  - `langchain-openai>=0.3.33` - OpenAI integration
  - `langchain-google-genai>=2.1.10` - Google GenAI integration
  - `langchain-huggingface>=0.3.1` - HuggingFace integration
- **ML Libraries**:
  - `sentence-transformers>=5.1.0` - Sentence embeddings
  - `scikit-learn>=1.7.2` - Machine learning utilities
- **Utilities**:
  - `pydantic>=2.11.9` - Data validation
  - `python-dotenv>=1.1.1` - Environment management
  - `streamlit>=1.49.1` - Web interface

## 🏗️ Project Structure

```
├── dummy_runnable_from_scratch_demo.py  # Main demonstration file
├── pyproject.toml                       # Project configuration
├── requirements.txt                     # Dependencies
├── README.md                           # This file
├── .gitignore                          # Git ignore rules
└── .venv/                              # Virtual environment
```

## 💻 Usage

### Basic Example

```python
from dummy_runnable_from_scratch_demo import dummyPromptTemplate, dummyLLM

# Create a prompt template
prompt = dummyPromptTemplate(
    template="Hello {name}, welcome to {place}!",
    input_variables=["name", "place"]
)

# Use the template
result = prompt.invoke({"name": "Alice", "place": "LangChain"})
print(result)  # Output: Hello Alice, welcome to LangChain!

# Create an LLM instance
llm = dummyLLM()
```

### Deprecation Handling

The project demonstrates proper deprecation handling:

```python
# Using deprecated method (will show warning)
result = prompt.format({"name": "Bob", "place": "AI World"})

# Recommended approach
result = prompt.invoke({"name": "Bob", "place": "AI World"})
```

## 🔧 Key Components

### Runnable Abstract Base Class

```python
class Runnable(ABC):
    @abstractmethod
    def invoke(args):
        pass
```

### Custom Prompt Template

- **Purpose**: Template management with variable substitution
- **Key Methods**: 
  - `invoke()` - Primary method for template processing
  - `format()` - Deprecated method with proper warning

### Custom LLM

- **Purpose**: Demonstration of LLM integration patterns
- **Features**: Extensible design for different LLM providers

## ⚠️ Deprecation Warnings

This project demonstrates best practices for API deprecation:

- Clear warning messages indicating the deprecated method
- Alternative method recommendations
- Proper `stacklevel` for accurate error reporting
- Backward compatibility during transition periods

## 🧪 Development

### Running Tests

```bash
python -m pytest
```

### Code Quality

```bash
# Format code
black .

# Lint code
flake8 .

# Type checking
mypy .
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📚 Learning Resources

- [LangChain Documentation](https://python.langchain.com/)
- [LangChain Runnable Interface](https://python.langchain.com/docs/concepts/runnables/)
- [Python Abstract Base Classes](https://docs.python.org/3/library/abc.html)
- [Python Deprecation Warnings](https://docs.python.org/3/library/warnings.html)

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🔗 Related Projects

- [LangChain](https://github.com/langchain-ai/langchain)
- [LangChain Core](https://github.com/langchain-ai/langchain/tree/master/libs/core)
- [LangSmith](https://smith.langchain.com/)

## 📧 Contact

For questions, suggestions, or collaboration opportunities, please open an issue on GitHub.

---

**Note**: This is a demonstration project for educational purposes. For production use, consider using the official LangChain components and following their latest best practices.