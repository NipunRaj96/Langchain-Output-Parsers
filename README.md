# 🧩 Langchain Output Parsers

This repository showcases my hands-on exploration of **Langchain Output Parsers** — tools used to parse and structure the responses from Language Models (LLMs) into more reliable and usable formats. Through these examples, I learned how to turn raw LLM outputs into structured data for downstream applications.

---

## 🚀 What I Learned

- **StringOutputParser**  
  How to extract simple string responses from LLMs for quick and direct usage.

- **StructuredOutputParser**  
  How to define structured schemas using format instructions and extract fielded outputs directly from LLM completions.

- **JsonOutputParser**  
  How to ensure the LLM responds strictly in JSON format, and how to safely parse this response using Langchain's JSON utilities.

- **PydanticOutputParser**  
  How to use Python's `pydantic` library to define strict data models and parse validated, strongly typed outputs from LLMs.

---

## 📂 Repository Files

- `str_output_parser.py` and `str_output_parser1.py` – Demonstrates usage of **StringOutputParser** to extract plain text responses.
- `structured_output_parser.py` – Uses **StructuredOutputParser** to extract specific fields from LLM output using format instructions.
- `json_output_parser.py` – Forces and parses LLM output in JSON using **JsonOutputParser**.
- `pydantic_output_parser.py` – Uses **PydanticOutputParser** to enforce schema-based responses using **pydantic.BaseModel.**

---

## 🙋‍♂️ Author

**Nipun Kumar**  
[🌐 Portfolio](https://nipun.framer.website) • [🐙 GitHub](https://github.com/NipunRaj96) • [💼 LinkedIn](https://www.linkedin.com/in/nipunkumar01)
