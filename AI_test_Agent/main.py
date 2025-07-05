
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from Vector import retriever

model = OllamaLLM(model="llama3.2")

template  = """

You are an expert in answering questions based on product reviews. Your task is to provide accurate and helpful answers to the questions based on the provided reviews.

Here are some examples of reviews: {reviews}

He are some examples of questions: {questions}

"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model
while True :
    print("\n\n-----------")
    UserInput  = input( "Ask your question ( q to quit ): " )
    print("\n\n")
    if UserInput.lower() == "q":
        break
    reviews = retriever.invoke(UserInput)
    print("Retrieved reviews:", reviews)
    results = chain.invoke({
    "reviews": reviews,
    "questions": UserInput
    })

print(results)