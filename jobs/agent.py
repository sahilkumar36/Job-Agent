import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import ResponseSchema, StructuredOutputParser

def analyze_job(job_description, user_skills):
    """
    Analyzes a job description against a user's skills using Google Gemini.
    """
    # Initialize LLM
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash", 
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )
    
    # Define the output structure
    response_schemas = [
        ResponseSchema(name="summary", description="A concise 2-sentence summary of the job role and main requirements."),
        ResponseSchema(name="match_score", description="An integer between 0 and 100 indicating how well the user's skills match the job."),
        ResponseSchema(name="skills_found", description="A list of relevant skills found in both the job description and user's profile."),
        ResponseSchema(name="missing_skills", description="A list of key skills mentioned in the job but missing from the user's profile."),
    ]
    output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
    format_instructions = output_parser.get_format_instructions()
    
    # Define the prompt
    prompt = ChatPromptTemplate.from_template(
        template="""
        As an expert career coach and technical recruiter, analyze the following job description against the provided user skills.
        
        Job Description:
        {job_description}
        
        User's Skills/Profile:
        {user_skills}
        
        {format_instructions}
        
        Provide the analysis in the requested JSON format.
        """
    )
    
    # Generate the response
    messages = prompt.format_messages(
        job_description=job_description,
        user_skills=user_skills,
        format_instructions=format_instructions
    )
    
    response = llm.invoke(messages)
    return output_parser.parse(response.content)
