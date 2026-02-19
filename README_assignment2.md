# Assignment 2: Resume Information Extractor

## Overview

This assignment demonstrates the creation of an AI-powered resume information extraction system using LangChain's JsonOutputParser. The system analyzes resume text and extracts structured data including personal information, skills, experience, and education into a standardized JSON format.

## Features

- **Structured Data Extraction**: Extracts specific fields from unstructured resume text
- **JSON Output**: Uses JsonOutputParser for reliable structured data generation
- **Data Validation**: Validates extracted data for completeness and type correctness
- **LangChain Integration**: Demonstrates advanced prompt engineering with format instructions
- **Ollama LLM**: Leverages local Mistral model for information extraction

## Requirements

- Python 3.8+
- Ollama installed and running
- Mistral model pulled (`ollama pull mistral`)
- Required packages: langchain-core, langchain-ollama

## Installation

1. Ensure Ollama is installed and running:
   ```bash
   ollama serve
   ```

2. Pull the Mistral model:
   ```bash
   ollama pull mistral
   ```

3. Install required Python packages:
   ```bash
   pip install langchain-core langchain-ollama
   ```

## Usage

Run the assignment:

```bash
python assignment2_resume_extractor.py
```

The program will:
1. Create a resume extraction chain with JSON output parsing
2. Process a sample resume text
3. Extract structured information into JSON format
4. Validate the extracted data
5. Display formatted results

## Code Structure

### `create_resume_extractor()`
- Initializes Ollama LLM with Mistral model
- Creates JsonOutputParser for structured output
- Defines detailed prompt template with format instructions
- Returns a LangChain chain (prompt → LLM → parser)

### `validate_resume_data(data)`
- Validates extracted JSON data for required fields
- Checks data types (string, list, integer)
- Ensures data completeness and correctness

### `main()`
- Demonstrates the complete extraction pipeline
- Shows input processing and JSON output handling
- Includes data validation and formatted display

## Expected JSON Output Format

The system extracts data into this JSON structure:

```json
{
  "name": "Full Name",
  "email": "email@address.com",
  "skills": ["Skill 1", "Skill 2", "Skill 3"],
  "experience_years": 5,
  "education": ["Degree 1", "Degree 2"]
}
```

## Key Components

### JsonOutputParser
- Ensures LLM outputs valid JSON format
- Provides format instructions to guide the model
- Automatically parses JSON responses
- Handles JSON decoding errors gracefully

### Format Instructions
The parser generates specific instructions for the LLM:
```
The output should be formatted as a JSON instance that conforms to the JSON schema below.

As an example, for the schema {"properties": {"foo": {"title": "Foo", "description": "a list of strings", "type": "array", "items": {"type": "string"}}}, "required": ["foo"]}}
the object {"foo": ["bar", "baz"]} is a well-formatted instance of the schema. The object {"properties": {"foo": ["bar", "baz"]}} is not well-formatted.
```

## Learning Objectives

- Understanding JsonOutputParser for structured data extraction
- Working with format instructions for reliable LLM outputs
- Implementing data validation for extracted information
- Handling JSON parsing and error management
- Creating robust information extraction pipelines

## Example

Input resume text produces structured JSON with:
- Personal information (name, email)
- Technical skills as an array
- Total experience in years
- Educational qualifications as an array

The system validates all extracted data and provides formatted output for easy reading.</content>
<parameter name="filePath">c:\Users\jhanv\OneDrive\Documents\ollama\README_assignment2.md