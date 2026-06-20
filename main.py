import os
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types
from system_prompt import system_prompt
from call_function import call_function, available_functions



def main():

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key == None:
        raise RuntimeError("Missing api_key")
    client = genai.Client(api_key=api_key)

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    
    messages: list[types.Content] = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=messages,
    config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt))

    function_response: list[types.Part] = []
    if not response.usage_metadata:
        raise RuntimeError("Error happened ?")
    if args.verbose == True:
        print (f"User prompt: {args.user_prompt}")
        print (f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print (f"Response tokens: {response.usage_metadata.candidates_token_count}")
    if response.function_calls:
        for function_call in response.function_calls:
            function_call_result = call_function(function_call, args.verbose)
            if not function_call_result.parts:
                raise Exception("Parts list is empty!")
            if function_call_result.parts[0].function_response is None:
                raise Exception("Function response is missing!")
            if function_call_result.parts[0].function_response.response is None:
                raise Exception("Response data is missing!")
            function_response.append(function_call_result.parts[0])
            if args.verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")
    else:
        print(response.text)
    print(response.text)
if __name__ == "__main__":
    main()
