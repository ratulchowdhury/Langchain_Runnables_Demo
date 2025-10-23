# LangChain Runnables Demo

A comprehensive demonstration project showcasing LangChain's Runnable interface patterns and advanced chaining techniques for building modular AI applications.

## 📋 Overview

This project provides practical examples of LangChain's core Runnable components, demonstrating various chaining patterns, parallel execution, conditional logic, and custom implementations. Each demo file focuses on specific Runnable patterns that are essential for building production-ready LangChain applications.

## 🚀 Features

- **🔗 Sequential Chains**: Chain multiple LLM calls with `RunnableSequence`
- **⚡ Parallel Processing**: Execute multiple chains simultaneously with `RunnableParallel`
- **🔀 Conditional Logic**: Implement branching logic with `RunnableBranch`
- **🔄 Data Passthrough**: Preserve input data with `RunnablePassthrough`
- **⚙️ Custom Functions**: Integrate custom logic with `RunnableLambda`
- **🏗️ Custom Runnables**: Build your own runnable components from scratch
- **⚠️ Deprecation Handling**: Proper API evolution with deprecation warnings
- **🤖 Multi-Provider Support**: OpenAI and HuggingFace integrations
- **📊 Output Parsing**: JSON and string output formatting

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
├── dummy_runnable_from_scratch_demo.py   # Custom Runnable implementation from scratch
├── runnable_sequence_demo.py             # Sequential chain execution patterns
├── runnable_parallel_demo.py             # Parallel execution examples
├── runnable_branch_demo.py               # Conditional branching logic
├── runnable_passthrough_demo.py          # Data passthrough patterns
├── runnable_lambda_demo.py               # Custom function integration
├── pyproject.toml                        # Project configuration
├── requirements.txt                      # Dependencies
├── .env                                  # Environment variables (API keys)
├── README.md                            # This documentation
├── .gitignore                           # Git ignore rules
└── .venv/                               # Virtual environment
```

## 📚 Demo Files Overview

### 🔧 `dummy_runnable_from_scratch_demo.py`
**Purpose**: Learn how to create custom Runnable components from scratch
- Abstract base class implementation
- Custom prompt template with deprecation warnings
- Custom LLM wrapper
- Best practices for API evolution

### 🔗 `runnable_sequence_demo.py` 
**Purpose**: Chain multiple operations in sequence
- Sequential LLM calls
- Output parsing between chains
- JSON format instructions
- Error handling patterns

### ⚡ `runnable_parallel_demo.py`
**Purpose**: Execute multiple chains simultaneously
- Parallel content generation (article + tweet)
- Performance optimization
- Result aggregation
- Concurrent processing patterns

### 🔀 `runnable_branch_demo.py`
**Purpose**: Implement conditional logic and branching
- Conditional chain execution
- Dynamic routing based on input
- Multi-path processing
- Decision tree patterns

### 🔄 `runnable_passthrough_demo.py`
**Purpose**: Preserve and pass data through chains
- Input data preservation
- Context maintenance
- Data flow control
- Information retention patterns

### ⚙️ `runnable_lambda_demo.py`
**Purpose**: Integrate custom functions and transformations
- Custom data processing
- Function integration
- Data transformation
- Custom logic injection

## � Quick Start

### 1. Environment Setup

Create a `.env` file in the project root:

```bash
OPENAI_API_KEY=your_openai_api_key_here
HUGGINGFACE_API_KEY_FINEGRAINED=your_hf_token_here  # Optional for HF models
```

### 2. Run Demo Files

Each demo can be run independently:

```bash
# Sequential chains
python runnable_sequence_demo.py

# Parallel processing  
python runnable_parallel_demo.py

# Conditional branching
python runnable_branch_demo.py

# Data passthrough
python runnable_passthrough_demo.py

# Custom functions
python runnable_lambda_demo.py

# Custom runnables
python dummy_runnable_from_scratch_demo.py
```

## 💻 Usage Examples

### 🔗 Sequential Chain Example

```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Create chain components
llm = ChatOpenAI(model="gpt-4o", temperature=0.5)
prompt = PromptTemplate(template="Tell me about {topic}", input_variables=["topic"])
parser = StrOutputParser()

# Create sequential chain
chain = prompt | llm | parser

# Execute
result = chain.invoke({"topic": "LangChain Runnables"})
```

### ⚡ Parallel Execution Example

```python
from langchain_core.runnables import RunnableParallel

# Create parallel chains
parallel_chain = RunnableParallel({
    "article": prompt_article | llm | parser,
    "tweet": prompt_tweet | llm | parser
})

