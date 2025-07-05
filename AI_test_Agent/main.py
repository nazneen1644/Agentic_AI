
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model = OllamaLLM(model="llama3.2")

template  = """

You are an expert in answering questions about pizza resturants

Here are some examples of reviews: {reviews}

He are some examples of questions: {questions}

"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

results = chain.invoke({
    "reviews": [],
    "questions": "What is the best pizza place in town? "
})

print(results)