from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

# Local Ollama model (phi3)
llm = ChatOllama(
    model="phi3",
    temperature=0.7
)

def generate_restaurant_name_and_items(cuisine: str):
    # Prompt 1: Restaurant name
    name_prompt = PromptTemplate(
        input_variables=["cuisine"],
        template=(
            "I want to open a restaurant for {cuisine} food.\n"
            "Suggest ONE fancy restaurant name.\n"
            "Do NOT use quotes.\n"
            "Return only the name."
        )
    )


    name_chain = name_prompt | llm

    # Prompt 2: Menu items
    menu_prompt = PromptTemplate(
        input_variables=["restaurant_name"],
        template=(
            "You are a chef.\n"
            "Given the restaurant name '{restaurant_name}', "
            "suggest 8 menu items (food dishes only).\n"
            "Return them as a comma-separated list."
        )
    )

    menu_chain = menu_prompt | llm

    # Sequential execution (replacement for SequentialChain)
    restaurant_name = name_chain.invoke({"cuisine": cuisine}).content
    restaurant_name = restaurant_name.strip().strip('"').strip("'")
    menu_items = menu_chain.invoke(
        {"restaurant_name": restaurant_name}
    ).content

    return {
        "restaurant_name": restaurant_name,
        "menu_items": menu_items
    }


if __name__ == "__main__":
    print(generate_restaurant_name_and_items("Italian"))
