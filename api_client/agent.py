import json
from django.conf import settings
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.tools import tool
from .services import MaxoMartClient

# Initialize OpenAI
llm = ChatOpenAI(
    api_key=settings.OPENAI_API_KEY,
    model=settings.OPENAI_MODEL,
    temperature=0.1
)

# Initialize Client (Creates a new session per request)
client = MaxoMartClient()


@tool
def get_live_products() -> str:
    """Fetch a list of products from the live MaxoMart website."""
    try:
        client.login()
        data = client.get_products()
        # Just return the first 10 products to save tokens
        products = data.get("items", [])[:10]
        return json.dumps(products)
    except Exception as e:
        return f"Error: {str(e)}"

@tool
def get_user_cart() -> str:
    """Get the current user's shopping cart from MaxoMart."""
    try:
        client.login()
        cart = client.get_cart()
        return json.dumps(cart)
    except Exception as e:
        return f"Error: {str(e)}"


tools = [get_live_products, get_user_cart]
llm_with_tools = llm.bind_tools(tools)

def run_agent(message_text: str):
    """Executes the agent with tools."""
    messages = [
        SystemMessage(content=(
            "You are a helpful customer support AI for MaxoMart. "
            "Use your tools to answer questions about products or the user's cart. "
            "When listing products, DO NOT include image markdown or image URLs. "
            "Instead, provide a clean list with the product name, price, rating, stock, and a clickable text link "
            "to the product page (e.g., [View Product](https://demo.maxoperf.com/products/slug)). "
            "Keep responses concise and professional."
        )),
        HumanMessage(content=message_text)
    ]
    
    # 1. Ask OpenAI
    response = llm_with_tools.invoke(messages)
    
    # 2. Check if OpenAI wants to use a tool
    if response.tool_calls:
        messages.append(response)
        for tool_call in response.tool_calls:
            tool_name = tool_call["name"]
            tool_func = next((t for t in tools if t.name == tool_name), None)
            
            if tool_func:
                # Execute the tool
                tool_result = tool_func.invoke(tool_call["args"])
                messages.append({"role": "tool", "content": tool_result, "tool_call_id": tool_call["id"]})
        
        # 3. Get final answer from OpenAI
        final_response = llm_with_tools.invoke(messages)
        return final_response.content
    
    return response.content
    
    # 1. Ask OpenAI
    response = llm_with_tools.invoke(messages)
    
    # 2. Check if OpenAI wants to use a tool
    if response.tool_calls:
        messages.append(response)
        for tool_call in response.tool_calls:
            tool_name = tool_call["name"]
            tool_func = next((t for t in tools if t.name == tool_name), None)
            
            if tool_func:
                # Execute the tool
                tool_result = tool_func.invoke(tool_call["args"])
                messages.append({"role": "tool", "content": tool_result, "tool_call_id": tool_call["id"]})
        
        # 3. Get final answer from OpenAI
        final_response = llm_with_tools.invoke(messages)
        return final_response.content
    
    return response.content