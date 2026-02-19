

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_ollama import OllamaLLM
import json


def create_resume_extractor():
    """
    Creates a resume information extraction pipeline using JsonOutputParser.
    Returns a chain that extracts structured data from resume text.
    """
    
    # Initialize the Ollama LLM
    llm = OllamaLLM(model="mistral")
    
    # Initialize the JSON output parser
    output_parser = JsonOutputParser()
    
    # Get format instructions for JSON output
    format_instructions = output_parser.get_format_instructions()
    
    # Create a detailed prompt template for resume extraction
    prompt_template = PromptTemplate(
        input_variables=["resume_text"],
        template="""Extract structured information from the following resume text. 
You must output valid JSON format only.

{format_instructions}

The JSON should contain exactly these fields:
- "name": Full name of the person (string)
- "email": Email address (string)
- "skills": List of technical and professional skills (array of strings)
- "experience_years": Total years of professional experience (integer)
- "education": List of educational qualifications (array of strings)

Resume Text:
{resume_text}

Remember: Output ONLY valid JSON, nothing else.""",
        partial_variables={"format_instructions": format_instructions}
    )
    
    # Chain components: prompt -> model -> parser
    chain = prompt_template | llm | output_parser
    
    return chain


def validate_resume_data(data: dict) -> bool:
    """
    Validates that the extracted resume data contains all required fields.
    
    Args:
        data: Dictionary containing extracted resume information
        
    Returns:
        True if all required fields are present and valid, False otherwise
    """
    required_fields = ["name", "email", "skills", "experience_years", "education"]
    
    # Check if all required fields are present
    for field in required_fields:
        if field not in data:
            return False
    
    # Validate field types
    if not isinstance(data["name"], str):
        return False
    if not isinstance(data["email"], str):
        return False
    if not isinstance(data["skills"], list):
        return False
    if not isinstance(data["experience_years"], int):
        return False
    if not isinstance(data["education"], list):
        return False
    
    return True


def main():
    """
    Main function demonstrating the resume information extractor.
    """
    print("=" * 70)
    print("Assignment 2: Resume Information Extractor using JsonOutputParser")
    print("=" * 70)
    
    # Create the extractor chain
    chain = create_resume_extractor()
    
    # Example resume text
    resume_text = """
    JOHN SMITH
    john.smith@email.com | (555) 123-4567
    
    PROFESSIONAL SUMMARY
    Experienced software engineer with 5 years of professional experience in full-stack web development.
    Skilled in Python, JavaScript, and cloud technologies. Passionate about building scalable applications.
    
    TECHNICAL SKILLS
    Programming Languages: Python, JavaScript, Java, SQL
    Web Frameworks: Django, React, FastAPI
    Databases: PostgreSQL, MongoDB, MySQL
    Cloud Platforms: AWS, Google Cloud Platform
    Other: Docker, Kubernetes, Git, Linux
    
    WORK EXPERIENCE
    Senior Developer at TechCorp (2021-Present) - 3 years
    - Led development of microservices architecture using Python and Docker
    - Mentored junior developers
    
    Junior Developer at StartupXYZ (2019-2021) - 2 years
    - Developed full-stack web applications using React and Django
    - Implemented responsive UI designs
    
    EDUCATION
    Bachelor of Science in Computer Science
    VTU (2019)
    """
    
    print("\nInput Resume Text:")
    print("-" * 70)
    print(resume_text)
    print("-" * 70)
    
    try:
        print("\nExtracting information with JsonOutputParser...")
        result = chain.invoke({"resume_text": resume_text})
        
        print("\nExtracted Data (JSON):")
        print("-" * 70)
        print(json.dumps(result, indent=2))
        print("-" * 70)
        
        # Validate the extracted data
        if validate_resume_data(result):
            print("\n✅ Validation: All required fields are present and valid!")
            
            print("\nFormatted Output:")
            print("-" * 70)
            print(f" Name: {result['name']}")
            print(f" Email: {result['email']}")
            print(f" Experience: {result['experience_years']} years")
            print(f"\n Skills ({len(result['skills'])} total):")
            for skill in result['skills']:
                print(f"   • {skill}")
            print(f"\n Education ({len(result['education'])} qualifications):")
            for edu in result['education']:
                print(f"   • {edu}")
            print("-" * 70)
        else:
            print("\n❌ Validation failed! Some required fields are missing or invalid.")
            
    except json.JSONDecodeError as e:
        print(f"\nJSON Decoding Error: {e}")
        print("Note: The LLM may not have returned valid JSON. This can happen with some models.")
    except Exception as e:
        print(f"\nError during processing: {e}")
        raise


if __name__ == "__main__":
    main()
