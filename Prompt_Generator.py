from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    validate_template=True,
    input_variables=["paper_input","style_input","length_input"],
    template="""
    Please summarize the research paper titled “{paper_input}” with the following specifications:
    Explanation Style: {style_input}
    Explanation Length: {length_input}

    1. Mathematical Details:
       - Include relevant mathematical equations if present.
       - Explain math concepts with simple code snippets if applicable.

    2. Analogies:
       - Use relatable analogies to simplify complex ideas.

    If certain information is not available, respond with:
    “Insufficient information available”.
    
    Ensure the summary is clear, accurate, and aligned with the style and length.
    """
)

template.save("template.json")