# Execute both simultaneously
results = parallel_chain.invoke({"topic": "AI News"})
print(results["article"])  # Generated article
print(results["tweet"])    # Generated tweet
```

### 🔀 Branching Example

```python
from langchain_core.runnables import RunnableBranch

# Create conditional chain
branch = RunnableBranch(
    (lambda x: "urgent" in x["topic"].lower(), urgent_chain),
    (lambda x: "news" in x["topic"].lower(), news_chain),
    default_chain  # Default case
)

result = branch.invoke({"topic": "Urgent: Breaking News"})
```

### 🏗️ Custom Runnable Example

```python
from dummy_runnable_from_scratch_demo import dummyPromptTemplate

# Create custom prompt template
prompt = dummyPromptTemplate(
    template="Hello {name}, welcome to {place}!",
    input_variables=["name", "place"]
)

# Use with proper method
result = prompt.invoke({"name": "Alice", "place": "LangChain"})

# Deprecated method (shows warning)
result = prompt.format({"name": "Bob", "place": "AI World"})
```

## 🔧 Key Runnable Types

### Core LangChain Runnables

| Runnable | Purpose | Use Case |
|----------|---------|----------|
| `RunnableSequence` | Chain operations sequentially | Multi-step processing |
| `RunnableParallel` | Execute operations in parallel | Performance optimization |
| `RunnableBranch` | Conditional execution | Decision-based routing |
| `RunnablePassthrough` | Pass data through unchanged | Context preservation |
| `RunnableLambda` | Wrap custom functions | Custom transformations |

### Custom Runnable Implementation

```python
from abc import ABC, abstractmethod

class Runnable(ABC):
    @abstractmethod
    def invoke(self, input_data):
        """Execute the runnable with given input."""
        pass

class CustomPromptTemplate(Runnable):
    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables
    
    def invoke(self, kwargs):
        return self.template.format(**kwargs)
```

### LLM Provider Support

- **OpenAI**: `ChatOpenAI` for GPT models
- **HuggingFace**: `ChatHuggingFace` for open-source models
- **Custom**: Build your own LLM wrappers

## ⚠️ Deprecation Warnings

This project demonstrates best practices for API deprecation:

- Clear warning messages indicating the deprecated method
- Alternative method recommendations
- Proper `stacklevel` for accurate error reporting
- Backward compatibility during transition periods

## 🛠️ Development & Troubleshooting

### Common Issues

1. **API Key Errors**: Ensure your `.env` file contains valid API keys
2. **Import Errors**: Make sure virtual environment is activated
3. **Model Access**: Some HuggingFace models require authentication

### Running Individual Demos

```bash
# Activate virtual environment first
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Run specific demos
python runnable_sequence_demo.py    # Sequential processing
python runnable_parallel_demo.py    # Parallel execution
python runnable_branch_demo.py      # Conditional logic
python runnable_passthrough_demo.py # Data preservation
python runnable_lambda_demo.py      # Custom functions
```

### Code Quality

```bash
# Format code
black .

# Type checking
mypy .

# Install dev dependencies
pip install black mypy pytest
```

### Performance Tips

- Use `RunnableParallel` for independent operations
- Implement proper error handling in custom runnables
- Cache expensive operations when possible
- Monitor API rate limits

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📚 Learning Path

### Recommended Order

1. **Start Here**: `dummy_runnable_from_scratch_demo.py` - Understand the basics
2. **Sequential Processing**: `runnable_sequence_demo.py` - Learn chaining
3. **Performance**: `runnable_parallel_demo.py` - Parallel execution  
4. **Control Flow**: `runnable_branch_demo.py` - Conditional logic
5. **Data Management**: `runnable_passthrough_demo.py` - Context preservation
6. **Advanced**: `runnable_lambda_demo.py` - Custom functions

### Key Concepts to Master

- **Chain Composition**: Using `|` operator for chaining
- **Input/Output Handling**: Understanding data flow between components
- **Error Handling**: Proper exception management in chains
- **Performance**: When to use parallel vs sequential execution
- **Extensibility**: Building reusable runnable components

## 📖 Additional Resources

- [LangChain Documentation](https://python.langchain.com/)
- [LangChain Runnable Interface](https://python.langchain.com/docs/concepts/runnables/)
- [LangChain Expression Language (LCEL)](https://python.langchain.com/docs/concepts/lcel/)
- [OpenAI API Documentation](https://platform.openai.com/docs/)
- [HuggingFace Transformers](https://huggingface.co/docs/transformers/)
- [Python Abstract Base Classes](https://docs.python.org/3/library/abc.html)

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